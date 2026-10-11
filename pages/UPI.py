
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="UPI | FinSaathi",
    page_icon="📱",
    layout="wide"
)

# Restore the language selected in FinSaathi
if "language" not in st.session_state:
    saved_language = st.query_params.get("language", "English")
    if saved_language not in LANGUAGES:
        saved_language = "English"
    st.session_state["language"] = saved_language

st.sidebar.title("🌐 " + tr("Language Settings"))

selected_language = st.sidebar.selectbox(
    tr("Choose your language"),
    LANGUAGES,
    index=LANGUAGES.index(st.session_state["language"]),
    key="upi_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

st.title("📱 " + tr("UPI Digital Payments"))
st.write(
    tr(
        "Learn how Unified Payments Interface (UPI) works, how to make "
        "payments safely, and how to recognise common digital payment scams."
    )
)

st.info(
    "💡 " + tr(
        "UPI makes it possible to transfer money between supported bank "
        "accounts through compatible payment applications."
    )
)

st.markdown("---")

# SECTION 1: UPI BASICS
st.header("1. " + tr("What Is UPI?"))

st.write(
    tr(
        "UPI stands for Unified Payments Interface. It is a digital payment "
        "system developed by the National Payments Corporation of India (NPCI). "
        "It enables supported bank accounts to send and receive money using "
        "compatible payment applications."
    )
)

st.markdown("**" + tr("Common uses of UPI") + "**")

st.markdown(
    "- " + tr("Paying a shopkeeper.") + "\n"
    "- " + tr("Sending money to another person.") + "\n"
    "- " + tr("Paying certain bills.") + "\n"
    "- " + tr("Checking transaction status in a payment application.") + "\n"
    "- " + tr("Receiving money through supported payment methods.")
)

st.success(
    "📌 " + tr(
        "Example: A customer scans a shop's genuine payment QR code, "
        "checks the merchant and amount, and authorises the payment."
    )
)

st.markdown("---")

# SECTION 2: IMPORTANT UPI TERMS
st.header("2. " + tr("Important UPI Terms"))

upi_terms = [
    {
        tr("Term"): tr("UPI ID"),
        tr("Meaning"): tr("An address used to identify a UPI account for payments")
    },
    {
        tr("Term"): tr("QR Code"),
        tr("Meaning"): tr("A code that a compatible application can scan to prepare a payment")
    },
    {
        tr("Term"): tr("UPI PIN"),
        tr("Meaning"): tr("A confidential PIN used to authorise certain banking transactions")
    },
    {
        tr("Term"): tr("Transaction ID"),
        tr("Meaning"): tr("A reference that helps identify a particular transaction")
    },
    {
        tr("Term"): tr("Pending Transaction"),
        tr("Meaning"): tr("A payment whose final status has not yet been confirmed")
    }
]

st.table(upi_terms)

st.warning(
    "🔐 " + tr(
        "A UPI PIN is confidential. Never disclose it to another person, "
        "even if they claim to be a bank employee or payment support agent."
    )
)

st.markdown("---")

# SECTION 3: HOW TO MAKE A PAYMENT
st.header("3. " + tr("How to Make a UPI Payment"))

st.write(
    tr(
        "The exact screens vary by application, but the basic process is similar."
    )
)

payment_steps = [
    tr("Open your installed, trusted UPI payment application."),
    tr("Choose the appropriate payment option, such as paying a person or merchant."),
    tr("Select or enter the recipient details, or scan the intended merchant's QR code."),
    tr("Check the recipient name and enter the correct amount."),
    tr("Review the details carefully before proceeding."),
    tr("Authorise the payment yourself if the transaction is genuine and intended."),
    tr("Check the final status and keep the transaction reference.")
]

for number, step in enumerate(payment_steps, start=1):
    st.write(f"**{number}.** {step}")

st.error(
    "🚨 " + tr(
        "Never enter your UPI PIN just to receive money. A PIN request normally "
        "authorises a payment or another banking action, so read the screen carefully."
    )
)

st.markdown("---")

# SECTION 4: SAFE PAYMENT PRACTICE
st.header("4. " + tr("Interactive Payment Practice"))

st.write(
    tr(
        "Practise checking a fictional payment before making a decision. "
        "This activity does not connect to a bank or move real money."
    )
)

practice_recipient = st.selectbox(
    tr("Fictional recipient"),
    [
        "Ravi Stores",
        "Unknown Recipient",
        "School Book Shop"
    ],
    key="upi_practice_recipient"
)

practice_amount = st.number_input(
    tr("Practice payment amount (₹)"),
    min_value=1,
    max_value=100000,
    value=250,
    step=50,
    key="upi_practice_amount"
)

st.write(tr("Recipient") + ": " + practice_recipient)
st.write(tr("Amount") + f": ₹{practice_amount:,.2f}")

confirm_payment = st.checkbox(
    tr(
        "I have checked the fictional recipient and amount and understand "
        "that this is only a practice activity."
    ),
    key="upi_practice_confirm"
)

if st.button(tr("Review Practice Payment"), use_container_width=True):
    if not confirm_payment:
        st.warning(
            tr("Read the details and tick the confirmation box first.")
        )
    elif practice_recipient == "Unknown Recipient":
        st.error(
            tr(
                "Practice result: Do not proceed until you independently "
                "verify who the recipient is."
            )
        )
    else:
        st.success(
            tr(
                "Practice result: The details have been reviewed for this "
                "demonstration. In a real payment, verify the recipient and "
                "amount in your payment application before authorising anything."
            )
        )

st.caption(
    tr(
        "This demonstration never processes a payment, collects a PIN, "
        "or accesses a bank account."
    )
)

st.markdown("---")

# SECTION 5: QR CODE SAFETY
st.header("5. " + tr("QR Code Safety"))

st.write(
    tr(
        "QR codes can make payments convenient, but scanning a code does not "
        "prove that it is genuine."
    )
)

st.markdown("**" + tr("Before paying") + "**")

st.markdown(
    "- " + tr("Check who will receive the money.") + "\n"
    "- " + tr("Confirm the amount before authorising the transaction.") + "\n"
    "- " + tr("Do not scan a suspicious QR code simply because a stranger asks you to.") + "\n"
    "- " + tr("Do not approve an unexpected collect request.") + "\n"
    "- " + tr("Keep your payment application updated through its official app store.")
)

with st.expander(tr("Example: Someone says to scan a QR code to receive a prize")):
    st.write(
        tr(
            "A stranger claims that scanning a code and entering a PIN will "
            "credit a prize. This is a warning sign. Do not proceed. Verify "
            "any prize through the organisation's independently confirmed official channel."
        )
    )

st.markdown("---")

# SECTION 6: COMMON UPI SCAMS
st.header("6. " + tr("Common UPI Scams"))

scam_examples = [
    {
        tr("Scam type"): tr("Fake customer support"),
        tr("Warning sign"): tr("A caller asks for a PIN, OTP, or remote access to your phone."),
        tr("Safe response"): tr("End the interaction and contact official support yourself.")
    },
    {
        tr("Scam type"): tr("Fake collect request"),
        tr("Warning sign"): tr("An unexpected request asks you to approve a payment."),
        tr("Safe response"): tr("Reject requests you did not initiate or cannot verify.")
    },
    {
        tr("Scam type"): tr("Fake payment screenshot"),
        tr("Warning sign"): tr("Someone shows an image claiming money was sent."),
        tr("Safe response"): tr("Check your own application and account transaction record.")
    },
    {
        tr("Scam type"): tr("Impersonation"),
        tr("Warning sign"): tr("Someone pretends to be a relative, official, or bank employee."),
        tr("Safe response"): tr("Verify the person's identity through a separate trusted channel.")
    },
    {
        tr("Scam type"): tr("Fraudulent refund offer"),
        tr("Warning sign"): tr("Someone asks for a fee, PIN, or OTP to release a refund."),
        tr("Safe response"): tr("Use the official application or bank complaint process.")
    }
]

st.dataframe(
    scam_examples,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# SECTION 7: PAYMENT PROBLEMS
st.header("7. " + tr("What If a Payment Fails?"))

st.write(
    tr(
        "A payment may show pending, failed, or successful. Do not assume that "
        "a pending payment has failed or repeat it immediately without checking."
    )
)

st.markdown(
    "1. " + tr("Open your payment application's transaction history.") + "\n"
    "2. " + tr("Check the final status and transaction reference.") + "\n"
    "3. " + tr("Check your bank account statement or balance through a trusted channel.") + "\n"
    "4. " + tr("Follow the application's official dispute or complaint process.") + "\n"
    "5. " + tr("Keep the reference number and any complaint acknowledgement.") + "\n"
    "6. " + tr("Contact your bank if the issue remains unresolved.")
)

st.warning(
    "📌 " + tr(
        "Avoid making a duplicate payment until you have checked the transaction status."
    )
)

st.markdown("---")

# SECTION 8: REPORTING FRAUD
st.header("8. " + tr("How to Report UPI Fraud in India"))

st.markdown(
    "1. " + tr("Contact your bank immediately using a verified official channel.") + "\n"
    "2. " + tr("Report the suspicious transaction in your payment application.") + "\n"
    "3. " + tr("For suspected cyber financial fraud, call India's helpline 1930 promptly.") + "\n"
    "4. " + tr("Submit a report through the official National Cyber Crime Reporting Portal.") + "\n"
    "5. " + tr("Keep transaction references and complaint numbers for follow-up.")
)

st.markdown(
    "**" + tr("Official reporting portal") + ": "
    "https://cybercrime.gov.in/"
)

st.markdown(
    "**" + tr("NPCI official website") + ": "
    "https://www.npci.org.in/"
)

st.error(
    "🛡️ " + tr(
        "Never pay a stranger who promises to recover lost money. "
        "Use your bank and official reporting channels."
    )
)

st.markdown("---")

# SECTION 9: UPI SAFETY CHECKLIST
st.header("9. " + tr("UPI Safety Checklist"))

checklist = [
    tr("I verify the recipient before sending money."),
    tr("I check the amount before authorising a payment."),
    tr("I never share my UPI PIN or OTP."),
    tr("I do not approve unexpected collect requests."),
    tr("I verify payment status in my own application."),
    tr("I use official customer-support channels."),
    tr("I report suspected fraud promptly.")
]

for index, item in enumerate(checklist):
    st.checkbox(item, key=f"upi_safety_{index}")

st.markdown("---")

st.success(
    "📱 " + tr(
        "Remember: UPI is convenient when used carefully. Verify every "
        "payment, protect your PIN, and never rush because someone pressures you."
    )
)

st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
