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
