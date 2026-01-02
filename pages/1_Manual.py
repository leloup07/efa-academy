import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Manual EFA", layout="wide")

st.title("📘 Manual EFA")

MANUALES_DIR = Path("data/manuales")

manuales = sorted(MANUALES_DIR.glob("*.md"))

if not manuales:
    st.warning("No hay manuales disponibles.")
else:
    nombres = {m.stem.replace("_", " ").title(): m for m in manuales}
    seleccion = st.sidebar.radio("Selecciona un tema", list(nombres.keys()))

    contenido = nombres[seleccion].read_text(encoding="utf-8")
    st.markdown(contenido)
