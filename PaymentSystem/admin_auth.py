import streamlit as st

# Simple hardcoded login for now (you can upgrade to DB-based later)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def admin_login():
    st.subheader("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state["admin_logged_in"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")
