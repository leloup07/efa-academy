import streamlit as st
import sqlite3

st.set_page_config(page_title="Tests EFA", layout="wide")
st.title("📝 Tests EFA")

DB_PATH = "data/preguntas.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

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
            WHERE tema = ?
            ORDER BY RANDOM()
            LIMIT ?
        """, (tema, limit))
        return cur.fetchall()

# ---------- STATE ----------
if "test_activo" not in st.session_state:
    st.session_state.test_activo = False
if "preguntas" not in st.session_state:
    st.session_state.preguntas = []
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

temas = get_temas()
tema = st.selectbox("Selecciona tema", temas)

# ---------- START TEST ----------
if st.button("Empezar test") and not st.session_state.test_activo:
    st.session_state.preguntas = get_preguntas(tema)
    st.session_state.respuestas = {}
    st.session_state.test_activo = True

# ---------- TEST LOOP ----------
if st.session_state.test_activo:
    for i, p in enumerate(st.session_state.preguntas):
        st.markdown(f"### {i+1}. {p[0]}")
        opciones = {
            "A": p[1],
            "B": p[2],
            "C": p[3],
            "D": p[4],
        }
        st.session_state.respuestas[i] = st.radio(
            "Elige una opción",
            opciones.keys(),
            format_func=lambda x: f"{x}. {opciones[x]}",
            key=f"q_{i}"
        )

    if st.button("Finalizar test"):
        score = 0
        for i, p in enumerate(st.session_state.preguntas):
            if st.session_state.respuestas.get(i) == p[5]:
                score += 1

        st.success(f"Resultado final: {score} / {len(st.session_state.preguntas)}")
        st.session_state.test_activo = False
