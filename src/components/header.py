import streamlit as st

def render_header():
    st.markdown(
        "<h1 style='text-align: center; color: #1f77b4;'>Upstream Decline Curve Analyzer</h1>",
        unsafe_allow_html=True
    )
    st.markdown("---")
