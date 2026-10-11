
import streamlit as st
import re
from translation import tr

st.set_page_config(
    page_title="FinSaathi - Fraud Safety",
    page_icon="🛡️",
    layout="wide"
)

def t(text):
    return tr(text)

if "language" not in st.session_state:
    st.session_state["language"] = "English"

st.title(t("🛡️ Fraud Safety Centre"))
st.write(t("Learn to recognise and avoid common financial scams."))

st.divider()

st.subheader(t("Warning Signs of Fraud"))

tips = [
    "Someone asks for your OTP, UPI PIN or password.",
    "A message threatens to block your bank account immediately.",
    "An unknown link promises a prize or unexpected payment.",
    "A caller pressures you to act urgently."
]

for tip in tips:
    st.warning(t(tip))

st.divider()

st.subheader(t("🔎 Suspicious Message Checker"))
st.write(t("Paste a suspicious SMS or message here"))

message = st.text_area(
    t("Enter the suspicious message"),
    height=150,
    key="fraud_message"
)

if st.button(t("Check Message"), use_container_width=True):
    if not message.strip():
        st.info(t("Please enter a message first."))
    else:
        patterns = {
            "OTP/PIN/password request":
                r"\b(otp|pin|password|passcode)\b",
            "Urgent threat":
                r"\b(block(ed)?|suspend(ed)?|urgent|immediately|expire[ds]?)\b",
            "Prize or reward bait":
                r"\b(prize|winner|reward|lottery|claim)\b",
            "Suspicious link":
                r"(https?://|www\.)",
            "UPI payment request":
                r"\b(upi|payment request|collect request)\b"
        }

        found = [
            reason
            for reason, pattern in patterns.items()
            if re.search(pattern, message, re.IGNORECASE)
        ]

        if found:
            st.error(
                t(
                    "⚠️ This message contains warning signs. "
                    "Verify it through official channels."
                )
            )
            st.write(t("Possible warning signs detected:"))

            translated_reasons = {
                "OTP/PIN/password request":
                    "Request for OTP, PIN or password",
                "Urgent threat":
                    "Urgent threat or pressure",
                "Prize or reward bait":
                    "Prize or reward offer",
                "Suspicious link":
                    "Link requiring caution",
                "UPI payment request":
                    "UPI payment request"
            }

            for reason in found:
                st.write("• " + t(translated_reasons[reason]))
        else:
            st.info(
                t(
                    "No common warning patterns were detected. "
                    "This does not guarantee that the message is safe."
                )
            )

        st.warning(
            t(
                "Never share your OTP, PIN or password. "
                "Do not click unknown links. Verify messages "
                "through official channels."
            )
        )

st.divider()

st.subheader(t("Important Safety Rules"))

rules = [
    "Never share your OTP, PIN or password.",
    "Never install an unknown app at a caller's request.",
    "Contact your bank using its official number."
]

for rule in rules:
    st.write("• " + t(rule))

st.divider()

st.info(
    t(
        "If you suspect financial cyber fraud in India, call 1930 "
        "promptly and report it at the official cybercrime portal."
    )
)

st.caption(
    t("Official reporting portal:") + " https://cybercrime.gov.in/"
)

st.caption(t("FinSaathi — Learn Finance. Stay Safe. 💙"))

if st.button(t("🏠 Home")):
    st.switch_page("app.py")

