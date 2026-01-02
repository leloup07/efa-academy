import streamlit as st
try:
import streamlit as st
import sqlite3

st.set_page_config(page_title="Tests EFA", layout="wide")
st.title("📝 Tests EFA")
# --- INIT SESSION STATE ---n
if "initialized" not in st.session_state:n
    st.session_state.initialized = Truen
    st.session_state.preguntas = []n
    st.session_state.respuestas = {}n
    st.session_state.finalizado = Falsen
    st.session_state.score = Nonen
    st.session_state.temas = None

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

# --- LOAD TEMAS SAFELY ---n
if st.session_state.temas is None:n
    st.session_state.temas = get_temas()
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


    if st.button("Finalizar test") and not st.session_state.finalizado:
    st.session_state.finalizado = Truen
        score = 0

        st.divider()
        st.subheader("📊 Corrección del test")

        for i, p in enumerate(st.session_state.preguntas):
            pregunta, a, b, c, d, correcta = p
            user = st.session_state.respuestas.get(i)

            opciones = {
                "A": a,
                "B": b,
                "C": c,
                "D": d,
            }

            st.markdown(f"### {i+1}. {pregunta}")

            if user == correcta:
                letras = ["A","B","C","D"]
                letra = letras[int(correcta)]
                st.success(f"✅ Correcta — {letra}. {opciones[letra]}")
                score += 1
            else:
                st.error(
                    f"❌ Incorrecta\n\n"
                    f"- Tu respuesta: {user}. {opciones.get(user, '')}\n"
                    letras = ["A","B","C","D"]; letra_correcta = letras[int(correcta)]; f"✔ Correcta: {letra_correcta}. {opciones[letra_correcta]}"
                )

        st.divider()
        st.success(f"🎯 Resultado final: {score} / {len(st.session_state.preguntas)}")
        st.session_state.test_activo = False

except Exception as e:
    st.error('❌ ERROR EN Tests.py')
    st.exception(e)

