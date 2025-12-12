import streamlit as st
import pandas as pd
import io
from datetime import datetime
from queries import fetch_transactions

# ------------------------
# Configuration / Defaults
# ------------------------
st.set_page_config(page_title="Admin Dashboard", page_icon="🛡️", layout="wide")

# Simple role-based credentials (change or move to DB for production)
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "viewer": {"password": "viewer123", "role": "viewer"}
}
# ------------------------
# Theme CSS (Light / Dark)
# ------------------------
LIGHT_CSS = """
<style>
    .reportview-container { background: #FFFFFF; }
    .stApp { background: #FFFFFF; color: #000000 }
    .card { background: #F8F9FA; padding: 12px; border-radius: 8px; }
</style>
"""
DARK_CSS = """
<style>
    .reportview-container { background: #0E1117; }
    .stApp { background: #0E1117; color: #E6EDF3 }
    .card { background: #0B1220; padding: 12px; border-radius: 8px; }
    .stButton>button { background-color: #0B1220; }
</style>
"""

# Load theme preference from session state
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Apply CSS
def apply_theme():
    if st.session_state.theme == "dark":
        st.markdown(DARK_CSS, unsafe_allow_html=True)
    else:
        st.markdown(LIGHT_CSS, unsafe_allow_html=True)

apply_theme()