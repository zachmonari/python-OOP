import streamlit as st
import pandas as pd
from admin_utils import load_transactions
from admin_auth import admin_login
from queries import fetch_transactions
from PIL import Image


logo=Image.open("ZachTechs.jpg")
st.image(logo, width=150)

st.set_page_config(page_title="Admin Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ Admin Dashboard")

# Check login status
if "admin_logged_in" not in st.session_state or not st.session_state["admin_logged_in"]:
    admin_login()
    st.stop()

# Load transaction data
df = load_transactions()

st.sidebar.header("📌 Filters")

# Filter by method
methods = st.sidebar.multiselect("Payment Method", options=df["Method"].unique(), default=df["Method"].unique())

# Filter by currency
currencies = st.sidebar.multiselect("Currency", options=df["Currency"].unique(), default=df["Currency"].unique())

# Date range filter
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Apply filters
filtered_df = df[
    (df["Method"].isin(methods)) &
    (df["Currency"].isin(currencies)) &
    (df["Timestamp"].dt.date >= start_date) &
    (df["Timestamp"].dt.date <= end_date)
]

st.subheader("📊 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Transactions", len(filtered_df))

with col2:
    st.metric("Total Revenue", f"{filtered_df['Amount'].sum():,.2f}")

with col3:
    st.metric("Payment Methods Used", filtered_df['Method'].nunique())

st.subheader("📄 Transaction Data")

# Search bar
search = st.text_input("Search transaction ID or method")

if search:
    filtered_df = filtered_df[
        filtered_df["Method"].str.contains(search, case=False) |
        filtered_df["ID"].astype(str).str.contains(search)
    ]

# Display table
st.dataframe(filtered_df, width="stretch")

# CSV Download
csv = filtered_df.to_csv(index=False).encode()
st.download_button("📥 Download CSV", csv, "transactions.csv", "text/csv")

# Show receipts
st.subheader("📎 View Receipts")

selected_id = st.selectbox("Select Transaction ID", filtered_df["ID"])

receipt_path = df[df["ID"] == selected_id]["Receipt"].values[0]

if st.button("Open Receipt PDF"):
    with open(receipt_path, "rb") as f:
        st.download_button(
            label="Download Receipt",
            data=f.read(),
            file_name=receipt_path,
            mime="application/pdf"
        )
df = fetch_transactions()
st.dataframe(df)