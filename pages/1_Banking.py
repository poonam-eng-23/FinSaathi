import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi - Banking",
    page_icon="🏦",
    layout="wide"
)

# Use the same language setting as app.py
if "language" not in st.session_state:
    st.session_state["language"] = "English"

if "language_picker" not in st.session_state:
    st.session_state["language_picker"] = st.session_state["language"]


def t(text):
    return tr(text)


def update_language():
    st.session_state["language"] = st.session_state["language_picker"]


# Sidebar
st.sidebar.title("💙 FinSaathi")

st.sidebar.selectbox(
    t("Choose your language"),
    LANGUAGES,
    key="language_picker",
    on_change=update_language
)

# Accessibility: Larger Text, High Contrast, Read Aloud, Voice Input
apply_accessibility()

# Banking page
st.title("🏦 " + t("Basic Banking"))
st.write(t("Learn the basics of banking."))

st.divider()

st.subheader(t("What is a bank account?"))
st.write(
    t("A bank account helps you deposit, save and withdraw money safely.")
)

st.subheader(t("Savings Account"))
st.write(
    t("A savings account lets you keep money in a bank and may earn interest.")
)

st.subheader(t("ATM"))
st.write(
    t("An ATM allows you to withdraw cash and perform certain banking services.")
)

st.subheader(t("Passbook"))
st.write(
    t("A passbook records deposits, withdrawals and your account balance.")
)

st.divider()

st.subheader(t("Banking Safety Tips"))
st.warning(t("Never share your ATM PIN, OTP or password."))
st.info(t("Use official bank websites and apps."))
st.info(t("Report unknown transactions to your bank immediately."))

st.divider()

st.caption(t("FinSaathi — Learn Finance. Stay Safe. 💙"))

if st.button(t("Home")):
    st.switch_page("app.py")
