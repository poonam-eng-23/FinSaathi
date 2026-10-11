
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="UPI - FinSaathi",
    page_icon="📱",
    layout="wide"
)

st.title("📱 UPI Payments")
st.write("Learn how to make digital payments safely.")

st.markdown("---")

st.subheader("What is UPI?")
st.write(
    "UPI stands for Unified Payments Interface. "
    "It allows people to send and receive money digitally."
)

st.subheader("How to make a UPI payment")

st.markdown("""
1. Open your official UPI payment app.
2. Choose the person or merchant you want to pay.
3. Enter the amount.
4. Check the recipient's details carefully.
5. Enter your UPI PIN only inside the official payment app to authorize a payment.
6. Check the transaction status.
""")

st.warning(
    "Never share your UPI PIN or OTP with anyone. "
    "You do not need to enter your UPI PIN to receive money."
)

st.subheader("Practice: Identify Safe or Unsafe Actions")

question = st.radio(
    "Someone calls and asks you to share your UPI PIN. What should you do?",
    [
        "Share it because the caller says they are from the bank",
        "Never share it and end the call",
        "Send it by message instead"
    ],
    index=None
)

if st.button("Check Answer"):
    if question == "Never share it and end the call":
        st.success("Correct! Keep your UPI PIN secret.")
    elif question is None:
        st.info("Please select an answer first.")
    else:
        st.error("Incorrect. Never share your UPI PIN.")

st.markdown("---")
st.caption("FinSaathi — Learn Finance. Stay Safe.")
