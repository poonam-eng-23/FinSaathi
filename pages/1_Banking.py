
import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi - Banking",
    page_icon="🏦",
    layout="wide"
)

if "language" not in st.session_state:
    st.session_state["language"] = "English"

if "language_picker" not in st.session_state:
    st.session_state["language_picker"] = st.session_state["language"]


def t(text):
    return tr(text)


def update_language():
    st.session_state["language"] = st.session_state["language_picker"]


st.sidebar.title("💙 FinSaathi")

st.sidebar.selectbox(
    t("Choose your language"),
    LANGUAGES,
    key="language_picker",
    on_change=update_language
)

# Accessibility settings
apply_accessibility()

# Banking page
st.title("🏦 " + t("Banking Basics"))

st.write(
    t("Learn how bank accounts, ATMs and safe banking work.")
)

st.info(
    t("Never share your ATM PIN, UPI PIN, password or OTP with anyone.")
)

st.divider()

# Bank accounts
st.header("💳 " + t("Bank Accounts"))

st.write(
    t("A bank account helps you keep your money safe, receive money "
      "and make payments.")
)

with st.expander("📘 " + t("Types of Bank Accounts")):
    st.markdown(
        "- **Savings Account:** For saving money and earning interest.\n"
        "- **Current Account:** Mainly used by businesses.\n"
        "- **Student Account:** An account designed for eligible students.\n"
        "- **Fixed Deposit:** Money kept in a deposit for a chosen period."
    )

with st.expander("📝 " + t("How to Open a Bank Account")):
    st.markdown(
        "1. Choose a bank.\n"
        "2. Ask the bank about account eligibility and documents.\n"
        "3. Complete the application form.\n"
        "4. Submit the required identity and address documents.\n"
        "5. Keep your account details secure."
    )

st.divider()

# ATM information
st.header("🏧 " + t("ATM Safety"))

st.write(
    t("An ATM lets you withdraw cash and perform certain banking tasks.")
)

st.markdown(
    "- Keep your PIN private.\n"
    "- Cover the keypad while entering your PIN.\n"
    "- Do not accept help from strangers with your card or PIN.\n"
    "- Take your card and cash before leaving.\n"
    "- Contact your bank promptly if your card is lost."
)

st.divider()

# Safe banking
st.header("🔐 " + t("Safe Banking Rules"))

st.markdown(
    "- Never tell anyone your OTP, PIN or password.\n"
    "- Do not click unknown banking links in SMS or messages.\n"
    "- Use official bank websites and applications.\n"
    "- Check transaction messages and account statements.\n"
    "- Contact your bank through its official contact details if "
    "you notice a suspicious transaction."
)

st.warning(
    "🚨 If you suspect financial cyber fraud in India, contact "
    "the national cybercrime helpline at 1930 promptly."
)

st.divider()

# Knowledge check
st.header("🧠 " + t("Quick Knowledge Check"))

question = st.radio(
    t("Should you share your OTP with a person claiming to be a bank employee?"),
    [
        t("Yes, if they ask politely"),
        t("No, never share your OTP"),
        t("Only over a phone call")
    ],
    key="banking_quiz"
)

if st.button(t("Check Answer"), key="banking_check"):
    if question == t("No, never share your OTP"):
        st.success(t("Correct! Keep your OTP private."))
    else:
        st.error(t("Incorrect. Never share your OTP with anyone."))

st.divider()

if st.button("🏠 " + t("Home"), use_container_width=True):
    st.switch_page("app.py")

st.caption("💙 FinSaathi — " + t("Learn Finance. Stay Safe."))
