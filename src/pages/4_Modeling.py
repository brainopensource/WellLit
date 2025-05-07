import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

render_header()
st.title("Modeling")
st.write("Modeling the curves and production parameters.")
render_footer()
