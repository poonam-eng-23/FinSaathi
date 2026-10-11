import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Banking - FinSaathi",
    page_icon="🏦",
    layout="wide"
)

# Language selector
st.sidebar.title("🌐 " + tr("Language Settings"))

current_language = st.session_state.get("language", "English")
if current_language not in LANGUAGES:
    current_language = "English"

selected_language = st.sidebar.selectbox(
    "Choose your language",
    LANGUAGES,
    index=LANGUAGES.index(current_language),
    key="banking_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

# Page heading
st.title("🏦 " + tr("Complete Banking Guide"))
st.write(
    tr(
        "Learn how bank accounts work, how to use banking services, "
        "and how to protect your money."
    )
)

st.info(
    "💡 " + tr(
        "A bank can help you save money, receive payments, "
        "and access financial services."
    )
)

st.markdown("---")

# Section 1: Introduction
st.header("1. " + tr("Understanding Banking"))

st.write(
    tr(
        "A bank is a financial institution that accepts deposits, "
        "helps customers make payments, and provides services such as "
        "loans and money transfers."
    )
)

st.subheader(tr("Why do people use banks?"))

bank_uses = [
    "To keep money in a bank account.",
    "To receive salary, pensions, scholarships, and other eligible payments.",
    "To send and receive money.",
    "To save money and earn interest on eligible deposits.",
    "To access loans subject to eligibility and bank approval.",
    "To maintain a record of financial transactions."
]

for item in bank_uses:
    st.markdown("- " + tr(item))

st.subheader(tr("Important Banking Terms"))

terms = [
    (
        "Deposit",
        "Money placed into a bank account."
    ),
    (
        "Withdrawal",
        "Money taken out of a bank account."
    ),
    (
        "Interest",
        "Money earned on eligible savings or paid on a loan."
    ),
    (
        "Balance",
        "The amount of money recorded in an account."
    ),
    (
        "Nominee",
        "A person nominated to receive eligible account proceeds "
        "under applicable rules."
    ),
    (
        "KYC",
        "Know Your Customer: identity and address verification "
        "required for financial services."
    ),
    (
        "Passbook",
        "A record of account transactions provided by a bank."
    )
]

st.table({
    tr("Term"): [tr(item[0]) for item in terms],
    tr("Meaning"): [tr(item[1]) for item in terms]
})

st.markdown("---")

# Section 2: Account types
st.header("2. " + tr("Types of Bank Accounts"))

account_types = [
    (
        "Savings Account",
        "For individuals who want to save money and access it when needed.",
        "Check interest rates, minimum balance requirements, and charges."
    ),
    (
        "Current Account",
        "Often used by businesses that need frequent transactions.",
        "Check transaction limits, charges, and account conditions."
    ),
    (
        "Fixed Deposit (FD)",
        "Money deposited for a chosen period under agreed terms.",
        "Check interest, maturity date, and early withdrawal rules."
    ),
    (
        "Recurring Deposit (RD)",
        "A fixed amount deposited regularly for a chosen period.",
        "Check the required instalment, tenure, and missed-payment rules."
    )
]

st.table({
    tr("Account Type"): [tr(item[0]) for item in account_types],
    tr("Purpose"): [tr(item[1]) for item in account_types],
    tr("What to Check"): [tr(item[2]) for item in account_types]
})

st.subheader(tr("Example: Choosing an Account"))

st.write(
    tr(
        "Meena receives money each month and wants to save part of it "
        "while keeping some money available for daily expenses. "
        "A savings account may suit her needs. She should compare "
        "account conditions before choosing a bank."
    )
)

st.success(
    "✅ " + tr(
        "Choose an account based on your needs, access requirements, "
        "fees, and the bank's terms."
    )
)

st.markdown("---")

# Section 3: Opening an account
st.header("3. " + tr("How to Open a Bank Account"))

st.write(
    tr(
        "You can enquire at a bank branch or use an official digital "
        "banking channel if the service is available to you."
    )
)

opening_steps = [
    "Choose a bank and compare its account options.",
    "Ask about minimum balance, fees, interest, and available services.",
    "Ask the bank which identity and address documents are accepted.",
    "Complete the application using accurate information.",
    "Complete the bank's identity verification process.",
    "Read the account terms before accepting them.",
    "Keep your account details and passbook or statement safely."
]

for index, step in enumerate(opening_steps, start=1):
    st.markdown(f"**{index}.** {tr(step)}")

st.subheader(tr("Documents and Information"))

st.write(
    tr(
        "Banks may ask for identity information, address details, "
        "photographs, PAN or Form 60 where applicable, and other "
        "documents depending on the account and current rules."
    )
)

st.warning(
    "⚠️ " + tr(
        "Requirements vary by account type and bank. Confirm the current "
        "requirements with the official bank before applying. "
        "Never give original documents or sensitive information to "
        "an unverified agent."
    )
)

with st.expander("📘 " + tr("Example: A Student Opens an Account")):
    st.write(
        tr(
            "Ravi wants an account to receive a scholarship. "
            "He checks which accounts are available to students, "
            "asks about fees and required documents, and confirms "
            "the scholarship's bank-account requirements with the "
            "official institution before applying."
        )
    )

st.markdown("---")

# Section 4: ATM and debit cards
st.header("4. " + tr("ATM and Debit Card Safety"))

st.write(
    tr(
        "An Automated Teller Machine (ATM) can allow customers to "
        "withdraw cash, check balances, and perform other supported "
        "transactions using an authorised card or banking method."
    )
)

st.subheader(tr("Safe ATM Steps"))

atm_steps = [
    "Use an ATM in a safe and well-lit location.",
    "Check for anything unusual around the machine.",
    "Shield the keypad when entering your PIN.",
    "Follow the on-screen instructions carefully.",
    "Collect your cash and card before leaving.",
    "Keep the receipt if needed and check your account statement.",
    "Report a retained card or suspicious transaction to your bank."
]

for index, step in enumerate(atm_steps, start=1):
    st.markdown(f"{index}. {tr(step)}")

st.subheader(tr("Never Do These Things"))

unsafe_actions = [
    "Never tell anyone your ATM PIN or OTP.",
    "Never write your PIN on your card.",
    "Never accept help from an unknown person using your card.",
    "Never ignore an unfamiliar transaction alert.",
    "Never disclose banking passwords to callers claiming to be bank staff."
]

for item in unsafe_actions:
    st.markdown("- " + tr(item))

st.markdown("---")

# Section 5: Statements and errors
st.header("5. " + tr("Understanding Your Bank Statement"))

st.write(
    tr(
        "A bank statement records money coming into and going out "
        "of an account. Reviewing it regularly can help you notice "
        "mistakes or unfamiliar transactions."
    )
)

st.table({
    tr("Entry"): [
        tr("Opening Balance"),
        tr("Deposit"),
        tr("Withdrawal"),
        tr("Bank Charge"),
        tr("Closing Balance")
    ],
    tr("Meaning"): [
        tr("Balance at the start of the period."),
        tr("Money added to the account."),
        tr("Money taken out of the account."),
        tr("A fee charged according to the bank's terms."),
        tr("Balance at the end of the period.")
    ]
})

st.subheader(tr("What if something goes wrong?"))

problems = [
    (
        "Cash was not dispensed, but the account was debited.",
        "Keep the transaction details and contact your bank through its official complaint channel."
    ),
    (
        "An unknown transaction appears.",
        "Contact the bank immediately, report the transaction, and follow its security instructions."
    ),
    (
        "Your ATM card is lost.",
        "Ask the bank to block the card using an official channel."
    ),
    (
        "Your account details appear incorrect.",
        "Contact the bank and request an explanation or correction."
    )
]

for problem, action in problems:
    with st.expander("❓ " + tr(problem)):
        st.write(tr(action))

st.markdown("---")

# Section 6: Government financial inclusion
st.header("6. " + tr("Government Banking Schemes"))

st.write(
    tr(
        "The following Indian government programmes may help eligible "
        "people access banking or financial protection services. "
        "Benefits and eligibility depend on the current official rules."
    )
)

schemes = [
    (
        "Pradhan Mantri Jan-Dhan Yojana (PMJDY)",
        "A financial inclusion programme intended to expand access to basic banking services.",
        "Ask a participating bank about account eligibility, facilities, and current terms.",
        "https://pmjdy.gov.in/"
    ),
    (
        "Pradhan Mantri Suraksha Bima Yojana (PMSBY)",
        "A government-backed accident insurance scheme for eligible subscribers.",
        "Check current eligibility, premium, coverage, and enrolment rules with an authorised bank.",
        "https://jansuraksha.gov.in/"
    ),
    (
        "Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)",
        "A government-backed life insurance scheme for eligible subscribers.",
        "Check current eligibility, premium, coverage, and renewal conditions with an authorised bank.",
        "https://jansuraksha.gov.in/"
    ),
    (
        "Atal Pension Yojana (APY)",
        "A pension scheme subject to eligibility and applicable rules.",
        "Check age conditions, contribution requirements, and current eligibility with an authorised bank.",
        "https://www.npscra.nsdl.co.in/"
    )
]

for name, description, details, url in schemes:
    with st.expander("🏛️ " + tr(name)):
        st.write(tr(description))
        st.write("**" + tr("What to check") + ":** " + tr(details))
        st.link_button(
            tr("Visit Official Website"),
            url,
            use_container_width=True
        )

st.warning(
    "⚠️ " + tr(
        "Scheme rules, eligibility, premiums, and benefits can change. "
        "Verify all details on the official website or with an authorised "
        "bank before making a decision. FinSaathi does not guarantee eligibility."
    )
)

st.markdown("---")

# Section 7: Real-life case study
st.header("7. " + tr("Real-Life Case Study"))

st.subheader(tr("Case: A Suspicious Bank Call"))

st.write(
    tr(
        "Anita receives a call from someone claiming to be a bank employee. "
        "The caller says her account will be blocked unless she shares "
        "an OTP immediately."
    )
)

st.write("**" + tr("What should Anita do?") + "**")

case_answer = st.radio(
    tr("Choose the safest action"),
    [
        tr("Share the OTP to keep the account active."),
        tr("End the call and contact the bank using official details."),
        tr("Tell the caller her ATM PIN instead.")
    ],
    index=None,
    key="banking_case_answer"
)

if st.button("Check Case Study", use_container_width=True):
    if case_answer is None:
        st.info(tr("Please choose an answer."))
    elif case_answer == tr(
        "End the call and contact the bank using official details."
    ):
        st.success(
            "✅ " + tr(
                "Correct. Never disclose OTPs or PINs to callers. "
                "Verify account concerns independently."
            )
        )
    else:
        st.error(
            "❌ " + tr(
                "That is unsafe. Keep your OTP and PIN private and contact "
                "your bank through an official channel."
            )
        )

st.markdown("---")

# Section 8: Knowledge quiz
st.header("8. " + tr("Banking Knowledge Quiz"))

quiz_questions = [
    {
        "question": "Which account is commonly used for personal savings?",
        "options": [
            "Savings Account",
            "ATM PIN",
            "Bank Statement"
        ],
        "answer": "Savings Account",
        "explanation": "A savings account is designed for personal deposits and access to money under its terms."
    },
    {
        "question": "What should you do if you notice an unknown bank transaction?",
        "options": [
            "Ignore it",
            "Report it to the bank promptly",
            "Share your OTP with a caller"
        ],
        "answer": "Report it to the bank promptly",
        "explanation": "Prompt reporting helps the bank investigate and advise on account protection."
    },
    {
        "question": "Who should know your ATM PIN?",
        "options": [
            "Unknown callers",
            "Friends",
            "You should keep it secret"
        ],
        "answer": "You should keep it secret",
        "explanation": "Keep your PIN confidential and never share it."
    },
    {
        "question": "Where should you verify government banking scheme details?",
        "options": [
            "An unknown message",
            "An official government website or authorised bank",
            "An unverified social media post"
        ],
        "answer": "An official government website or authorised bank",
        "explanation": "Official sources provide the appropriate scheme conditions and current requirements."
    },
    {
        "question": "What does a bank statement show?",
        "options": [
            "Account transactions",
            "Your social media password",
            "A caller's identity automatically"
        ],
        "answer": "Account transactions",
        "explanation": "A bank statement records transactions and balances for an account."
    }
]

quiz_answers = []

for index, item in enumerate(quiz_questions):
    st.markdown(
        f"**{index + 1}. {tr(item['question'])}**"
    )

    answer = st.radio(
        tr("Choose your answer"),
        [tr(option) for option in item["options"]],
        index=None,
        key=f"banking_quiz_{index}",
        label_visibility="collapsed"
    )

    quiz_answers.append(answer)

if st.button("Submit Banking Quiz", use_container_width=True):
    if any(answer is None for answer in quiz_answers):
        st.warning(tr("Please answer all questions before submitting."))
    else:
        score = 0

        for index, item in enumerate(quiz_questions):
            if quiz_answers[index] == tr(item["answer"]):
                score += 1

        st.metric(
            tr("Your Score"),
            f"{score} / {len(quiz_questions)}"
        )

        st.progress(score / len(quiz_questions))

        if score == len(quiz_questions):
            st.success(tr("Excellent! All answers are correct."))
        elif score >= 3:
            st.success(tr("Good work! Review the explanations below."))
        else:
            st.info(tr("Keep learning and try the quiz again."))

        st.subheader(tr("Answer Explanations"))

        for index, item in enumerate(quiz_questions):
            st.markdown(
                f"**{index + 1}. {tr(item['answer'])}**"
            )
            st.write(tr(item["explanation"]))

st.markdown("---")

st.subheader("📌 " + tr("Banking Safety Checklist"))

checklist = [
    "Keep your PINs, OTPs, and passwords private.",
    "Use official bank websites and apps.",
    "Review account transactions regularly.",
    "Report suspected fraud immediately.",
    "Read account terms and fees before signing up."
]

for index, item in enumerate(checklist):
    st.checkbox(
        tr(item),
        key=f"banking_checklist_{index}"
    )

st.markdown("---")
st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
