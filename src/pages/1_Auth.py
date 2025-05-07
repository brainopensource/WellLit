import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

render_header()
st.title("Authentication")
st.write("Use your Woodmackenzie inumber and password to login.")
render_footer()
