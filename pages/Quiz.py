
import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi - Financial Quiz",
    page_icon="🧠",
    layout="wide"
)

if "language" not in st.session_state:
    st.session_state["language"] = "English"

if "language_picker" not in st.session_state:
    st.session_state["language_picker"] = st.session_state["language"]


def t(text):
    return tr(text)


def update_language():
    st.session_state["language"] = st.session_state["language_picker"]


st.sidebar.title("💙 FinSaathi")

st.sidebar.selectbox(
    t("Choose your language"),
    LANGUAGES,
    key="language_picker",
    on_change=update_language
)

# Accessibility settings
apply_accessibility()

# Quiz page
st.title("🧠 " + t("Financial Literacy Quiz"))

st.write(
    t("Test your knowledge about banking, savings, UPI and fraud safety.")
)

st.info(
    t("Answer all questions and click Submit Quiz to see your score.")
)

# Questions and answers
questions = [
    {
        "question": "1. What should you do with your banking OTP?",
        "options": [
            "Share it with callers",
            "Keep it private",
            "Post it online",
            "Send it to strangers"
        ],
        "answer": "Keep it private",
        "explanation": "An OTP is private. Never share it with anyone."
    },
    {
        "question": "2. What is a good saving habit?",
        "options": [
            "Spend all your money",
            "Borrow for every purchase",
            "Save regularly when possible",
            "Ignore your expenses"
        ],
        "answer": "Save regularly when possible",
        "explanation": "Regular saving can help you prepare for future needs."
    },
    {
        "question": "3. Do you need a UPI PIN to receive money?",
        "options": [
            "Yes, always",
            "No, you do not need it to receive money",
            "Only at night",
            "Only for small payments"
        ],
        "answer": "No, you do not need it to receive money",
        "explanation": "A UPI PIN is used to authorise payments, not to receive money."
    },
    {
        "question": "4. What should you do with an unknown banking link?",
        "options": [
            "Open it immediately",
            "Enter your PIN",
            "Forward it to everyone",
            "Avoid it and verify through official channels"
        ],
        "answer": "Avoid it and verify through official channels",
        "explanation": "Unknown links may lead to fake websites or scams."
    },
    {
        "question": "5. What is a budget?",
        "options": [
            "A plan for managing money",
            "A bank password",
            "A payment PIN",
            "A lottery ticket"
        ],
        "answer": "A plan for managing money",
        "explanation": "A budget helps you plan income, expenses and savings."
    },
    {
        "question": "6. What should you do if you notice a suspicious bank transaction?",
        "options": [
            "Ignore it",
            "Share your OTP with a caller",
            "Contact your bank using official details",
            "Post your account details online"
        ],
        "answer": "Contact your bank using official details",
        "explanation": "Contact your bank promptly and follow its fraud-reporting guidance."
    },
    {
        "question": "7. Which is an essential banking safety rule?",
        "options": [
            "Use the same PIN everywhere",
            "Share passwords with strangers",
            "Write your OTP in public",
            "Keep your PIN and password private"
        ],
        "answer": "Keep your PIN and password private",
        "explanation": "Keep your banking credentials confidential and secure."
    },
    {
        "question": "8. What should you check before making a UPI payment?",
        "options": [
            "Only the phone wallpaper",
            "The recipient and amount",
            "The weather",
            "Nothing at all"
        ],
        "answer": "The recipient and amount",
        "explanation": "Always verify the recipient and amount before authorising payment."
    },
    {
        "question": "9. What is a sensible way to manage expenses?",
        "options": [
            "Record and review them",
            "Never check your spending",
            "Spend without planning",
            "Ignore essential needs"
        ],
        "answer": "Record and review them",
        "explanation": "Tracking expenses helps you understand where your money goes."
    },
    {
        "question": "10. What should you do if you suspect online financial fraud in India?",
        "options": [
            "Share your PIN with the caller",
            "Delete all evidence immediately",
            "Report promptly through official channels",
            "Ignore every transaction"
        ],
        "answer": "Report promptly through official channels",
        "explanation": "Contact your bank and report suspected cyber financial fraud promptly. India's helpline is 1930."
    }
]

# Initialise quiz state
if "quiz_submitted" not in st.session_state:
    st.session_state["quiz_submitted"] = False

if "quiz_score" not in st.session_state:
    st.session_state["quiz_score"] = 0

# Quiz form
with st.form("financial_literacy_quiz"):
    selected_answers = {}

    for index, item in enumerate(questions):
        st.subheader(item["question"])

        selected_answers[index] = st.radio(
            "Choose one answer:",
            item["options"],
            index=None,
            key=f"financial_quiz_question_{index}"
        )

        st.divider()

    submitted = st.form_submit_button(
        "✅ Submit Quiz",
        use_container_width=True
    )

    if submitted:
        score = 0

        for index, item in enumerate(questions):
            if selected_answers[index] == item["answer"]:
                score += 1

        st.session_state["quiz_score"] = score
        st.session_state["quiz_submitted"] = True

# Results
if st.session_state["quiz_submitted"]:
    score = st.session_state["quiz_score"]
    percentage = score / len(questions) * 100

    st.header("🏆 " + t("Your Quiz Result"))

    st.metric(
        t("Your Score"),
        f"{score} / {len(questions)}"
    )

    st.progress(percentage / 100)

    st.write(f"{t('Percentage')}: {percentage:.0f}%")

    if percentage >= 80:
        st.success(
            t("Excellent! You have a good understanding of financial safety.")
        )
    elif percentage >= 50:
        st.info(
            t("Good effort! Review the explanations and try again.")
        )
    else:
        st.warning(
            t("Keep learning! Review the lessons and attempt the quiz again.")
        )

    st.subheader("📘 " + t("Answer Review"))

    for index, item in enumerate(questions):
        st.markdown(f"**{item['question']}**")
        st.write(f"{t('Correct answer')}: {item['answer']}")
        st.caption(item["explanation"])

    if st.button("🔄 " + t("Try Again"), use_container_width=True):
        st.session_state["quiz_submitted"] = False
        st.session_state["quiz_score"] = 0

        for index in range(len(questions)):
            key = f"financial_quiz_question_{index}"
            if key in st.session_state:
                del st.session_state[key]

        st.rerun()

st.divider()

if st.button("🏠 " + t("Home"), use_container_width=True):
    st.switch_page("app.py")

st.caption("💙 FinSaathi — " + t("Learn Finance. Stay Safe."))
