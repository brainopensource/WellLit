import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

render_header()
st.title("Data Visualization")
st.write("Graphical representation of the data.")
render_footer()
