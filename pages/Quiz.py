
import streamlit as st
from translation import tr

st.set_page_config(
    page_title="FinSaathi - Quiz",
    page_icon="🧠",
    layout="wide"
)

def t(text):
    return tr(text)

if "language" not in st.session_state:
    st.session_state["language"] = "English"

st.title(t("🧠 Financial Literacy Quiz"))
st.write(t("Test your knowledge and learn how to stay financially safe."))

st.divider()

questions = [
    {
        "question": "What should you do with your UPI PIN?",
        "options": [
            "Share it with bank staff",
            "Keep it secret",
            "Write it on your ATM card",
            "Send it in a message"
        ],
        "answer": 1,
        "explanation": "Never share your UPI PIN with anyone."
    },
    {
        "question": "Do you need a UPI PIN to receive money?",
        "options": [
            "Yes, always",
            "Only at night",
            "No, you do not",
            "Only for large amounts"
        ],
        "answer": 2,
        "explanation": "You do not need a UPI PIN to receive money."
    },
    {
        "question": "What is a good saving habit?",
        "options": [
            "Spend all your income",
            "Borrow money for every purchase",
            "Ignore your expenses",
            "Save some money regularly"
        ],
        "answer": 3,
        "explanation": "Regular saving can help you prepare for future needs."
    },
    {
        "question": "What should you do with a suspicious bank link?",
        "options": [
            "Click it immediately",
            "Avoid it and verify through official channels",
            "Share it with everyone",
            "Enter your bank password"
        ],
        "answer": 1,
        "explanation": "Avoid unknown links and verify messages with your bank."
    },
    {
        "question": "What is a budget?",
        "options": [
            "A plan for income and expenses",
            "A bank password",
            "An ATM card",
            "A type of online scam"
        ],
        "answer": 0,
        "explanation": "A budget helps you plan your income and spending."
    }
]

if "quiz_answers" not in st.session_state:
    st.session_state["quiz_answers"] = {}

if "quiz_submitted" not in st.session_state:
    st.session_state["quiz_submitted"] = False

st.subheader(t("Answer the Questions"))

for i, q in enumerate(questions):
    st.markdown(f"**{i + 1}. {t(q['question'])}**")

    selected = st.radio(
        t("Choose one answer"),
        q["options"],
        key=f"quiz_question_{i}",
        format_func=t,
        index=None
    )

    st.session_state["quiz_answers"][i] = selected
    st.write("")

if st.button(t("Submit Quiz"), use_container_width=True):
    st.session_state["quiz_submitted"] = True

if st.session_state["quiz_submitted"]:
    score = 0

    for i, q in enumerate(questions):
        selected = st.session_state["quiz_answers"].get(i)

        if selected is None:
            continue

        selected_index = q["options"].index(selected)

        if selected_index == q["answer"]:
            score += 1

    st.divider()
    st.subheader(t("Your Result"))
    st.metric(
        t("Your Score"),
        f"{score} / {len(questions)}"
    )

    if score == len(questions):
        st.success(t("Excellent! You answered every question correctly."))
    elif score >= 3:
        st.success(t("Good work! Keep learning about financial safety."))
    else:
        st.info(t("Keep practising. Review the lessons and try again."))

    st.subheader(t("Answer Review"))

    for i, q in enumerate(questions):
        selected = st.session_state["quiz_answers"].get(i)
        correct_option = q["options"][q["answer"]]

        st.write(f"**{i + 1}. {t(q['question'])}**")

        if selected == correct_option:
            st.success(t("Correct answer") + ": " + t(correct_option))
        else:
            st.error(t("Correct answer") + ": " + t(correct_option))

        st.write(t(q["explanation"]))

    if st.button(t("Try Again")):
        st.session_state["quiz_submitted"] = False
        st.session_state["quiz_answers"] = {}
        for i in range(len(questions)):
            st.session_state.pop(f"quiz_question_{i}", None)
        st.rerun()

st.divider()
st.caption(t("FinSaathi — Learn Finance. Stay Safe. 💙"))

if st.button(t("🏠 Home")):
    st.switch_page("app.py")
