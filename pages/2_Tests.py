import streamlit as st
import psycopg2
import os
import random

st.set_page_config(page_title="Tests EFA", layout="wide")
st.title("📝 Tests EFA")

# ---------- DB ----------
def get_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")

def get_temas():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT tema FROM preguntas ORDER BY tema")
        return [r[0] for r in cur.fetchall()]

def get_preguntas(tema, limit=10):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta
            FROM preguntas
            WHERE tema = %s
            ORDER BY random()
            LIMIT %s
        """, (tema, limit))
        return cur.fetchall()

# ---------- SESSION ----------
if "preguntas" not in st.session_state:
    st.session_state.preguntas = []
    st.session_state.respuestas = {}
    st.session_state.finalizado = False
    st.session_state.score = None

# ---------- UI ----------
temas = get_temas()
tema = st.selectbox("Selecciona un tema", temas)

if st.button("▶️ Empezar test"):
    st.session_state.preguntas = get_preguntas(tema)
    st.session_state.respuestas = {}
    st.session_state.finalizado = False
    st.session_state.score = None

# ---------- TEST ----------
for i, p in enumerate(st.session_state.preguntas):
    pregunta, a, b, c, d, correcta = p
    st.subheader(f"{i+1}. {pregunta}")
    opciones = {"A": a, "B": b, "C": c, "D": d}
    resp = st.radio(
        "Elige una opción",
        opciones.keys(),
        key=f"q_{i}",
        format_func=lambda x: f"{x}. {opciones[x]}"
    )
    st.session_state.respuestas[i] = resp

# ---------- RESULT ----------
if st.session_state.preguntas and st.button("✅ Finalizar test"):
    score = 0
    for i, p in enumerate(st.session_state.preguntas):
        if st.session_state.respuestas.get(i) == p[5]:
            score += 1
    st.session_state.score = score
    st.session_state.finalizado = True

if st.session_state.finalizado:
    total = len(st.session_state.preguntas)
    st.success(f"Resultado: {st.session_state.score} / {total}")

    st.divider()

    st.divider()
    st.header("📊 Corrección detallada")

    with st.container():
        for i, p in enumerate(st.session_state.preguntas):
            (
                pregunta,
                a, b, c, d,
                correcta,
                explicacion
            ) = p

            opciones = {"A": a, "B": b, "C": c, "D": d}
            marcada = st.session_state.respuestas.get(i)

            st.markdown(f"**{i+1}. {pregunta}**")

            if marcada == correcta:
                st.success(f"✔ Correcta: {correcta}. {opciones[correcta]}")
            else:
                st.error(
                    f"❌ Tu respuesta: {marcada}. {opciones.get(marcada, '')}\n\n"
                    f"✔ Correcta: {correcta}. {opciones[correcta]}"
                )

            st.info(f"💡 Explicación: {explicacion}")
            st.markdown("---")
