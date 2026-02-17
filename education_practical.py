"""
ELEVE — Practical Trading Learning Companion (v0.1)
==================================================
A minimal, practice-first "education" module designed for:
- very limited time
- basic trading knowledge
- focus on decision-making, not theory

How to run:
    streamlit run education_practical.py

What it does:
- Daily Decision Card (GO / WAIT / NO-TRADE)
- "Where to wait" zones (BUY / NO-TRADE / SELL)
- Minimal indicator set (EMA + RSI) with parameter guidance
- Micro-journal (1-minute) to learn by repetition

Notes:
- This module is intentionally manual-input-first. You can later plug in live market data.
- It does NOT try to "predict". It enforces a consistent process.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional, Tuple

import streamlit as st


# =========================
# Configuration & constants
# =========================

APP_TITLE = "ELEVE · Practical Trading Companion"
DEFAULT_TIMEZONE = "Europe/Madrid"

DATA_DIR = Path(__file__).with_suffix("")  # folder-like path (same name without .py)
JOURNAL_PATH = Path(str(DATA_DIR) + "_journal.jsonl")


@dataclass
class MonteCarloPanel:
    """Numbers copied from your Monte Carlo panel (manual input for now)."""
    horizon_days: int = 7
    p_up_5: float = 0.21       # Probability of +5% or more
    p_down_5: float = 0.40     # Probability of -5% or more
    p_reach_r1: float = 0.15   # Probability of reaching R1
    median_return: float = -0.029  # Median return (e.g., -2.9% -> -0.029)


@dataclass
class Zones:
    """Action zones, typically derived from supports/resistances/Fib bands."""
    buy_low: float
    buy_high: float
    sell_low: float
    sell_high: float

    def classify_price(self, price: float) -> str:
        if self.buy_low <= price <= self.buy_high:
            return "BUY_ZONE"
        if self.sell_low <= price <= self.sell_high:
            return "SELL_ZONE"
        return "NO_TRADE_ZONE"


@dataclass
class Indicators:
    """Minimal indicator readouts (manual inputs)."""
    ema20: Optional[float] = None
    ema50: Optional[float] = None
    rsi: Optional[float] = None

    def ema_alignment(self, price: float) -> Optional[str]:
        if self.ema20 is None or self.ema50 is None:
            return None
        if price > self.ema20 > self.ema50:
            return "BULL"
        if price < self.ema20 < self.ema50:
            return "BEAR"
        return "RANGE"


@dataclass
class Decision:
    status: str  # GO / WAIT / NO-TRADE
    rationale: str
    next_action: str
    checklist: Dict[str, bool]


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


# =========================
# Decision engine (simple)
# =========================

def decision_engine(
    price: float,
    zones: Zones,
    mc: MonteCarloPanel,
    ind: Indicators,
) -> Decision:
    """
    A deliberately simple engine:
    - First decides if "environment" is favorable (Monte Carlo bias).
    - Then checks if price is in an actionable zone (BUY/SELL vs NO-TRADE).
    - Finally uses minimal confirmation (EMA alignment + RSI threshold) only as a gate.
    """

    zone = zones.classify_price(price)

    # 1) Environment bias from Monte Carlo
    bear_bias = (mc.p_down_5 >= 0.35) and (mc.p_up_5 <= 0.25) and (mc.median_return < 0)
    bull_bias = (mc.p_up_5 >= 0.35) and (mc.p_down_5 <= 0.25) and (mc.median_return > 0)

    # 2) Regime from EMA (optional)
    ema_regime = ind.ema_alignment(price)

    # 3) RSI gate (optional) — keep it brutally simple
    rsi_ok_for_long = (ind.rsi is not None) and (ind.rsi >= 50.0)
    rsi_improving_hint = (ind.rsi is not None) and (45.0 <= ind.rsi < 50.0)

    checklist = {
        "price_in_buy_zone": zone == "BUY_ZONE",
        "price_in_sell_zone": zone == "SELL_ZONE",
        "mc_bear_bias": bear_bias,
        "mc_bull_bias": bull_bias,
        "ema_regime_bull": ema_regime == "BULL" if ema_regime is not None else False,
        "ema_regime_bear": ema_regime == "BEAR" if ema_regime is not None else False,
        "rsi_ok_for_long": rsi_ok_for_long,
        "rsi_improving_hint": rsi_improving_hint,
    }

    # Core policy:
    # - We are swing/spot oriented: prefer BUY_ZONE entries, avoid "middle".
    # - In bear_bias, only allow "GO" for longs if BUY_ZONE + (EMA not BEAR) + RSI ok (or improving).
    # - In bull_bias, we can be more permissive: BUY_ZONE + at least one of (EMA BULL, RSI ok).
    if zone == "NO_TRADE_ZONE":
        return Decision(
            status="WAIT",
            rationale="Precio en zona neutra (NO-TRADE). Espera a que el precio venga a la zona de acción.",
            next_action="Poner alertas en BUY ZONE y SELL ZONE. No operar en el medio.",
            checklist=checklist,
        )

    if zone == "SELL_ZONE":
        return Decision(
            status="NO-TRADE",
            rationale="Precio en zona de resistencia/venta. No abrir longs nuevos en esta zona.",
            next_action="Si ya estás dentro, planifica TP/gestión. Si no, espera pullback a BUY ZONE.",
            checklist=checklist,
        )

    # BUY_ZONE
    if bear_bias:
        # Strict
        if (ema_regime != "BEAR") and (rsi_ok_for_long or rsi_improving_hint):
            return Decision(
                status="GO",
                rationale="Sesgo bajista moderado, pero precio en BUY ZONE con señales mínimas de estabilización.",
                next_action="Entrada escalonada + stop bajo estructura. TP conservador (zona neutra / 0.618).",
                checklist=checklist,
            )
        return Decision(
            status="WAIT",
            rationale="Sesgo bajista y falta confirmación mínima en BUY ZONE.",
            next_action="Esperar confirmación (recuperación EMA20 o RSI > 50) o barrido + recuperación.",
            checklist=checklist,
        )

    if bull_bias:
        if (ema_regime == "BULL") or rsi_ok_for_long:
            return Decision(
                status="GO",
                rationale="Sesgo alcista + BUY ZONE con confirmación suficiente.",
                next_action="Entrada por tramos. Stop bajo el último mínimo. TP por zonas (SELL ZONE / R1).",
                checklist=checklist,
            )
        return Decision(
            status="WAIT",
            rationale="BUY ZONE, pero falta confirmación mínima para que el long sea de calidad.",
            next_action="Espera recuperación de EMA20 o RSI > 50 antes de disparar.",
            checklist=checklist,
        )

    # Neutral environment (no strong bias)
    if (ema_regime == "BULL") and (rsi_ok_for_long or rsi_improving_hint):
        return Decision(
            status="GO",
            rationale="Entorno neutro, pero BUY ZONE con confirmación (EMA + RSI).",
            next_action="Entrada conservadora. TP1 zona neutra. No convertirlo en inversión.",
            checklist=checklist,
        )

    return Decision(
        status="WAIT",
        rationale="BUY ZONE sin confirmación suficiente en entorno neutro.",
        next_action="Esperar estructura (dejar de hacer lower lows) o señal (EMA/RSI).",
        checklist=checklist,
    )


# =========================
# Journal helpers
# =========================

def append_journal(entry: Dict) -> None:
    JOURNAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with JOURNAL_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def read_journal(limit: int = 200) -> list[Dict]:
    if not JOURNAL_PATH.exists():
        return []
    lines = JOURNAL_PATH.read_text(encoding="utf-8").splitlines()
    lines = lines[-limit:]
    out = []
    for ln in lines:
        try:
            out.append(json.loads(ln))
        except json.JSONDecodeError:
            continue
    return out


# =========================
# UI: Streamlit app
# =========================

def render_header() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="🧭", layout="wide")
    st.title(APP_TITLE)
    st.caption(
        "Aprendizaje práctico: decisiones repetibles > teoría. "
        "Este módulo está diseñado para tu poco tiempo: 2–10 min/día."
    )


def ui_decision_card() -> None:
    st.subheader("🧾 Decision Card (2 minutos)")
    c1, c2, c3 = st.columns(3)

    with c1:
        symbol = st.selectbox("Activo", ["BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD", "BNB-USD"], index=0)
        price = st.number_input("Precio actual", min_value=0.0, value=87869.14, step=10.0, format="%.2f")
        horizon = st.selectbox("Horizonte (días)", [7, 14, 30, 60], index=0)

    with c2:
        st.markdown("**Zonas (acción por precio)**")
        buy_low = st.number_input("BUY low", min_value=0.0, value=80659.81, step=10.0, format="%.2f")
        buy_high = st.number_input("BUY high", min_value=0.0, value=84436.31, step=10.0, format="%.2f")
        sell_low = st.number_input("SELL low", min_value=0.0, value=92159.96, step=10.0, format="%.2f")
        sell_high = st.number_input("SELL high", min_value=0.0, value=95712.36, step=10.0, format="%.2f")

    with c3:
        st.markdown("**Monte Carlo (copiar del panel)**")
        p_up_5 = st.slider("P(subir +5%)", 0.0, 1.0, 0.21, 0.01)
        p_down_5 = st.slider("P(bajar -5%)", 0.0, 1.0, 0.40, 0.01)
        p_reach_r1 = st.slider("P(alcanza R1)", 0.0, 1.0, 0.15, 0.01)
        median_return = st.slider("Mediana retorno", -0.50, 0.50, -0.029, 0.001)

    st.divider()

    st.markdown("### Indicadores mínimos (opcional, para confirmar)")
    d1, d2, d3 = st.columns(3)
    with d1:
        ema20 = st.number_input("EMA 20", min_value=0.0, value=0.0, step=10.0, format="%.2f",
                                help="Si no la sabes, déjala en 0 para ignorarla.")
    with d2:
        ema50 = st.number_input("EMA 50", min_value=0.0, value=0.0, step=10.0, format="%.2f",
                                help="Si no la sabes, déjala en 0 para ignorarla.")
    with d3:
        rsi = st.number_input("RSI (0-100)", min_value=0.0, max_value=100.0, value=0.0, step=1.0,
                              help="Si no lo sabes, déjalo en 0 para ignorarlo.")

    ind = Indicators(
        ema20=None if ema20 == 0 else float(ema20),
        ema50=None if ema50 == 0 else float(ema50),
        rsi=None if rsi == 0 else float(rsi),
    )
    zones = Zones(buy_low=float(min(buy_low, buy_high)), buy_high=float(max(buy_low, buy_high)),
                  sell_low=float(min(sell_low, sell_high)), sell_high=float(max(sell_low, sell_high)))
    mc = MonteCarloPanel(
        horizon_days=int(horizon),
        p_up_5=clamp01(float(p_up_5)),
        p_down_5=clamp01(float(p_down_5)),
        p_reach_r1=clamp01(float(p_reach_r1)),
        median_return=float(median_return),
    )

    decision = decision_engine(price=float(price), zones=zones, mc=mc, ind=ind)

    # Big status
    status_color = {"GO": "🟢", "WAIT": "🟡", "NO-TRADE": "🔴"}.get(decision.status, "⚪")
    st.markdown(f"## {status_color} {decision.status}")

    k1, k2 = st.columns([2, 1])
    with k1:
        st.markdown(f"**Por qué:** {decision.rationale}")
        st.markdown(f"**Siguiente acción:** {decision.next_action}")
    with k2:
        st.markdown("**Zona actual:**")
        st.code(zones.classify_price(float(price)))
        if ind.ema20 and ind.ema50:
            st.markdown("**Régimen EMA:**")
            st.code(ind.ema_alignment(float(price)) or "N/A")

    st.divider()

    # Checklist
    st.markdown("### Checklist (aprendizaje por repetición)")
    cols = st.columns(4)
    items = list(decision.checklist.items())
    for i, (k, v) in enumerate(items):
        with cols[i % 4]:
            st.checkbox(k.replace("_", " "), value=bool(v), disabled=True)

    # Journal quick log
    st.markdown("### Micro-journal (1 minuto)")
    with st.expander("Guardar una entrada en el journal"):
        colj1, colj2, colj3 = st.columns(3)
        with colj1:
            did_trade = st.selectbox("¿Hiciste trade?", ["No", "Sí"], index=0)
            followed_plan = st.selectbox("¿Seguiste el plan?", ["N/A", "Sí", "No"], index=0)
        with colj2:
            entry_price = st.number_input("Entry (si aplica)", min_value=0.0, value=0.0, step=10.0, format="%.2f")
            stop_price = st.number_input("Stop (si aplica)", min_value=0.0, value=0.0, step=10.0, format="%.2f")
        with colj3:
            tp1 = st.number_input("TP1 (si aplica)", min_value=0.0, value=0.0, step=10.0, format="%.2f")
            outcome = st.selectbox("Resultado", ["N/A", "Win", "Loss", "BE"], index=0)

        note = st.text_area("Nota (máx 1 línea):", placeholder="Ej.: esperé BUY ZONE, entré tras recuperar EMA20, TP1 en zona neutra.")

        if st.button("Guardar en journal"):
            entry = {
                "ts": datetime.now(timezone.utc).isoformat(),
                "symbol": symbol,
                "horizon_days": horizon,
                "price": float(price),
                "zones": asdict(zones),
                "mc": asdict(mc),
                "indicators": {
                    "ema20": ind.ema20,
                    "ema50": ind.ema50,
                    "rsi": ind.rsi,
                },
                "decision": decision.status,
                "did_trade": did_trade == "Sí",
                "followed_plan": followed_plan,
                "entry_price": float(entry_price) if entry_price else None,
                "stop_price": float(stop_price) if stop_price else None,
                "tp1": float(tp1) if tp1 else None,
                "outcome": outcome,
                "note": note.strip()[:300],
            }
            append_journal(entry)
            st.success("Guardado.")


def ui_parameter_guide() -> None:
    st.subheader("🧪 Indicador Lab (pocos indicadores, parámetros con criterio)")
    st.markdown(
        "Objetivo: que sepas **qué indicador usar** y **qué parámetros** tienen sentido para **swing**. "
        "Aquí no hay recetas mágicas: solo decisiones funcionales."
    )

    st.markdown("## 1) EMAs — para *contexto* y *timing* (no para adivinar)")
    st.markdown(
        "- **EMA 50**: contexto (¿tendencia razonable?)\n"
        "- **EMA 20**: timing (¿pullback y recuperación?)\n"
        "Regla de oro: **no cambies parámetros** hasta haber hecho 20 decisiones con los mismos."
    )

    col1, col2 = st.columns(2)
    with col1:
        tf = st.selectbox("Tu temporalidad principal", ["1D (swing)", "4H (swing)", "1H (timing)"], index=1)
        style = st.selectbox("Tu estilo", ["Swing conservador", "Swing activo"], index=0)
    with col2:
        st.markdown("**Recomendación práctica (por defecto):**")
        st.code("EMA 20 + EMA 50\nRSI 14")
        st.caption("Hasta dominar esto, no añadas más.")

    st.markdown("### ¿Cuándo tendría sentido ajustar EMA 20?")
    st.markdown(
        "- Si ves demasiadas falsas señales (mucho ruido): sube a **EMA 21–25**.\n"
        "- Si quieres timing más rápido (más entradas, más ruido): baja a **EMA 15–18**.\n"
        "Pero: **solo ajusta una vez cada 2 semanas** y documenta el cambio."
    )

    st.markdown("## 2) RSI — para *fuerza*, no para 'sobrecompra/sobreventa'")
    st.markdown(
        "- Uso mínimo (para aprender):\n"
        "  - **RSI ≥ 50**: fuerza suficiente para long\n"
        "  - **RSI 45–50**: posible recuperación (a confirmar)\n"
        "  - **RSI < 45**: debilidad (mejor esperar)\n"
        "- Parámetro por defecto: **RSI 14**"
    )

    st.markdown("### ¿Cuándo ajustar RSI?")
    st.markdown(
        "- Si tu RSI se mueve demasiado con ruido: prueba **RSI 21** (más lento).\n"
        "- Si llega tarde y pierdes timing: prueba **RSI 10–12** (más rápido).\n"
        "Mantén el resto constante."
    )

    st.info(
        "Atajo mental: **más periodo = más lento y más estable**. "
        "**menos periodo = más rápido y más ruidoso**."
    )

    st.markdown("## 3) Regla anti-caos (la más importante)")
    st.markdown(
        "Cada indicador debe tener **una función única**:\n"
        "- Contexto: EMA50\n"
        "- Timing: EMA20\n"
        "- Confirmación: RSI\n\n"
        "Si un indicador está respondiendo a dos preguntas, te confunde."
    )


def ui_micro_plan() -> None:
    st.subheader("📅 Plan ultra-práctico (10 min/día)")
    st.markdown(
        "Sin teoría. Solo repetición.\n\n"
        "**Diario (10 min):**\n"
        "1) Abre el gráfico (BTC o el activo que uses)\n"
        "2) Copia 4 números del panel (p_up_5, p_down_5, mediana, R1)\n"
        "3) Marca BUY ZONE y SELL ZONE\n"
        "4) Rellena el Decision Card y acepta la decisión (GO/WAIT/NO-TRADE)\n"
        "5) Si operas: stop/TP definidos ANTES\n"
        "6) Guarda journal (1 minuto)\n\n"
        "**Semanal (20 min):**\n"
        "- Revisa el journal: ¿respetaste zonas? ¿te adelantaste? ¿rompiste el plan?\n"
        "- NO cambies parámetros si el problema fue disciplina."
    )


def ui_journal_view() -> None:
    st.subheader("📓 Journal (aprendes aquí, no en vídeos)")
    entries = read_journal(limit=300)
    if not entries:
        st.warning("Aún no hay entradas. Guarda 5–10 y vuelve aquí.")
        return

    st.caption(f"Mostrando {len(entries)} últimas entradas (archivo: {JOURNAL_PATH.name})")
    # Simple stats
    trades = [e for e in entries if e.get("did_trade")]
    wins = [e for e in trades if e.get("outcome") == "Win"]
    losses = [e for e in trades if e.get("outcome") == "Loss"]
    be = [e for e in trades if e.get("outcome") == "BE"]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Trades", len(trades))
    c2.metric("Wins", len(wins))
    c3.metric("Losses", len(losses))
    c4.metric("BE", len(be))

    st.divider()
    st.markdown("### Últimas entradas")
    for e in reversed(entries[-20:]):
        ts = e.get("ts", "")
        sym = e.get("symbol", "")
        dec = e.get("decision", "")
        note = e.get("note", "")
        st.markdown(f"**{sym}** · {dec} · {ts}")
        if note:
            st.caption(note)
        st.write(e.get("zones", {}))
        st.write({
            "mc": e.get("mc", {}),
            "indicators": e.get("indicators", {}),
            "trade": {
                "did_trade": e.get("did_trade"),
                "followed_plan": e.get("followed_plan"),
                "entry": e.get("entry_price"),
                "stop": e.get("stop_price"),
                "tp1": e.get("tp1"),
                "outcome": e.get("outcome"),
            }
        })
        st.divider()


def render_app() -> None:
    render_header()

    tab1, tab2, tab3, tab4 = st.tabs([
        "Decision Card",
        "Indicador Lab",
        "Plan 10 min/día",
        "Journal",
    ])

    with tab1:
        ui_decision_card()
    with tab2:
        ui_parameter_guide()
    with tab3:
        ui_micro_plan()
    with tab4:
        ui_journal_view()


if __name__ == "__main__":
    render_app()
