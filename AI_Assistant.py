import streamlit as st

st.set_page_config(
    page_title="AI Assistant - FinSaathi",
    page_icon="🤖"
)

st.title("🤖 FinSaathi AI Assistant")
st.subheader("Ask simple questions about money and banking")

st.write(
    "Ask a question in simple English. "
    "The assistant will provide a basic financial explanation."
)

st.divider()

question = st.text_area(
    "💬 Type your question",
    placeholder="Example: What is an ATM?"
)

if st.button("🤖 Ask Assistant"):

    if question.strip() == "":
        st.warning("Please type a question first.")

    else:
        q = question.lower()

        if "atm" in q:
            st.info(
                "ATM means Automated Teller Machine. "
                "It allows you to withdraw cash and use some banking services."
            )

        elif "upi" in q:
            st.info(
                "UPI is a digital payment system that allows you "
                "to send and receive money using a mobile phone."
            )

        elif "otp" in q:
            st.warning(
                "OTP is a One-Time Password. Never share your OTP "
                "with anyone, even if they claim to be from your bank."
            )

        elif "saving" in q or "save" in q:
            st.info(
                "Saving means keeping some money aside for future needs "
                "or emergencies."
            )

        elif "bank account" in q:
            st.info(
                "A bank account is used to safely keep money and "
                "perform banking transactions."
            )

        elif "fraud" in q or "scam" in q:
            st.warning(
                "Never share your OTP, UPI PIN, ATM PIN or password. "
                "If you receive a suspicious message or call, verify it "
                "through an official source."
            )

        else:
            st.info(
                "I can currently answer basic questions about "
                "ATM, UPI, OTP, savings, bank accounts and fraud safety."
            )

st.divider()

st.success(
    "🛡️ Safety reminder: Never share your OTP, UPI PIN, "
    "ATM PIN or password with anyone."
)

st.caption("FinSaathi – Learn Finance. Stay Safe. 💰")