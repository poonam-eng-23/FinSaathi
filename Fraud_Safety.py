import streamlit as st

st.set_page_config(
    page_title="Fraud Safety - FinSaathi",
    page_icon="🛡️"
)

st.title("🛡️ Fraud Safety Checker")
st.subheader("Check a message for common signs of online fraud")

st.write(
    "Paste a suspicious SMS, WhatsApp message, email, or offer below. "
    "FinSaathi will check it for common warning signs."
)

st.divider()

# ---------------- FRAUD CHECKER ----------------

st.header("🔍 Check a Suspicious Message")

message = st.text_area(
    "Enter the message here:",
    placeholder="Example: Congratulations! You have won ₹50,000. Click this link to claim your prize.",
    height=150
)

if st.button("🔍 Check for Fraud"):

    if not message.strip():
        st.warning("⚠️ Please enter a message first.")

    else:
        text = message.lower()

        warning_words = [
            "urgent",
            "click",
            "verify",
            "otp",
            "password",
            "prize",
            "winner",
            "won",
            "claim",
            "bank",
            "account",
            "blocked",
            "lottery",
            "payment",
            "upi",
            "link",
            "refund",
            "kyc"
        ]

        found_words = []

        for word in warning_words:
            if word in text:
                found_words.append(word)

        if len(found_words) >= 2:

            st.error("🚨 Potential Fraud Detected!")

            st.write(
                "This message contains several common warning signs "
                "of online fraud."
            )

            st.write(
                "⚠️ Warning signs found:",
                ", ".join(sorted(set(found_words)))
            )

            st.info(
                "Do not share OTPs, passwords, PINs or banking details. "
                "Avoid clicking unknown links."
            )

        elif len(found_words) == 1:

            st.warning("⚠️ Be Careful")

            st.write(
                "This message contains a possible warning sign. "
                "Verify the information using an official source."
            )

            st.write(
                "Possible warning sign:",
                found_words[0]
            )

        else:

            st.success("✅ No obvious fraud warning signs detected.")

            st.write(
                "However, this does not guarantee that the message is safe. "
                "Always verify unexpected requests."
            )


st.divider()

# ---------------- COMMON FRAUDS ----------------

st.header("🚨 Common Frauds")

st.warning("📞 Fake Calls")
st.write(
    "Never share your OTP, ATM PIN, UPI PIN or password "
    "with anyone over a phone call."
)

st.warning("📱 Fake Messages")
st.write(
    "Be careful with messages claiming that you have won a prize "
    "or asking you to update your bank account."
)

st.warning("🔗 Fake Links")
st.write(
    "Do not click suspicious links. Check the website address "
    "before entering any personal information."
)

st.warning("💳 UPI Fraud")
st.write(
    "You do NOT need to enter your UPI PIN to receive money. "
    "Enter your PIN only when you are making a payment."
)

st.divider()

# ---------------- SAFETY RULES ----------------

st.header("✅ Safety Rules")

st.write("1. Never share OTP or PIN.")
st.write("2. Do not trust unknown callers.")
st.write("3. Do not click suspicious links.")
st.write("4. Check payment details before paying.")
st.write("5. Use official bank or government websites.")
st.write("6. If something seems suspicious, stop and verify.")

st.divider()

# ---------------- REMEMBER ----------------

st.header("💡 Remember")

st.success(
    "STOP → THINK → VERIFY → THEN PAY"
)

st.caption("FinSaathi – Learn Finance. Stay Safe. 💰")