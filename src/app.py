# -*- coding: UTF-8 -*- Requires Python 3.10+

import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

# Define configurações gerais
st.set_page_config(page_title="Oil & Gas Decline Analysis", layout="wide")

def main():
    render_header()
    st.markdown("## Welcome to the Oil & Gas Decline Analysis App.")
    render_footer()

if __name__ == "__main__":
    main()
