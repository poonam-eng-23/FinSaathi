
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💰",
    layout="wide"
)

# Restore the selected language from the URL, if available
if "language" not in st.session_state:
    saved_language = st.query_params.get("language", "English")
    if saved_language not in LANGUAGES:
        saved_language = "English"
    st.session_state["language"] = saved_language

st.sidebar.title("🌐 " + tr("Language Settings"))

selected_language = st.sidebar.selectbox(
    "Choose your language",
    LANGUAGES,
    key="language"
)

# Keep the selected language in the URL when navigating pages
st.query_params["language"] = selected_language

st.title("💰 " + tr("FinSaathi"))
st.subheader(tr("Learn Finance. Stay Safe."))

st.write(
    tr(
        "Welcome to FinSaathi! Learn about banking, savings, "
        "UPI payments, budgeting, and financial fraud prevention."
    )
)

st.info(
    "💡 " + tr(
        "Learn how to manage money safely and make better "
        "financial decisions."
    )
)

st.markdown("---")
st.subheader("📚 " + tr("Explore FinSaathi"))

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏦 " + tr("Banking"))
    st.write(tr("Learn about bank accounts, ATMs, and banking safety."))
    if st.button(tr("Open Banking"), use_container_width=True):
        st.switch_page("pages/1_Banking.py")

    st.markdown("### 💰 " + tr("Savings"))
    st.write(tr("Learn simple ways to save money."))
    if st.button(tr("Open Savings"), use_container_width=True):
        st.switch_page("pages/Savings.py")

    st.markdown("### 📱 " + tr("UPI Payments"))
    st.write(tr("Understand digital payments and safe UPI practices."))
    if st.button(tr("Open UPI"), use_container_width=True):
        st.switch_page("pages/UPI.py")

    st.markdown("### 🛡️ " + tr("Fraud Safety"))
    st.write(tr("Learn how to identify scams and protect your money."))
    if st.button(tr("Open Fraud Safety"), use_container_width=True):
        st.switch_page("pages/Fraud_Safety.py")

with col2:
    st.markdown("### 🤖 " + tr("AI Assistant"))
    st.write(tr("Explore financial questions and helpful guidance."))
    if st.button(tr("Open AI Assistant"), use_container_width=True):
        st.switch_page("pages/AI_Assistant.py")

    st.markdown("### 📊 " + tr("Budget Planner"))
    st.write(tr("Plan your monthly spending and savings."))
    if st.button(tr("Open Budget"), use_container_width=True):
        st.switch_page("pages/Budget.py")

    st.markdown("### 📝 " + tr("Financial Quiz"))
    st.write(tr("Test your financial knowledge."))
    if st.button(tr("Open Quiz"), use_container_width=True):
        st.switch_page("pages/Quiz.py")

st.markdown("---")
st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
