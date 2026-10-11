
import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi - Fraud Safety",
    page_icon="🛡️",
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

# Fraud Safety page
st.title("🛡️ " + t("Fraud Safety Centre"))

st.write(
    t("Learn how to recognise common scams and protect your money.")
)

st.error(
    "Never share your OTP, UPI PIN, ATM PIN or banking password."
)

st.divider()

# Common scams
st.header("🚨 " + t("Common Financial Scams"))

with st.expander("📞 " + t("Fake Bank Calls")):
    st.write(
        t("Scammers may pretend to be bank employees and ask for your "
          "OTP, PIN or account details. End the call and contact your "
          "bank using its official contact information.")
    )

with st.expander("🔗 " + t("Suspicious Links")):
    st.write(
        t("Unexpected messages may contain links to fake websites. "
          "Do not open unknown links or enter banking details on them.")
    )

with st.expander("💸 " + t("UPI Payment Scams")):
    st.write(
        t("Do not approve unexpected payment requests. You do not need "
          "to enter your UPI PIN to receive money.")
    )

with st.expander("🎁 " + t("Prize and Lottery Scams")):
    st.write(
        t("Be cautious of messages claiming you have won a prize but "
          "must pay a fee or share sensitive information to claim it.")
    )

with st.expander("💼 " + t("Fake Job Offers")):
    st.write(
        t("Be careful if someone asks for an advance payment or sensitive "
          "banking information for a promised job.")
    )

st.divider()

# Message checker
st.header("🔎 " + t("Suspicious Message Checker"))

st.write(
    t("Paste a suspicious SMS or message below. This basic checker "
      "looks for warning signs; it cannot prove whether a message is genuine.")
)

message = st.text_area(
    t("Paste the message here"),
    placeholder="Example: Your account will be blocked. Share your OTP now.",
    height=150,
    key="fraud_message_input"
)

if st.button(t("Check Message"), use_container_width=True):
    if not message.strip():
        st.warning(t("Please paste a message first."))
    else:
        suspicious_terms = [
            "otp",
            "pin",
            "password",
            "urgent",
            "blocked",
            "block your account",
            "verify immediately",
            "click here",
            "claim prize",
            "won a prize",
            "send money",
            "upi pin",
            "account suspended",
            "kyc expired",
            "remote access"
        ]

        message_lower = message.lower()
        matches = [
            term for term in suspicious_terms
            if term in message_lower
        ]

        if matches:
            st.warning(
                t("Warning: this message contains possible scam indicators.")
            )
            st.write(
                t("Warning signs detected") + ": " + ", ".join(matches)
            )
        else:
            st.info(
                t("No listed warning words were detected. "
                  "This does not mean the message is safe.")
            )

        st.caption(
            t("This is a basic keyword checker, not an AI-powered "
              "verification service. Always verify through official channels.")
        )

st.divider()

# What to do
st.header("✅ " + t("What To Do If You Suspect Fraud"))

st.markdown(
    "1. Stop responding to the suspicious caller or message.\n"
    "2. Do not share OTPs, PINs or passwords.\n"
    "3. Contact your bank using its official number or app.\n"
    "4. Preserve transaction references and relevant messages.\n"
    "5. In India, report suspected cyber financial fraud promptly "
    "by calling 1930 or using the official cybercrime reporting portal."
)

st.caption(
    "Official portal: https://www.cybercrime.gov.in/"
)

st.divider()

# Knowledge quiz
st.header("🧠 " + t("Fraud Awareness Quiz"))

answer = st.radio(
    t("A caller asks you to share an OTP to keep your bank account active. What should you do?"),
    [
        t("Share the OTP"),
        t("Refuse and contact the bank using official details"),
        t("Send the OTP to a friend")
    ],
    key="fraud_safety_quiz"
)

if st.button(t("Check Answer"), key="fraud_quiz_check"):
    if answer == t("Refuse and contact the bank using official details"):
        st.success(
            t("Correct! Never share your OTP, even with someone claiming to be from a bank.")
        )
    else:
        st.error(
            t("Incorrect. Keep your OTP private and verify through official channels.")
        )

st.divider()

if st.button("🏠 " + t("Home"), use_container_width=True):
    st.switch_page("app.py")

st.caption("💙 FinSaathi — " + t("Learn Finance. Stay Safe."))
