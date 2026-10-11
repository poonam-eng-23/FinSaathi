
import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi - UPI",
    page_icon="📱",
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

# UPI page
st.title("📱 " + t("Learn About UPI"))

st.write(
    t("UPI lets you send and receive money digitally using supported apps.")
)

st.info(
    t("You generally enter your UPI PIN to AUTHORISE a payment. "
      "You do not enter your PIN to receive money.")
)

st.divider()

# UPI basics
st.header("📘 " + t("UPI Basics"))

st.markdown(
    "- UPI stands for Unified Payments Interface.\n"
    "- You can use supported apps linked to your bank account.\n"
    "- A UPI ID can be used to identify an account for payments.\n"
    "- Check the receiver's name and amount before authorising a payment.\n"
    "- Never share your UPI PIN or OTP with anyone."
)

st.divider()

# How to make a payment
st.header("💸 " + t("How to Make a UPI Payment"))

st.markdown(
    "1. Open your trusted UPI application.\n"
    "2. Choose the payment option.\n"
    "3. Enter or scan the intended recipient's UPI ID or QR code.\n"
    "4. Verify the recipient's name and payment amount carefully.\n"
    "5. Enter your UPI PIN only in the trusted app when authorising a payment.\n"
    "6. Check the transaction status and keep the confirmation."
)

st.warning(
    "Never enter your UPI PIN to receive money or to claim a prize."
)

st.divider()

# Practice payment calculator — simulation only
st.header("🧪 " + t("Practice Payment"))

st.caption(
    t("This is a demonstration only. It does not transfer real money "
      "or connect to a bank.")
)

recipient = st.text_input(
    t("Practice recipient name"),
    placeholder="Example: Rani",
    key="upi_practice_recipient"
)

amount = st.number_input(
    t("Practice amount (₹)"),
    min_value=1,
    max_value=100000,
    value=100,
    step=10,
    key="upi_practice_amount"
)

if st.button(t("Preview Practice Payment"), use_container_width=True):
    if recipient.strip():
        st.success(
            f"{t('Practice payment preview')}\n\n"
            f"{t('Recipient')}: {recipient}\n\n"
            f"{t('Amount')}: ₹{amount:,.2f}"
        )
        st.info(
            t("Simulation complete. No money was sent.")
        )
    else:
        st.warning(t("Please enter a recipient name."))

st.divider()

# Scam awareness
st.header("🚨 " + t("Recognise UPI Scams"))

st.markdown(
    "- Do not scan unknown QR codes to receive money.\n"
    "- Do not approve unexpected collect requests.\n"
    "- Never share your PIN, OTP or screen with strangers.\n"
    "- Avoid remote-access apps suggested by unknown callers.\n"
    "- If a payment seems suspicious, stop and verify independently."
)

st.divider()

# UPI quiz
st.header("🧠 " + t("UPI Safety Quiz"))

answer = st.radio(
    t("Someone says you must enter your UPI PIN to receive money. What should you do?"),
    [
        t("Enter the PIN immediately"),
        t("Refuse and verify the request"),
        t("Share the PIN with the caller")
    ],
    key="upi_safety_quiz"
)

if st.button(t("Check Answer"), key="upi_check_answer"):
    if answer == t("Refuse and verify the request"):
        st.success(
            t("Correct! You do not need to enter your UPI PIN to receive money.")
        )
    else:
        st.error(
            t("Incorrect. Never enter your PIN to receive money.")
        )

st.divider()

if st.button("🏠 " + t("Home"), use_container_width=True):
    st.switch_page("app.py")

st.caption("💙 FinSaathi — " + t("Learn Finance. Stay Safe."))
