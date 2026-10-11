
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Banking | FinSaathi",
    page_icon="🏦",
    layout="wide"
)

# Keep the selected language consistent with FinSaathi
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
    key="banking_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

st.title("🏦 " + tr("Banking Basics"))
st.write(
    tr(
        "Learn how bank accounts work, how to use ATMs safely, "
        "how to read bank statements, and how to protect your money."
    )
)

st.info(
    "💡 " + tr(
        "A bank helps you keep money safe, receive payments, "
        "save for the future, and make digital transactions."
    )
)

st.markdown("---")

# SECTION 1: INTRODUCTION
st.header("1. " + tr("Understanding Banking"))

st.write(
    tr(
        "A bank is a financial institution that accepts deposits, "
        "helps people save money, supports payments, and may provide loans."
    )
)

st.markdown("**" + tr("Why do people use banks?") + "**")
st.markdown(
    "- " + tr("To keep money safer than carrying large amounts of cash.") + "\n"
    "- " + tr("To receive salaries, scholarships, pensions, and government benefits.") + "\n"
    "- " + tr("To transfer money to other people.") + "\n"
    "- " + tr("To save money and earn interest where applicable.") + "\n"
    "- " + tr("To maintain a record of financial transactions.")
)

st.success(
    "📌 " + tr(
        "Example: A student can receive a scholarship in a bank account "
        "and use a debit card or approved digital payment service for expenses."
    )
)

st.markdown("---")

# SECTION 2: TYPES OF ACCOUNTS
st.header("2. " + tr("Types of Bank Accounts"))

account_data = [
    {
        tr("Account type"): tr("Savings Account"),
        tr("Main purpose"): tr("Personal savings and everyday transactions"),
        tr("Important point"): tr("Interest and minimum-balance rules vary by bank")
    },
    {
        tr("Account type"): tr("Current Account"),
        tr("Main purpose"): tr("Business transactions"),
        tr("Important point"): tr("Usually designed for frequent transactions")
    },
    {
        tr("Account type"): tr("Fixed Deposit (FD)"),
        tr("Main purpose"): tr("Keeping a lump sum for a chosen period"),
        tr("Important point"): tr("Premature withdrawal may have conditions or penalties")
    },
    {
        tr("Account type"): tr("Recurring Deposit (RD)"),
        tr("Main purpose"): tr("Depositing a chosen amount regularly"),
        tr("Important point"): tr("Deposit schedule and terms depend on the institution")
    }
]

st.table(account_data)

st.subheader("How to choose an account")

st.markdown(
    "1. " + tr("Decide why you need the account.") + "\n"
    "2. " + tr("Compare service charges, minimum balance, and interest terms.") + "\n"
    "3. " + tr("Check access to branches, ATMs, and digital banking.") + "\n"
    "4. " + tr("Read the terms and conditions before opening the account.") + "\n"
    "5. " + tr("Use the bank's official website or branch for verified information.")
)

st.markdown("---")

# SECTION 3: OPENING AN ACCOUNT
st.header("3. " + tr("How to Open a Bank Account"))

st.write(
    tr(
        "Requirements differ by account type and bank. Ask the bank for its "
        "current document list before applying."
    )
)

st.markdown("**" + tr("Step-by-step guide") + "**")

steps = [
    tr("Choose a bank and account suitable for your needs."),
    tr("Ask about eligibility, fees, minimum balance, and services."),
    tr("Prepare the required identity and address documents."),
    tr("Complete the official application form."),
    tr("Complete identity verification as required by the bank."),
    tr("Read the account terms and keep your account details secure.")
]

for number, step in enumerate(steps, start=1):
    st.write(f"**{number}.** {step}")

st.warning(
    "⚠️ " + tr(
        "Never submit false documents. Do not share your banking password, "
        "OTP, PIN, or confidential credentials with anyone claiming to help "
        "you open an account."
    )
)

st.markdown("---")

# SECTION 4: ATM AND DEBIT CARD SAFETY
st.header("4. " + tr("ATM and Debit Card Safety"))

st.subheader("Using an ATM safely")

st.markdown(
    "- " + tr("Check your surroundings before using an ATM.") + "\n"
    "- " + tr("Cover the keypad while entering your PIN.") + "\n"
    "- " + tr("Never write your PIN on your card.") + "\n"
    "- " + tr("Do not accept help from strangers with your card or PIN.") + "\n"
    "- " + tr("Collect your card and cash before leaving.") + "\n"
    "- " + tr("Check transaction alerts and your account statement.") + "\n"
    "- " + tr("Report a lost card immediately through your bank's official channel.")
)

st.subheader("Example situation")

with st.expander(tr("What should you do if your card is lost?")):
    st.write(
        tr(
            "Contact your bank immediately using its official app, website, "
            "or verified customer-care number. Request card blocking, review "
            "recent transactions, and report any unauthorised transaction promptly."
        )
    )

st.markdown("---")

# SECTION 5: BANK STATEMENTS
st.header("5. " + tr("Understanding Your Bank Statement"))

st.write(
    tr(
        "A bank statement records money entering and leaving your account. "
        "Review it regularly to identify mistakes or suspicious transactions."
    )
)

statement_data = [
    {
        tr("Term"): tr("Opening Balance"),
        tr("Meaning"): tr("Money in the account at the start of the period")
    },
    {
        tr("Term"): tr("Credit"),
        tr("Meaning"): tr("Money added to the account")
    },
    {
        tr("Term"): tr("Debit"),
        tr("Meaning"): tr("Money taken out of the account")
    },
    {
        tr("Term"): tr("Closing Balance"),
        tr("Meaning"): tr("Money remaining at the end of the period")
    },
    {
        tr("Term"): tr("Transaction Reference"),
        tr("Meaning"): tr("Identifier that can help the bank trace a transaction")
    }
]

st.table(statement_data)

st.subheader("Practice example")

opening_balance = 1000
money_received = 500
money_spent = 250
closing_balance = opening_balance + money_received - money_spent

st.write(tr("Opening balance") + ": ₹1,000")
st.write(tr("Money received") + ": ₹500")
st.write(tr("Money spent") + ": ₹250")
st.metric(
    tr("Closing balance"),
    f"₹{closing_balance:,}"
)

st.caption(
    tr("This is a fictional example for learning, not a real bank statement.")
)

st.subheader("If you notice an unfamiliar transaction")

st.markdown(
    "1. " + tr("Check the transaction date, amount, and reference.") + "\n"
    "2. " + tr("Contact your bank through its official channel.") + "\n"
    "3. " + tr("Report unauthorised transactions promptly.") + "\n"
    "4. " + tr("Keep the complaint reference number and relevant records.") + "\n"
    "5. " + tr("Never share an OTP or PIN to obtain a refund.")
)

st.markdown("---")

# SECTION 6: GOVERNMENT BANKING SCHEMES
st.header("6. " + tr("Government Banking Schemes"))

st.write(
    tr(
        "The following schemes may help eligible people access banking, "
        "insurance, or pension services. Eligibility, benefits, premiums, "
        "and rules can change. Verify current details through official sources."
    )
)

schemes = [
    {
        tr("Scheme"): "Pradhan Mantri Jan-Dhan Yojana (PMJDY)",
        tr("Purpose"): tr("Financial inclusion and access to basic banking services"),
        tr("Official website"): "https://pmjdy.gov.in/"
    },
    {
        tr("Scheme"): "Pradhan Mantri Suraksha Bima Yojana (PMSBY)",
        tr("Purpose"): tr("Accident insurance for eligible subscribers"),
        tr("Official website"): "https://jansuraksha.gov.in/"
    },
    {
        tr("Scheme"): "Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)",
        tr("Purpose"): tr("Life insurance for eligible subscribers"),
        tr("Official website"): "https://jansuraksha.gov.in/"
    },
    {
        tr("Scheme"): "Atal Pension Yojana (APY)",
        tr("Purpose"): tr("Pension scheme subject to current eligibility rules"),
        tr("Official website"): "https://www.pfrda.org.in/"
    }
]

st.dataframe(schemes, use_container_width=True, hide_index=True)

st.info(
    "📌 " + tr(
        "Do not assume that every scheme is free or that everyone qualifies. "
        "Confirm eligibility, charges, benefits, and current conditions with "
        "the official scheme website or an authorised bank."
    )
)

st.markdown("---")

# SECTION 7: CASE STUDY
st.header("7. " + tr("Banking Case Study"))

st.write(
    tr(
        "A person receives a phone call from someone claiming to be a bank "
        "employee. The caller says the person's account will be blocked unless "
        "they reveal an OTP immediately."
    )
)

with st.expander(tr("Read the situation and safety guidance")):
    st.markdown("**" + tr("Warning signs") + "**")
    st.markdown(
        "- " + tr("The caller creates urgency or fear.") + "\n"
        "- " + tr("The caller asks for a confidential OTP or PIN.") + "\n"
        "- " + tr("The caller pressures the person to act without verification.")
    )

    st.markdown("**" + tr("What should the person do?") + "**")
    st.markdown(
        "1. " + tr("Do not reveal the OTP or PIN.") + "\n"
        "2. " + tr("End the call and do not follow suspicious instructions.") + "\n"
        "3. " + tr("Contact the bank using a verified official number.") + "\n"
        "4. " + tr("If money is lost, contact the bank and report the incident promptly.")
    )

st.success(
    "🛡️ " + tr(
        "Safety rule: Never share your OTP, PIN, password, or other "
        "confidential banking credentials with callers."
    )
)

st.markdown("---")

# SECTION 8: BANKING SAFETY CHECKLIST
st.header("8. " + tr("Banking Safety Checklist"))

st.write(
    tr("Use this checklist to review your everyday banking habits.")
)

checklist_items = [
    tr("I keep my PIN and passwords private."),
    tr("I never share OTPs with callers or messages."),
    tr("I use official banking apps and websites."),
    tr("I review transaction messages and statements."),
    tr("I report lost cards and suspicious transactions promptly."),
    tr("I check fees and terms before accepting a banking product."),
    tr("I never install unknown apps at the request of a caller."),
    tr("I verify government schemes using official sources.")
]

for item in checklist_items:
    st.checkbox(item, key="banking_check_" + str(checklist_items.index(item)))

st.markdown("---")

st.subheader("Remember")

st.info(
    "🏦 " + tr(
        "Use banks to manage money carefully, read the terms of financial "
        "products, protect confidential information, and verify important "
        "details through official sources."
    )
)

st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
