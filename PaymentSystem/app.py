import streamlit as st
from payment_methods import Mpesa, Card, PayPal
from utils import validate_amount, SUPPORTED_CURRENCIES
from checkout import checkout
from PIL import Image
logo=Image.open("ZachTechs.jpg")
st.image(logo,width=150)

st.set_page_config(page_title="Mini Payment System", page_icon="💳")

st.title("💳 Mini Payment System")


# Payment method selection
method = st.selectbox("Select Payment Method", ["M-Pesa", "Card", "PayPal"])

# Currency selection
currency = st.selectbox("Select Currency", list(SUPPORTED_CURRENCIES.keys()))

# Amount input
amount_input = st.text_input("Enter amount")

if st.button("Process Payment"):
    amount = validate_amount(amount_input)

    if amount is None:
        st.error("❌ Invalid amount. Enter a positive number.")
    else:
        # Create payment method object
        if method == "M-Pesa":
            pm = Mpesa()
        elif method == "Card":
            pm = Card()
        else:
            pm = PayPal()

        message, receipt = checkout(pm, amount, currency)

        st.success(message)
        st.download_button(
            label="Download Receipt PDF",
            data=open(receipt, "rb").read(),
            file_name=receipt,
            mime="application/pdf"
        )

st.markdown("---")
st.caption("© Payment App™ | Developed in Python with ❤️ and Streamlit")
st.caption("@ Zach Techs 2025")