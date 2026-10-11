```python
import streamlit as st
from translation import tr

st.set_page_config(
    page_title="FinSaathi - UPI",
    page_icon="📱",
    layout="wide"
)

def t(text):
    return tr(text)

if "language" not in st.session_state:
    st.session_state["language"] = "English"

st.title(t("📱 UPI & Digital Payments"))
st.write(t("Learn how to make digital payments safely."))

st.divider()

st.subheader(t("What is UPI?"))
st.write(
    t(
        "UPI allows you to transfer money between bank accounts "
        "using a supported payment app."
    )
)

st.subheader(t("How to Send Money"))
steps = [
    "Open your trusted UPI payment app.",
    "Choose a recipient or scan their QR code.",
    "Check the recipient's name and amount carefully.",
    "Enter your UPI PIN only to authorise a payment you are making."
]

for i, step in enumerate(steps, start=1):
    st.write(f"{i}. {t(step)}")

st.divider()

st.subheader(t("Important Safety Rules"))
st.warning(
    t("You do not need to enter your UPI PIN to receive money.")
)
st.warning(
    t("Never share your UPI PIN or OTP with anyone.")
)
st.info(
    t("Do not approve unexpected collect requests.")
)

st.divider()

st.subheader(t("Quick Safety Quiz"))
st.write(
    t(
        "Someone says you must enter your UPI PIN to receive "
        "a payment. What should you do?"
    )
)

options = [
    t("Enter the PIN immediately"),
    t("Do not enter it; verify the request"),
    t("Share your PIN with the caller")
]

answer = st.radio(
    t("Choose your answer"),
    options,
    key="upi_safety_quiz"
)

if st.button(t("Check Answer")):
    if answer == options[1]:
        st.success(
            t("Correct! A UPI PIN is not needed to receive money.")
        )
    else:
        st.error(
            t("Not quite. Never enter your UPI PIN just to receive money.")
        )

st.divider()

st.caption(t("FinSaathi — Learn Finance. Stay Safe. 💙"))

if st.button(t("🏠 Home")):
    st.switch_page("app.py")
```
