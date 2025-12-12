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

# ------------------------
# Authentication / Roles
# ------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None

def login_box():
    st.sidebar.header("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        user = USERS.get(username)
        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = user["role"]
            st.sidebar.success(f"Logged in as {username} ({st.session_state.role})")
        else:
            st.sidebar.error("Invalid credentials")

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None
    st.rerun()

# Show login if not logged in
if not st.session_state.logged_in:
    st.title("🛡️ Admin Dashboard — Please log in")
    login_box()
    st.sidebar.markdown("\n---\nDefault credentials: admin/admin123 or viewer/viewer123")
    st.stop()

# ------------------------
# Top bar
# ------------------------
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image("https://static.streamlit.io/images/brand/streamlit-mark-color.png", width=60)
with col2:
    st.markdown(f"# Admin Dashboard")
    st.markdown(f"**User:** {st.session_state.username}  •  **Role:** {st.session_state.role}")
with col3:
    if st.button("Logout"):
        logout()

# Theme toggle
with st.sidebar:
    st.markdown("---")
    theme_choice = st.radio("Theme", ("light", "dark"), index=0 if st.session_state.theme == "light" else 1)
    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        apply_theme()

# ------------------------
# Load & Prepare Data
# ------------------------
@st.cache_data(ttl=30)
def load_data():
    df = fetch_transactions()
    if df.empty:
        return df
    # ensure Timestamp is datetime
    if not pd.api.types.is_datetime64_any_dtype(df["Time"]):
        df["Time"] = pd.to_datetime(df["Time"])
    return df

try:
    df = load_data()
except Exception as e:
    st.error("Error loading transactions: " + str(e))
    st.stop()

if df.empty:
    st.warning("No transactions found yet. Make a payment from the user app first.")
    st.stop()

# ------------------------
# Sidebar Filters
# ------------------------
st.sidebar.header("📌 Filters")

# Date range
min_date = df["Time"].min().date()
max_date = df["Time"].max().date()
start_date = st.sidebar.date_input("Start date", min_value=min_date, value=min_date)
end_date = st.sidebar.date_input("End date", min_value=min_date, value=max_date)

# Methods & currencies
methods = st.sidebar.multiselect("Payment Method", options=sorted(df["Method"].unique()), default=sorted(df["Method"].unique()))
currencies = st.sidebar.multiselect("Currency", options=sorted(df["Currency"].unique()), default=sorted(df["Currency"].unique()))

# Status filter (if present)
if "Status" in df.columns:
    statuses = st.sidebar.multiselect("Status", options=sorted(df["Status"].unique()), default=sorted(df["Status"].unique()))
else:
    statuses = None

# Quick search
search = st.sidebar.text_input("Search (ID, Method)")

# Apply filters
filtered = df[
    (df["Time"].dt.date >= start_date) &
    (df["Time"].dt.date <= end_date) &
    (df["Method"].isin(methods)) &
    (df["Currency"].isin(currencies))
]
if statuses is not None:
    filtered = filtered[filtered["Status"].isin(statuses)]

if search:
    mask = filtered["Method"].str.contains(search, case=False, na=False) | filtered["ID"].astype(str).str.contains(search)
    filtered = filtered[mask]

# ------------------------
# Summary Metrics
# ------------------------
st.header("📊 Summary")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Transactions", len(filtered))
with col2:
    st.metric("Total Revenue", f"{filtered['Amount'].sum():,.2f} {filtered['Currency'].mode()[0]}")
with col3:
    st.metric("Unique Payment Methods", filtered["Method"].nunique())
with col4:
    st.metric("Currencies", filtered["Currency"].nunique())

# ------------------------
# Charts
# ------------------------
st.header("📈 Visualizations")

# Revenue over time (daily)
revenue_ts = filtered.set_index("Time").resample('D')["Amount"].sum().reset_index()
colA, colB = st.columns([3,2])
with colA:
    st.subheader("Revenue (Daily)")
    st.line_chart(revenue_ts.rename(columns={"Time": "index"}).set_index("index")["Amount"])

with colB:
    st.subheader("By Payment Method")
    method_counts = filtered.groupby("Method")["Amount"].sum().sort_values(ascending=False)
    st.bar_chart(method_counts)

st.subheader("Currency Breakdown")
currency_breakdown = filtered.groupby("Currency")["Amount"].sum()
st.write(currency_breakdown)

# ------------------------
# Transaction Table + Download
# ------------------------
st.header("📄 Transactions")

# Allow admin only actions
is_admin = st.session_state.role == "admin"

st.dataframe(filtered.sort_values(by="Time", ascending=False), width="stretch")

# CSV export
csv_buffer = io.StringIO()
filtered.to_csv(csv_buffer, index=False)
csv_bytes = csv_buffer.getvalue().encode()

st.download_button("📥 Download CSV", data=csv_bytes, file_name=f"transactions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", mime="text/csv")

# ------------------------
# Receipt download / view
# ------------------------
st.header("📎 Receipts")
selected_id = st.selectbox("Select Transaction ID to view receipt", options=filtered["ID"].tolist())
rec_row = df[df["ID"] == selected_id]
if not rec_row.empty:
    receipt_path = rec_row.iloc[0]["Receipt"]
    try:
        with open(receipt_path, "rb") as f:
            receipt_bytes = f.read()
        st.download_button("Download Receipt PDF", data=receipt_bytes, file_name=receipt_path.split('/')[-1], mime="application/pdf")
    except FileNotFoundError:
        st.error("Receipt file not found on disk: " + str(receipt_path))
else:
    st.info("Selected transaction not found in current dataset")

# ------------------------
# Admin-only controls
# ------------------------
if is_admin:
    st.header("⚙️ Admin Controls")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Delete All Transactions (danger)"):
            st.warning("Delete functionality is not implemented in UI for safety. Please run a backend script to remove records.")
    with col2:
        if st.button("Refresh Data"):
            st.cache_data.clear()
            st.rerun()

st.markdown("---")
st.caption("Built with ❤️ by ZachTechs")