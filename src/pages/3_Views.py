import streamlit as st
from pyodata import Client
from requests.auth import HTTPBasicAuth
import requests
import pandas as pd
from src.components.header import render_header
from src.components.footer import render_footer

# Page setup
render_header()
st.title("OData API Access")
st.write("Accessing production data using OData authentication.")

render_footer()
