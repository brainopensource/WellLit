import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

render_header()
st.title("Data Selection")
st.write("Choose your data sources and query the data.")
render_footer()
