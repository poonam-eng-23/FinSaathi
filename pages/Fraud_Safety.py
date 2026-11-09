```python
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Fraud Safety | FinSaathi",
    page_icon="🛡️",
    layout="wide"
)

# Shared language selection
if "language" not in st.session_state:
    st.session_state["language"] = st.query_params.get("language", "English")

if st.session_state["language"] not in LANGUAGES:
    st.session_state["language"] = "English"

st.sidebar.title(tr("🌐 Language / ಭಾಷೆ"))

st.sidebar.selectbox(
    tr("Choose your language"),
    LANGUAGES,
    key="language"
)

st.query_params["language"] = st.session_state["language"]

# Main heading
st.title(tr("🛡️ Fraud Safety Centre"))
st.subheader(tr("Learn to recognise scams, protect your money, and report fraud."))

st.info(
    tr("Golden rule: Never share your OTP, UPI PIN, ATM PIN, password, or card security code with anyone.")
)

st.markdown("---")

# 1. Common fraud types
st.header(tr("1. Common Financial Scams"))

fraud_types = [
    (
        "📞 Fake bank calls",
        "Someone pretends to be a bank employee and asks for your OTP, PIN, or account details.",
        "End the call and contact your bank using its official number."
    ),
    (
        "🔗 Fake SMS and links",
        "A message claims your bank account, KYC, or SIM will be blocked unless you click a link.",
        "Do not click the link. Open the official bank app or website yourself."
    ),
    (
        "📷 QR code and UPI scams",
        "A stranger asks you to scan a QR code or enter your UPI PIN to receive money.",
        "You generally do not need your UPI PIN to receive money. Verify every payment request."
    ),
    (
        "🎁 Prize and lottery scams",
        "You are told that you won a prize but must pay a fee or tax first.",
        "Do not pay unexpected fees to claim a prize. Verify the organisation independently."
    ),
    (
        "💼 Fake investment offers",
        "Someone promises guaranteed high returns or pressures you to invest immediately.",
        "Be cautious of guaranteed returns. Verify the provider and understand the risks."
    ),
    (
        "🪪 Impersonation scams",
        "A person pretends to be a relative, official, police officer, or customer-care
