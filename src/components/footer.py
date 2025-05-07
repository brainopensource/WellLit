import streamlit as st

def render_footer():
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: gray;'>© Upstream Well Decaiment Analysis App 2025 - Lucas Rocha</p>",
        unsafe_allow_html=True
    )
