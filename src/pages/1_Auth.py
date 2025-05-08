import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer
from src.utils.connectors.auth import authenticate_user  # Import the authentication function

render_header()

# Title and Log-in Message
st.title("Authentication")
st.write("Use your Woodmackenzie inumber and password to login.")

# Username and Password fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Button to submit the form
if st.button("Login"):
    # Verification layer
    response = authenticate_user(username, password)
    
    # Check the response status_code
    if response["status_code"] == 200:  # Checks if authentication was successful
        st.success("Login successful!")
        st.write("Welcome to the app!")
        
        # Print the data returned by the API
        st.write("Connected to WoodMac's API, ANP Source")
        st.write(f"@odata.context: {response['data'].get('@odata.context', 'N/A')}")
        
    elif "error" in response:  # In case of authentication failure
        st.error(f"Authentication failed: {response['error']}")
    else:
        st.error("Unknown error occurred. Please try again.")

render_footer()
