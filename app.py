
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💰",
    layout="wide"
)

# Language selection
st.sidebar.title("🌐 Language")

language_options = list(LANGUAGES.keys())

selected_language = st.sidebar.selectbox(
    "Choose your language",
    language_options,
    key="selected_language"
)

# Store selected language
st.session_state["language"] = selected_language

# Home page
st.title("💰 FinSaathi")
st.subheader("Learn Finance. Stay Safe.")

st.write(
    "Welcome to FinSaathi! Learn about banking, savings, "
    "UPI payments, budgeting, and financial fraud prevention."
)

st.info(
    "💡 Learn how to manage money safely and make better "
    "financial decisions."
)

st.markdown("---")
st.subheader("📚 Explore FinSaathi")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏦 Banking")
    st.write("Learn about bank accounts, ATMs, and banking safety.")
    if st.button("Open Banking", use_container_width=True):
        st.switch_page("pages/1_Banking.py")

    st.markdown("### 💰 Savings")
    st.write("Learn simple ways to save money.")
    if st.button("Open Savings", use_container_width=True):
        st.switch_page("pages/Savings.py")

    st.markdown("### 📱 UPI Payments")
    st.write("Understand digital payments and safe UPI practices.")
    if st.button("Open UPI", use_container_width=True):
        st.switch_page("pages/UPI.py")

    st.markdown("### 🛡️ Fraud Safety")
    st.write("Learn how to identify scams and protect your money.")
    if st.button("Open Fraud Safety", use_container_width=True):
        st.switch_page("pages/Fraud_Safety.py")

with col2:
    st.markdown("### 🤖 AI Assistant")
    st.write("Explore financial questions and get helpful guidance.")
    if st.button("Open AI Assistant", use_container_width=True):
        st.switch_page("pages/AI_Assistant.py")

    st.markdown("### 📊 Budget Planner")
    st.write("Plan your monthly spending and savings.")
    if st.button("Open Budget", use_container_width=True):
        st.switch_page("pages/Budget.py")

    st.markdown("### 📝 Financial Quiz")
    st.write("Test your financial knowledge.")
    if st.button("Open Quiz", use_container_width=True):
        st.switch_page("pages/Quiz.py")

st.markdown("---")
st.caption("FinSaathi — Learn Finance. Stay Safe.")
