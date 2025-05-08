import streamlit as st

def render_sidebar_user_block():
    if st.session_state.get("logged_in"):
        with st.sidebar:
            st.markdown("### User Panel")
            st.write(f"Welcome, **{st.session_state.username}**!")

            if st.button("Logout"):
                for key in ["username", "password", "logged_in"]:
                    st.session_state.pop(key, None)
                st.success("Logged out successfully.")
