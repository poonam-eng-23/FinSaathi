```python
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Fraud Safety | FinSaathi",
    page_icon="🛡️",
    layout="wide"
)

# RESTORE SELECTED LANGUAGE
if "language" not in st.session_state:
    saved_language = st.query_params.get("language", "English")

    if saved_language not in LANGUAGES:
        saved_language = "English"

    st.session_state["language"] = saved_language

# LANGUAGE SETTINGS
st.sidebar.title("🌐 " + tr("Language Settings"))

st.sidebar.selectbox(
    tr("Choose your language"),
    LANGUAGES,
    key="language",
    format_func=tr
)

st.query_params["language"] = st.session_state["language"]


# PAGE TITLE
st.title("🛡️ " + tr("Fraud Awareness and Safety"))

st.write(
    tr(
        "Learn about common financial scams, identify suspicious messages, "
        "and understand how to protect your money and personal information."
    )
)

st.info(
    "💡 " + tr(
        "Remember: Never share your OTP, UPI PIN, password, or banking details "
        "with anyone."
    )
)

st.markdown("---")


# SECTION 1: COMMON FINANCIAL SCAMS
st.header("1. " + tr("Common Financial Scams"))

scams = [
    {
        "Scam": "OTP Scam",
        "Description": "A stranger asks you to share the OTP received on your phone.",
        "Safety": "Never share your OTP with anyone."
    },
    {
        "Scam": "UPI Payment Scam",
        "Description": "Someone sends an unexpected payment request and asks you to approve it.",
        "Safety": "Approve only payments that you understand and initiated."
    },
    {
        "Scam": "Fake Bank Call",
        "Description": "A caller pretends to be a bank employee and asks for confidential information.",
        "Safety": "Contact your bank through its verified official channel."
    },
    {
        "Scam": "Lottery Scam",
        "Description": "A message claims that you have won a prize and asks for money or personal details.",
        "Safety": "Do not pay money to claim an unexpected prize."
    },
    {
        "Scam": "Phishing Link",
        "Description": "A suspicious message contains a link asking you to enter banking details.",
        "Safety": "Do not open suspicious links or enter confidential information."
    },
    {
        "Scam": "Fake Customer Care",
        "Description": "Someone provides a fake customer-care number and asks for account information.",
        "Safety": "Find customer-care details through the official bank website or application."
    },
    {
        "Scam": "Job Offer Scam",
        "Description": "A fake recruiter asks for money to provide a job.",
        "Safety": "Verify job offers through the organisation's official website."
    },
    {
        "Scam": "Investment Scam",
        "Description": "Someone promises unusually high or guaranteed returns.",
        "Safety": "Research the investment and verify the organisation before making decisions."
    }
]

for scam in scams:
    with st.expander(tr(scam["Scam"])):
        st.write("**" + tr("Description") + ":**")
        st.write(tr(scam["Description"]))

        st.success(
            "**" + tr("Safety Tip") + ":** "
            + tr(scam["Safety"])
        )

st.markdown("---")


# SECTION 2: SUSPICIOUS MESSAGE CHECKER
st.header("2. " + tr("Suspicious Message Checker"))

st.write(
    tr(
        "Enter a message below to check whether it contains common warning words."
    )
)

message = st.text_area(
    tr("Enter a suspicious message"),
    placeholder=tr("Example: Your bank account will be blocked. Share your OTP immediately."),
    height=120,
    key="fraud_message"
)

# Common warning words and phrases
suspicious_keywords = [
    "otp",
    "upi pin",
    "password",
    "account blocked",
    "account suspended",
    "urgent",
    "click here",
    "verify immediately",
    "claim your prize",
    "lottery",
    "send money",
    "bank details",
    "share your pin",
    "remote access",
    "refund fee",
    "won a prize",
    "limited time"
]

if st.button(
    tr("Check Message"),
    use_container_width=True
):

    if not message.strip():
        st.warning(tr("Please enter a message first."))

    else:
        message_lower = message.lower()

        detected_words = [
            word for word in suspicious_keywords
            if word in message_lower
        ]

        if detected_words:
            st.error(
                "🚨 " + tr("Warning! Suspicious words or phrases were found.")
            )

            st.write("**" + tr("Detected words") + ":**")

            for word in detected_words:
                st.write("- " + tr(word))

            st.warning(
                tr(
                    "Do not click suspicious links or share personal information. "
                    "Verify the message independently."
                )
            )

        else:
            st.success(
                tr(
                    "No listed warning words were detected. However, this does "
                    "not prove that the message is safe. Always verify the sender."
                )
            )

st.caption(
    tr(
        "Note: This is a basic keyword checker, not an AI fraud detector. "
        "It may miss suspicious messages or flag harmless ones."
    )
)

st.markdown("---")


# SECTION 3: REAL-LIFE EXAMPLES
st.header("3. " + tr("Real-Life Fraud Examples"))

examples = [
    {
        "title": "Example 1: Fake Bank Message",
        "message": "Your bank account will be blocked today. Click this link and update your details.",
        "answer": "This may be a phishing attempt. Do not click the link. Contact your bank through an official channel."
    },
    {
        "title": "Example 2: Fake Prize Message",
        "message": "Congratulations! You have won a cash prize. Pay a processing fee to receive it.",
        "answer": "This is a warning sign of a prize scam. Do not pay the fee."
    },
    {
        "title": "Example 3: Fake Customer Support",
        "message": "I am from customer support. Tell me your OTP to solve your payment problem.",
        "answer": "Never share your OTP. Contact official customer support yourself."
    },
    {
        "title": "Example 4: Suspicious UPI Request",
        "message": "Approve this unexpected UPI request to receive money.",
        "answer": "Do not approve an unexpected payment request. Check the details carefully."
    }
]

for example in examples:
    with st.expander(tr(example["title"])):
        st.write("**" + tr("Suspicious message") + ":**")
        st.write(tr(example["message"]))

        st.success(
            "**" + tr("Correct action") + ":** "
            + tr(example["answer"])
        )

st.markdown("---")


# SECTION 4: WARNING SIGNS
st.header("4. " + tr("Warning Signs of Financial Fraud"))

warning_signs = [
    "Someone asks for your OTP, UPI PIN, or password.",
    "A caller creates fear or pressure and demands immediate action.",
    "A message contains an unexpected payment or prize request.",
    "A stranger asks you to install an unknown application.",
    "Someone promises guaranteed high returns.",
    "A person asks you to pay money to receive a refund or prize.",
    "A website asks for confidential banking information without proper verification."
]

for sign in warning_signs:
    st.write("- " + tr(sign))

st.warning(
    "⚠️ " + tr(
        "Fraudsters may pretend to be bank employees, government officials, "
        "relatives, or customer-care representatives."
    )
)

st.markdown("---")


# SECTION 5: WHAT TO DO AFTER FINANCIAL FRAUD
st.header("5. " + tr("What to Do If You Become a Victim of Fraud"))

recovery_steps = [
    "Contact your bank immediately using a verified official channel.",
    "Report the suspicious transaction through your payment application.",
    "For suspected cyber financial fraud in India, call helpline 1930 promptly.",
    "Submit a complaint through the National Cyber Crime Reporting Portal.",
    "Keep transaction details and complaint acknowledgement numbers.",
    "Do not delete relevant messages or transaction records.",
    "Do not pay anyone who promises to recover your lost money."
]

for number, step in enumerate(recovery_steps, start=1):
    st.write(f"**{number}.** {tr(step)}")

st.error(
    "🚨 " + tr(
        "Report suspected financial cyber fraud as soon as possible. "
        "Contact your bank immediately."
    )
)

st.markdown(
    "**" + tr("Cyber Crime Helpline") + ": 1930"
)

st.markdown(
    "**" + tr("Official Complaint Portal") + ": "
    "https://cybercrime.gov.in/"
)

st.markdown(
    "**" + tr("NPCI Official Website") + ": "
    "https://www.npci.org.in/"
)

st.markdown("---")


# SECTION 6: FINANCIAL SAFETY CHECKLIST
st.header("6. " + tr("Financial Safety Checklist"))

st.write(
    tr("Tick the following points to check your safety habits.")
)

safety_checklist = [
    "I never share my OTP with anyone.",
    "I never share my UPI PIN or banking password.",
    "I verify payment requests before approving them.",
    "I avoid clicking unknown links.",
    "I use official banking applications.",
    "I verify customer-care numbers through official sources.",
    "I check my bank transactions regularly.",
    "I report suspected financial fraud promptly."
]

for index, item in enumerate(safety_checklist):
    st.checkbox(
        tr(item),
        key=f"fraud_safety_check_{index}"
    )

st.markdown("---")


# SECTION 7: IMPORTANT SAFETY TIPS
st.header("7. " + tr("Important Safety Tips"))

safety_tips = [
    "Keep your banking applications updated.",
    "Use strong and private passwords.",
    "Never share confidential banking information.",
    "Do not trust unknown callers or messages.",
    "Check the recipient's name before making payments.",
    "Avoid using public Wi-Fi for sensitive banking activities.",
    "Ask your bank for help through its official channels when in doubt."
]

for tip in safety_tips:
    st.success("🛡️ " + tr(tip))

st.markdown("---")


# FINAL MESSAGE
st.success(
    "💚 " + tr(
        "Stay alert, protect your personal information, and think before "
        "you click or make a payment."
    )
)

st.caption(
    tr("FinSaathi — Learn Finance. Stay Safe.")
)
```
