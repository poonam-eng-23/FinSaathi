
import streamlit as st
import random

st.set_page_config(
    page_title="Financial Literacy Quiz - FinSaathi",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Financial Literacy Quiz")
st.write("Test your knowledge about banking, savings, UPI, and fraud safety!")

questions = [
    {
        "question": "1. Should you share your ATM PIN with someone who calls you?",
        "options": [
            "Yes, if they say they are from the bank",
            "No, never share your PIN",
            "Only with unknown callers"
        ],
        "answer": "No, never share your PIN",
        "explanation": "Keep your PIN secret, even from people claiming to be bank employees."
    },
    {
        "question": "2. What should you do before making a UPI payment?",
        "options": [
            "Check the recipient and amount",
            "Share your UPI PIN with the recipient",
            "Approve every payment request"
        ],
        "answer": "Check the recipient and amount",
        "explanation": "Always verify the recipient and amount before approving a payment."
    },
    {
        "question": "3. What is the main purpose of a budget?",
        "options": [
            "To spend all your money",
            "To plan income and expenses",
            "To borrow more money"
        ],
        "answer": "To plan income and expenses",
        "explanation": "A budget helps you plan spending and work towards savings goals."
    },
    {
        "question": "4. What should you do if you receive a suspicious bank link?",
        "options": [
            "Click it immediately",
            "Forward it to everyone",
            "Avoid clicking and verify with the bank"
        ],
        "answer": "Avoid clicking and verify with the bank",
        "explanation": "Suspicious links may be used to steal personal or banking information."
    },
    {
        "question": "5. Why is saving money useful?",
        "options": [
            "It can help with future needs and emergencies",
            "It means you must never spend money",
            "It guarantees you will become rich"
        ],
        "answer": "It can help with future needs and emergencies",
        "explanation": "Savings can help prepare for future expenses and unexpected needs."
    },
    {
        "question": "6. What does OTP mean?",
        "options": [
            "One-Time Password",
            "Online Transfer Payment",
            "Open Transaction Process"
        ],
        "answer": "One-Time Password",
        "explanation": "An OTP is a temporary code. Never disclose it to other people."
    },
    {
        "question": "7. If you suspect financial cyber fraud in India, which number can you call?",
        "options": [
            "100",
            "1930",
            "1098"
        ],
        "answer": "1930",
        "explanation": "1930 is India's helpline for reporting suspected cyber financial fraud."
    }
]

if "quiz_order" not in st.session_state:
    st.session_state.quiz_order = list(range(len(questions)))
    random.shuffle(st.session_state.quiz_order)

if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

for number, question_index in enumerate(st.session_state.quiz_order):
    question = questions[question_index]

    st.markdown("---")
    st.subheader(question["question"])

    selected = st.radio(
        "Choose your answer:",
        question["options"],
        key=f"quiz_{question_index}"
    )

    st.session_state.quiz_answers[question_index] = selected

if st.button("Submit Quiz"):
    score = 0

    for question_index, selected in st.session_state.quiz_answers.items():
        if selected == questions[question_index]["answer"]:
            score += 1

    st.session_state.quiz_score = score
    st.session_state.quiz_submitted = True

if st.session_state.get("quiz_submitted", False):
    score = st.session_state.quiz_score

    st.markdown("---")
    st.subheader("Your Results")
    st.metric("Your Score", f"{score} / {len(questions)}")

    if score == len(questions):
        st.success("Excellent! You answered every question correctly.")
    elif score >= 4:
        st.info("Good work! Review the explanations to learn more.")
    else:
        st.warning("Keep learning! Review the banking and fraud safety pages.")

    st.subheader("Correct Answers and Explanations")

    for question in questions:
        st.write(f"**{question['question']}**")
        st.write(f"Correct answer: {question['answer']}")
        st.caption(question["explanation"])

    if st.button("Try Again"):
        for key in ["quiz_order", "quiz_answers", "quiz_score", "quiz_submitted"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

st.markdown("---")
st.caption("FinSaathi — Learn Finance. Stay Safe.")
