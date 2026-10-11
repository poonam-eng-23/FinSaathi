
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Banking - FinSaathi",
    page_icon="🏦",
    layout="wide"
)

# Restore the language when opening this page directly
if "language" not in st.session_state:
    saved_language = st.query_params.get("language", "English")
    if saved_language not in LANGUAGES:
        saved_language = "English"
    st.session_state["language"] = saved_language

st.title("🏦 " + tr("Banking Basics"))
st.write(tr("Learn how to use banking services safely."))

st.markdown("---")

st.subheader(tr("1. What is a Bank Account?"))
st.write(tr(
    "A bank account helps you keep your money safe, receive money, "
    "save money, and make payments."
))

st.subheader(tr("2. What is an ATM?"))
st.write(tr(
    "An ATM allows you to withdraw cash and perform some banking "
    "activities using your ATM card and PIN."
))

st.warning(tr("Never share your ATM PIN, password, or OTP with anyone."))

st.subheader(tr("3. Types of Bank Accounts"))
st.markdown("\n".join([
    "- **" + tr("Savings Account") + ":** " + tr("For saving money and earning interest."),
    "- **" + tr("Current Account") + ":** " + tr("Commonly used by businesses."),
    "- **" + tr("Fixed Deposit (FD)") + ":** " + tr("Money deposited for a fixed period."),
    "- **" + tr("Recurring Deposit (RD)") + ":** " + tr("Money saved regularly over time.")
]))

st.subheader(tr("4. Safe Banking Tips"))
st.markdown("\n".join([
    "- " + tr("Keep your ATM card and PIN safe."),
    "- " + tr("Never share OTPs or passwords."),
    "- " + tr("Use official banking apps and websites."),
    "- " + tr("Contact your bank immediately if you notice suspicious activity.")
]))

st.markdown("---")
st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
