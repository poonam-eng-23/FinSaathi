import streamlit as st

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💰",
    layout="centered"
)

st.title("💰 FinSaathi")
st.subheader("Learn Finance. Stay Safe.")

st.write(
    "A simple financial literacy app for everyone."
)

st.divider()

st.header("🌐 Choose Your Language")

language = st.selectbox(
    "Select language",
    [
        "English",
        "ಕನ್ನಡ (Kannada)",
        "हिन्दी (Hindi)",
        "मराठी (Marathi)"
    ]
)

st.success(f"Selected language: {language}")

st.divider()

st.header("📚 Learn & Explore")

st.write("Choose a module to learn:")

if st.button("🏦 Banking", use_container_width=True):
    st.switch_page("pages/1_Banking.py")

if st.button("💰 Savings", use_container_width=True):
    st.switch_page("pages/Savings.py")

if st.button("📱 UPI & Payments", use_container_width=True):
    st.switch_page("pages/UPI.py")

if st.button("🛡️ Fraud Safety", use_container_width=True):
    st.switch_page("pages/Fraud_safety.py")

if st.button("📊 Budget", use_container_width=True):
    st.switch_page("pages/Budget.py")

if st.button("🤖 AI Assistant", use_container_width=True):
    st.switch_page("pages/AI_Assistant.py")

if st.button("📝 Financial Quiz", use_container_width=True):
    st.switch_page("pages/Quiz.py")

st.divider()

st.header("🚨 Today's Safety Tip")

st.warning(
    "Never share your OTP, UPI PIN, ATM PIN or password with anyone."
)

st.divider()

st.info(
    "💡 FinSaathi helps you learn banking, savings, "
    "digital payments, budgeting and fraud protection "
    "in simple language."
)

st.caption("FinSaathi – Learn Finance. Stay Safe. 💰")