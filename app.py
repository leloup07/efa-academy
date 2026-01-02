from data.db.init_progreso import init_progreso
init_progreso()

import streamlit as st

st.set_page_config(page_title="EFA Academy", layout="wide")

st.title("📘 EFA Academy")
st.success("Streamlit funcionando en Railway 🚀")
