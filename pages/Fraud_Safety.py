
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
selected_language = st.sidebar.selectbox(
    tr("Choose your language"),
    LANGUAGES,
    index=LANGUAGES.index(st.session_state["language"]),
    key="fraud_language"
)

if selected_language != st.session_state["language"]:
    st.session_state["language"] = selected_language
    st.query_params["language"] = selected_language
    st.rerun()

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
        "A person pretends to be a relative, official, police officer, or customer-care agent and demands money.",
        "Verify their identity through a separate, trusted contact method."
    ),
    (
        "📱 Remote-access app scams",
        "A caller asks you to install an app or share your screen to fix a banking problem.",
        "Do not give strangers access to your device or banking apps."
    ),
    (
        "💸 Fake loan offers",
        "A lender asks for an advance fee or sensitive details before giving a promised loan.",
        "Verify the lender and read the terms before sharing information or paying fees."
    )
]

for title, description, protection in fraud_types:
    with st.expander(tr(title)):
        st.write(tr(description))
        st.success(tr("How to stay safe: ") + tr(protection))

st.markdown("---")

# 2. Suspicious message checker
st.header(tr("2. Check a Suspicious Message"))
st.write(
    tr("Paste a suspicious SMS, email, or chat message below. "
       "This basic educational checker looks for warning signs. "
       "It cannot confirm whether a message is genuine.")
)

message = st.text_area(
    tr("Paste the message here"),
    height=150,
    placeholder=tr("Example: Your account will be blocked today. Click this link and share your OTP.")
)

if st.button(tr("🔍 Check Message"), use_container_width=True):
    if not message.strip():
        st.warning(tr("Please paste a message first."))
    else:
        text = message.lower()

        warning_phrases = {
            "urgent pressure": [
                "immediately", "urgent", "today only", "within 24 hours",
                "will be blocked", "account blocked", "last warning",
                "act now", "immediate action"
            ],
            "sensitive information request": [
                "share otp", "send otp", "enter your otp", "share pin",
                "upi pin", "atm pin", "password", "cvv", "card number"
            ],
            "suspicious payment or reward": [
                "claim your prize", "you have won", "lottery winner",
                "processing fee", "pay registration fee", "free gift",
                "guaranteed returns", "double your money"
            ],
            "suspicious link or account update": [
                "click here", "verify your account", "update your kyc",
                "kyc expired", "click the link", "account verification",
                "download this app", "install this app"
            ],
            "unusual payment request": [
                "scan this qr", "receive money", "collect request",
                "approve payment", "send money to verify"
            ]
        }

        found = []

        for category, phrases in warning_phrases.items():
            matches = [phrase for phrase in phrases if phrase in text]
            if matches:
                found.append((category, matches))

        if found:
            st.error(tr("⚠️ Warning signs detected"))
            st.write(
                tr("The message contains phrases that can appear in scams. "
                   "This does not prove that it is fraudulent.")
            )

            for category, matches in found:
                st.write("• " + tr(category.title()))
                st.caption(
                    tr("Matched phrases: ") + ", ".join(matches)
                )

            st.markdown("**" + tr("What you should do") + "**")
            st.write(tr("1. Do not click links or download attachments."))
            st.write(tr("2. Do not share OTPs, PINs, passwords, or bank details."))
            st.write(tr("3. Verify the request using an official app, website, or phone number."))
            st.write(tr("4. If money has been lost, contact your bank and report it promptly."))
        else:
            st.info(
                tr("No listed warning phrases were detected. "
                   "This does not mean the message is safe. "
                   "Check the sender, links, request, and context carefully.")
            )

st.caption(
    tr("Privacy tip: Avoid pasting real account numbers, phone numbers, OTPs, "
       "passwords, or other personal information into the checker.")
)

st.markdown("---")

# 3. Real-life examples
st.header(tr("3. Learn from These Examples"))

with st.expander(tr("Example A: Fake bank employee")):
    st.write(
        tr("A caller says your account will be frozen unless you tell them your OTP.")
    )
    st.write("**" + tr("Risk") + "**")
    st.write(tr("The caller may be trying to access your account."))
    st.write("**" + tr("Safe response") + "**")
    st.success(
        tr("Do not share the OTP. End the call and contact your bank through an official channel.")
    )

with st.expander(tr("Example B: QR code to receive money")):
    st.write(
        tr("A buyer says you must scan a QR code and enter your UPI PIN to receive payment.")
    )
    st.write("**" + tr("Risk") + "**")
    st.write(tr("You may accidentally authorise a payment instead of receiving money."))
    st.write("**" + tr("Safe response") + "**")
    st.success(
        tr("Do not enter your PIN to receive money. Check your UPI app for the actual transaction status.")
    )

with st.expander(tr("Example C: Fake investment opportunity")):
    st.write(
        tr("A social-media contact promises to double your money in a few days.")
    )
    st.write("**" + tr("Risk") + "**")
    st.write(tr("The offer may be designed to collect money and disappear."))
    st.write("**" + tr("Safe response") + "**")
    st.success(
        tr("Do not rush. Verify the company independently and be suspicious of guaranteed returns.")
    )

st.markdown("---")

# 4. What to do if money is lost
st.header(tr("4. What to Do If You Suspect Fraud"))

st.error(
    tr("Act quickly if money has been taken or an unauthorised transaction appears.")
)

response_steps = [
    "Contact your bank or payment service immediately using its official contact details.",
    "Ask the bank to report the transaction and secure the affected account or payment method.",
    "In India, call the cybercrime helpline 1930 as soon as possible for financial cyber fraud.",
    "Submit a report through the official National Cyber Crime Reporting Portal.",
    "Save transaction IDs, messages, phone numbers, screenshots, and complaint references.",
    "Change compromised passwords and secure your accounts from a trusted device.",
    "Never pay someone who promises to recover your money for an advance fee."
]

for index, step in enumerate(response_steps, start=1):
    st.write(f"**{index}.** {tr(step)}")

st.markdown("### " + tr("Official Reporting Resources"))

st.markdown(
    "- [National Cyber Crime Reporting Portal](https://cybercrime.gov.in/)\n"
    "- [Reserve Bank of India](https://www.rbi.org.in/)\n"
    "- [National Payments Corporation of India (UPI information)](https://www.npci.org.in/)"
)

st.caption(
    tr("Use official websites and verified contact details. "
       "Do not trust phone numbers or links sent by the suspected scammer.")
)

st.markdown("---")

# 5. Personal safety checklist
st.header(tr("5. My Fraud Safety Checklist"))

st.write(tr("Tick each habit you already follow:"))

checklist_items = [
    "I never share my OTP, UPI PIN, ATM PIN, or password.",
    "I verify unexpected calls and payment requests independently.",
    "I check the recipient and amount before approving a UPI payment.",
    "I avoid unknown links and unverified apps.",
    "I use official bank apps and websites.",
    "I review bank statements and transaction alerts.",
    "I know how to report cyber financial fraud."
]

for index, item in enumerate(checklist_items):
    st.checkbox(tr(item), key=f"fraud_safety_check_{index}")

st.markdown("---")

st.success(
    tr("Remember: Pause, verify, and protect your money. "
       "When in doubt, do not pay or share confidential information.")
)

st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
