import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer
from src.utils.connectors.auth import authenticate_user  # Import the authentication function
from src.components.sidebar import render_sidebar_user_block

render_header()
render_sidebar_user_block()

# Title and Log-in Message
st.title("Authentication")
st.write("Use your Woodmackenzie inumber and password to login.")

# Username and Password fields (preserve state across reruns)
username = st.text_input("Username", value=st.session_state.get("username", ""))
password = st.text_input("Password", type="password")

# Button to submit the form
if st.button("Login"):
    response = authenticate_user(username, password)
    
    if response["status_code"] == 200:
        # Store credentials in session_state
        st.session_state.username = username
        st.session_state.password = password
        st.session_state.logged_in = True

        st.success("Login successful")
        st.write(f"Connected to WoodMac's LDI API")

        # Access the 'data' safely
        data = response.get("data", {})
        st.write(data)  # Optionally, display the full response data for debugging purposes

    elif "error" in response:
        st.error(f"Authentication failed: {response['error']}")
    else:
        st.error("Unknown error occurred. Please try again.")

render_footer()
