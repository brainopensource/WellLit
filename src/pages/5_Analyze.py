import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

render_header()
st.title("Analyze")
st.write("Analyze the results of the model and publish results.")
render_footer()
