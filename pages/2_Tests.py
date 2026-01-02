import streamlit as st
import psycopg2
import os

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Tests EFA", layout="wide")
st.title("📝 Tests EFA")

# ---------------- DB ----------------
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
            SELECT id, pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta
            FROM preguntas
            WHERE tema = %s
            ORDER BY random()
            LIMIT %s
        """, (tema, limit))
        return cur.fetchall()

# ---------------- STATE ----------------
if "preguntas" not in st.session_state:
    st.session_state.preguntas = []
    st.session_state.respuestas = {}
    st.session_state.finalizado = False
    st.session_state.score = None

# ---------------- UI ----------------
temas = get_temas()
tema = st.selectbox("Selecciona tema", temas)

if st.button("Iniciar test"):
    st.session_state.preguntas = get_preguntas(tema)
    st.session_state.respuestas = {}
    st.session_state.finalizado = False
    st.session_state.score = None

for idx, q in enumerate(st.session_state.preguntas):
    qid, texto, a, b, c, d, correcta = q
    st.markdown(f"**{idx+1}. {texto}**")
    opcion = st.radio(
        "Elige una opción",
        ["A", "B", "C", "D"],
        key=f"q_{qid}",
        index=None
    )
    if opcion:
        st.session_state.respuestas[qid] = opcion

if st.button("Finalizar test") and not st.session_state.finalizado:
    score = 0
    for q in st.session_state.preguntas:
        qid = q[0]
        correcta = q[6]
        if st.session_state.respuestas.get(qid) == correcta:
            score += 1
    st.session_state.score = score
    st.session_state.finalizado = True

if st.session_state.finalizado:
    total = len(st.session_state.preguntas)
    st.success(f"Resultado final: {st.session_state.score} / {total}")
