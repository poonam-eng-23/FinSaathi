
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Banking - FinSaathi",
    page_icon="🏦",
    layout="wide"
)

language_options = list(LANGUAGES.keys())
language = st.session_state.get("language", language_options[0])

st.title("🏦 Banking Basics")
st.write("Learn how to use banking services safely.")

st.markdown("---")

st.subheader("1. What is a Bank Account?")
st.write(
    "A bank account helps you keep your money safe, "
    "receive money, save money, and make payments."
)

st.subheader("2. What is an ATM?")
st.write(
    "An ATM allows you to withdraw cash and perform "
    "some banking activities using your ATM card and PIN."
)

st.warning(
    "Never share your ATM PIN, password, or OTP with anyone."
)

st.subheader("3. Types of Bank Accounts")

st.markdown("""
- **Savings Account:** For saving money and earning interest.
- **Current Account:** Commonly used by businesses.
- **Fixed Deposit (FD):** Money deposited for a fixed period.
- **Recurring Deposit (RD):** Money saved regularly over time.
""")

st.subheader("4. Safe Banking Tips")

st.markdown("""
- Keep your ATM card and PIN safe.
- Never share OTPs or passwords.
- Use official banking apps and websites.
- Contact your bank immediately if you notice suspicious activity.
""")

st.markdown("---")
st.caption("FinSaathi — Learn Finance. Stay Safe.")
