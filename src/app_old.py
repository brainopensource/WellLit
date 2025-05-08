import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

# Define configurações gerais
st.set_page_config(page_title="Oil & Gas Decline Analysis", layout="wide")

def main():
    # Set the title in the sidebar to "Home"
    st.sidebar.title("Home")  # This will change the sidebar name to "Home"
    
    render_header()
    st.markdown("## Welcome to the Oil & Gas Decline Analysis App.")
    render_footer()

if __name__ == "__main__":
    main()
