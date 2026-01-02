import streamlit as st
import psycopg2
import os
from urllib.parse import urlparse
import random

st.set_page_config(page_title="Tests EFA", layout="wide")
st.title("📝 Tests EFA")

@st.cache_resource
def get_connection():
    url = urlparse(os.environ["DATABASE_URL"])
    return psycopg2.connect(
        dbname=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
        sslmode="require"
    )

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT DISTINCT tema FROM preguntas ORDER BY tema")
temas = [r[0] for r in cur.fetchall()]

tema = st.selectbox("📚 Selecciona tema", temas)

if st.button("🎯 Nueva pregunta"):
    cur.execute(
        "SELECT pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion "
        "FROM preguntas WHERE tema=%s ORDER BY RANDOM() LIMIT 1",
        (tema,)
    )
    q = cur.fetchone()
    if q:
        st.session_state.q = q
        st.session_state.respondido = False

if "q" in st.session_state:
    pregunta, a, b, c, d, correcta, explicacion = st.session_state.q
    st.subheader(pregunta)

    opcion = st.radio(
        "Elige una opción:",
# SYNTAX_FIX         ["A
cat > pages/2_Tests.py << 'EOF'
import streamlit as st
import psycopg2
import os
from urllib.parse import urlparse
import random

st.set_page_config(page_title="Tests EFA", layout="wide")
st.title("📝 Tests EFA")

@st.cache_resource
def get_connection():
    url = urlparse(os.environ["DATABASE_URL"])
    return psycopg2.connect(
        dbname=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
        sslmode="require"
    )

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT DISTINCT tema FROM preguntas ORDER BY tema")
temas = [r[0] for r in cur.fetchall()]

tema = st.selectbox("📚 Selecciona tema", temas)

if st.button("🎯 Nueva pregunta"):
    cur.execute(
        "SELECT pregunta, opcion_a, opcion_b, opcion_c, opcion_d, correcta, explicacion "
        "FROM preguntas WHERE tema=%s ORDER BY RANDOM() LIMIT 1",
        (tema,)
    )
    q = cur.fetchone()
    if q:
        st.session_state.q = q
        st.session_state.respondido = False

if "q" in st.session_state:
    pregunta, a, b, c, d, correcta, explicacion = st.session_state.q
    st.subheader(pregunta)

    opcion = st.radio(
        "Elige una opción:",
        ["A", "B", "C", "D"],
        format_func=lambda x: {
            "A": a, "B": b, "C": c, "D": d
        }[x]
    )

    if st.button("✅ Responder"):
        st.session_state.respondido = True
        if opcion == correcta:
            st.success("✔ Correcto")
        else:
            st.error(f"✘ Incorrecto. Correcta: {correcta}")
        st.info(explicacion)

cur.close()
