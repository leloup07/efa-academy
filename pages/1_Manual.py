import streamlit as st
from pathlib import Path

st.title("📘 Manual EFA")

BASE = Path(".")

manuals = sorted([
    p for p in BASE.glob("*.md")
    if not p.name.startswith("tests_")
])

if not manuals:
    st.warning("No se han encontrado manuales.")
else:
    for md in manuals:
        with st.expander(md.name.replace("_", " ").replace(".md", "").title()):
            st.markdown(md.read_text(), unsafe_allow_html=True)
