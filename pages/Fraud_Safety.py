```python
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Fraud Safety - FinSaathi",
    page_icon="🛡️",
    layout="wide"
)

# Language selector
st.sidebar.title("🌐 " + tr("Language Settings"))

current_language = st.session_state.get("language", "English")
if current_language not in LANGUAGES:
    current_language = "English"

selected_language = st.sidebar.selectbox(
    "Choose your language",
    LANGUAGES,
    index=LANGUAGES.index(current_language),
    key="fraud_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

# Fraud safety page
st.title("🛡️ " + tr("Fraud Safety"))
st.write(tr("Learn to identify scams and protect your money."))

st.markdown("---")

st.subheader("⚠️ " + tr("Common Financial Scams"))

scams = [
    (
        "Fake bank calls",
        "Scammers pretend to be bank employees and ask for your PIN or OTP."
    ),
    (
        "Fake payment links",
        "Scammers send suspicious links to steal personal or banking information."
    ),
    (
        "Prize and lottery scams",
        "Scammers claim you won a prize and ask you to pay a fee."
    ),
    (
        "Fake customer care",
        "Scammers publish fake customer-care numbers to trick people."
    ),
    (
        "UPI collect requests",
        "Unknown payment requests may trick you into authorising a payment."
    )
]

for title, description in scams:
    st.subheader(tr(title))
    st.write(tr(description))

st.warning(
    "🔐 " + tr(
        "Never share your OTP, UPI PIN, ATM PIN, or banking password."
    )
)

st.markdown("---")

st.subheader("🔍 " + tr("Check a Suspicious Message"))
st.write(
    tr(
        "Paste a suspicious SMS or message below. "
        "This basic checker looks for warning signs; it cannot guarantee "
        "whether a message is genuine."
    )
)

message = st.text_area(
    tr("Paste the message here"),
    height=150,
    placeholder=tr("Paste a suspicious message...")
)

if st.button("Check Message", use_container_width=True):
    if not message.strip():
        st.warning(tr("Please enter a message first."))
    else:
        text = message.lower()

        warning_phrases = [
            "share otp",
            "send otp",
            "upi pin",
            "claim your prize",
            "you have won",
            "urgent",
            "account blocked",
            "click this link",
            "verify your account",
            "send money",
            "bank details",
            "password",
            "lottery",
            "kyc update"
        ]

        found = [
            phrase for phrase in warning_phrases
            if phrase in text
        ]

        if found:
            st.error(
                "⚠️ " + tr(
                    "Warning signs detected. Treat this message carefully."
                )
            )
            st.write(
                tr("Warning signs found") + ": " +
                ", ".join(tr(phrase) for phrase in found)
            )
        else:
            st.info(
                "ℹ️ " + tr(
                    "No listed warning phrases were detected. "
                    "This does not mean the message is safe."
                )
            )

        st.write(
            tr(
                "Do not click suspicious links or share personal information. "
                "Verify the message using the organisation's official contact details."
            )
        )

st.markdown("---")

st.subheader("🚨 " + tr("What to Do If You Suspect Fraud"))

steps = [
    "Stop communicating with the suspected scammer.",
    "Do not share OTPs, PINs, or passwords.",
    "Contact your bank using its official contact details.",
    "In India, report cyber financial fraud by calling 1930 as soon as possible.",
    "Visit the official National Cyber Crime Reporting Portal at cybercrime.gov.in."
]

for step in steps:
    st.markdown("- " + tr(step))

st.markdown("---")
st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
```
