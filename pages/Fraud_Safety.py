
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Fraud Safety - FinSaathi",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Fraud Safety")
st.write("Learn how to identify scams and protect your money.")

st.markdown("---")

st.subheader("Common Financial Scams")

st.markdown("""
- **Fake bank calls:** Someone pretends to be a bank employee.
- **OTP scams:** Someone asks you to reveal a one-time password.
- **Fake links:** A message asks you to open a suspicious website.
- **UPI scams:** Someone tricks you into approving an unwanted payment.
- **Prize scams:** Someone asks for money to release a fake prize.
""")

st.warning(
    "Never share your OTP, PIN, password, or banking details "
    "with callers or through suspicious links."
)

st.subheader("Check a Suspicious Message")

message = st.text_area(
    "Paste the SMS or message you received",
    placeholder="Paste the message here..."
)

if st.button("Check Message"):
    if not message.strip():
        st.info("Please enter a message first.")
    else:
        suspicious_words = [
            "otp", "pin", "password", "urgent", "prize",
            "won", "click link", "verify account",
            "blocked", "send money", "upi pin"
        ]

        matched = [
            word for word in suspicious_words
            if word in message.lower()
        ]

        if matched:
            st.warning(
                "Caution: This message contains words often "
                "associated with scams. Do not click links or "
                "share personal details until you verify it."
            )
        else:
            st.info(
                "No common warning words were detected. "
                "That does not mean the message is safe. "
                "Verify the sender independently."
            )

st.subheader("What should you do if you suspect fraud?")

st.markdown("""
1. Do not click suspicious links.
2. Never share your OTP or PIN.
3. Contact your bank using its official contact details.
4. In India, report suspected cyber financial fraud by calling 1930.
""")

st.markdown("---")
st.caption("FinSaathi — Learn Finance. Stay Safe.")
