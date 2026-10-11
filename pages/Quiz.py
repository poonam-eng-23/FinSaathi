
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Financial Quiz - FinSaathi",
    page_icon="📝",
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
    key="quiz_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

# Quiz page
st.title("📝 " + tr("Financial Literacy Quiz"))
st.write(
    tr("Test your knowledge of banking, savings, UPI, and fraud safety.")
)

st.markdown("---")

questions = [
    {
        "question": "What should you do with your ATM PIN?",
        "options": [
            "Share it with friends",
            "Keep it secret",
            "Write it on your ATM card",
            "Tell it to unknown callers"
        ],
        "answer": "Keep it secret",
        "explanation": "Your ATM PIN is confidential. Never share it with anyone."
    },
    {
        "question": "What is the main purpose of saving money?",
        "options": [
            "To spend everything immediately",
            "To prepare for future needs and emergencies",
            "To give your password to others",
            "To avoid planning"
        ],
        "answer": "To prepare for future needs and emergencies",
        "explanation": "Savings can help you prepare for planned expenses and emergencies."
    },
    {
        "question": "Do you need to enter your UPI PIN to receive money?",
        "options": [
            "Yes, always",
            "Only for prizes",
            "No",
            "Only if a caller asks"
        ],
        "answer": "No",
        "explanation": "You do not need your UPI PIN to receive money."
    },
    {
        "question": "What should you do if you receive a suspicious bank link?",
        "options": [
            "Click it immediately",
            "Share it with everyone",
            "Enter your bank details",
            "Avoid clicking and verify through official channels"
        ],
        "answer": "Avoid clicking and verify through official channels",
        "explanation": "Suspicious links may be used to steal personal or banking information."
    },
    {
        "question": "What is a budget?",
        "options": [
            "A plan for income and expenses",
            "A bank password",
            "An ATM card",
            "A type of scam"
        ],
        "answer": "A plan for income and expenses",
        "explanation": "A budget helps you plan spending and savings."
    },
    {
        "question": "What should you do if you suspect financial cyber fraud in India?",
        "options": [
            "Ignore it",
            "Share your OTP",
            "Call 1930 promptly and contact your bank",
            "Send more money to the caller"
        ],
        "answer": "Call 1930 promptly and contact your bank",
        "explanation": "Report suspected financial cyber fraud quickly and contact your bank."
    }
]

st.subheader("📚 " + tr("Answer the Questions"))

user_answers = []

for index, item in enumerate(questions):
    st.markdown(
        f"**{index + 1}. {tr(item['question'])}**"
    )

    translated_options = [tr(option) for option in item["options"]]

    answer = st.radio(
        tr("Choose your answer"),
        translated_options,
        index=None,
        key=f"quiz_answer_{index}",
        label_visibility="collapsed"
    )

    user_answers.append(answer)
    st.markdown("---")

if st.button("Submit Quiz", use_container_width=True):
    unanswered = sum(answer is None for answer in user_answers)

    if unanswered:
        st.warning(
            tr("Please answer all questions before submitting.") +
            f" ({unanswered})"
        )
    else:
        score = 0

        for index, item in enumerate(questions):
            correct_answer = tr(item["answer"])

            if user_answers[index] == correct_answer:
                score += 1

        st.subheader("🏆 " + tr("Your Quiz Result"))
        st.metric(
            tr("Your Score"),
            f"{score} / {len(questions)}"
        )

        percentage = score / len(questions)
        st.progress(percentage)

        if score == len(questions):
            st.success(
                "🎉 " + tr("Excellent! You answered every question correctly.")
            )
        elif score >= 4:
            st.success(
                tr("Good job! Review the explanations to improve further.")
            )
        else:
            st.info(
                tr("Keep learning! Review the lessons and try again.")
            )

        st.subheader("📖 " + tr("Answer Review"))

        for index, item in enumerate(questions):
            correct_answer = tr(item["answer"])

            st.markdown(
                f"**{index + 1}. {tr(item['question'])}**"
            )
            st.write(
                tr("Correct answer") + ": " + correct_answer
            )
            st.caption(tr(item["explanation"]))

st.markdown("---")
st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
