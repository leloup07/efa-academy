import streamlit as st
try:
import streamlit as st
try:
import streamlit as st
import sqlite3

import streamlit as st
import psycopg2
import os

st.set_page_config(page_title="Tests EFA", layout="wide")
st.title("📝 Tests EFA")
# --- INIT SESSION STATE ---n
if "initialized" not in st.session_state:n
    st.session_state.initialized = Truen
    st.session_state.preguntas = []n
    st.session_state.respuestas = {}n
    st.session_state.finalizado = Falsen
    st.session_state.score = Nonen

# --- INIT SESSION STATE ---
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.preguntas = []
    st.session_state.respuestas = {}
    st.session_state.finalizado = False
    st.session_state.score = None
    st.session_state.temas = None

except Exception as e:
    st.error('❌ ERROR EN Tests.py')
    st.exception(e)

