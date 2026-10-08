import streamlit as st

st.set_page_config(
    page_title="UPI & Payments - FinSaathi",
    page_icon="📱"
)

st.title("📱 UPI & Digital Payments")
st.subheader("Learn how to use UPI safely")

st.write(
    "UPI makes digital payments fast and easy. "
    "Learn the basics before making a payment."
)

st.divider()

st.header("💡 What is UPI?")

st.write(
    "UPI stands for Unified Payments Interface. "
    "It allows you to send and receive money directly "
    "through a bank account using a UPI app."
)

st.divider()

st.header("📲 How to Make a UPI Payment")

st.write("1. Open your trusted UPI app.")
st.write("2. Select the person or business you want to pay.")
st.write("3. Enter the correct amount.")
st.write("4. Check the receiver name and amount.")
st.write("5. Enter your UPI PIN only to authorize your payment.")
st.write("6. Check whether the payment was successful.")

st.divider()

st.header("🛡️ UPI Safety Rules")

st.warning("🔐 Never share your UPI PIN with anyone.")

st.write("• You do not need your UPI PIN to receive money.")
st.write("• Never share your OTP with another person.")
st.write("• Check the receiver's name before paying.")
st.write("• Don't scan unknown QR codes.")
st.write("• Don't click suspicious payment links.")
st.write("• Never allow unknown people to control your phone.")

st.divider()

st.header("🚨 Common UPI Scams")

st.warning("💸 Fake Payment Request")
st.write(
    "Someone may send a fake payment request and ask you "
    "to enter your UPI PIN. Always check what you are approving."
)

st.warning("🎁 Fake Prize")
st.write(
    "Be careful if someone says you won a prize and asks "
    "you to make a payment or share banking information."
)

st.warning("📞 Fake Customer Care")
st.write(
    "Use customer-care numbers only from the official "
    "bank or UPI service website or app."
)

st.divider()

st.header("🧠 Remember")

st.success("CHECK → CONFIRM → PAY → VERIFY")

st.caption("FinSaathi – Learn Finance. Stay Safe. 💰")