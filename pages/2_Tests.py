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

temas = get_temas()

if not temas:
    st.warning("No hay preguntas cargadas todavía.")
    st.stop()

tema = st.selectbox("Selecciona tema", temas)

if st.button("Empezar test"):
    preguntas = get_preguntas(tema)

    score = 0
    for i, p in enumerate(preguntas, 1):
        st.markdown(f"### {i}. {p[0]}")
        opciones = {
            "A": p[1],
            "B": p[2],
            "C": p[3],
            "D": p[4],
        }
        respuesta = st.radio(
            "Elige una opción",
            opciones.keys(),
            format_func=lambda x: f"{x}. {opciones[x]}",
            key=f"q_{i}"
        )
        if respuesta == p[5]:
            score += 1

    st.success(f"Resultado: {score} / {len(preguntas)}")
