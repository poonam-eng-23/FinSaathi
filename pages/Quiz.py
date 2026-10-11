
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Financial Quiz | FinSaathi",
    page_icon="🎯",
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
    key="quiz_language"
)

if selected_language != st.session_state["language"]:
    st.session_state["language"] = selected_language
    st.query_params["language"] = selected_language
    st.rerun()

st.title(tr("🎯 FinSaathi Financial Literacy Quiz"))
st.subheader(tr("Test your knowledge and learn safer money habits."))

st.info(
    tr("Choose the best answer for each question. "
       "Read the explanation after submitting your answer.")
)

# Questions are stored as: question, options, correct option index, explanation, topic.
questions = [
    {
        "question": "What should you do with your bank OTP?",
        "options": [
            "Share it with a caller claiming to be from the bank",
            "Keep it private and enter it only when you initiate a trusted transaction",
            "Send it to a stranger on social media",
            "Write it on your debit card"
        ],
        "answer": 1,
        "explanation": "An OTP is confidential. Never disclose it to callers or strangers.",
        "topic": "Banking Safety"
    },
    {
        "question": "Which is a good first step when making a monthly budget?",
        "options": [
            "Spend all your money first",
            "Ignore regular bills",
            "List your income and expected expenses",
            "Borrow money for every purchase"
        ],
        "answer": 2,
        "explanation": "Knowing your income and expenses helps you make a realistic plan.",
        "topic": "Budgeting"
    },
    {
        "question": "What should you do if a stranger sends a suspicious bank link?",
        "options": [
            "Click immediately",
            "Enter your password to check",
            "Forward it to everyone",
            "Avoid clicking and verify through the official bank channel"
        ],
        "answer": 3,
        "explanation": "Unexpected links can lead to fake websites that steal personal information.",
        "topic": "Fraud Safety"
    },
    {
        "question": "Do you normally need a UPI PIN to receive money?",
        "options": [
            "Yes, every time",
            "No, a UPI PIN is generally used to authorise a payment",
            "Yes, if the sender asks",
            "Only when scanning a stranger's QR code"
        ],
        "answer": 1,
        "explanation": "Be cautious if someone asks you to enter your PIN to receive money.",
        "topic": "UPI Safety"
    },
    {
        "question": "What is an emergency fund intended for?",
        "options": [
            "Unexpected necessary expenses",
            "Only entertainment",
            "Buying things because they are trending",
            "Giving money to unknown callers"
        ],
        "answer": 0,
        "explanation": "An emergency fund can help cover unexpected costs, depending on your circumstances.",
        "topic": "Savings"
    },
    {
        "question": "What is simple interest on ₹1,000 at 5% per year for 2 years?",
        "options": [
            "₹50",
            "₹100",
            "₹200",
            "₹1,100"
        ],
        "answer": 1,
        "explanation": "Simple interest = Principal × Rate × Time ÷ 100. Here it is ₹1,000 × 5 × 2 ÷ 100 = ₹100.",
        "topic": "Interest"
    },
    {
        "question": "What is the safest response to a guaranteed high-return investment offer from an unknown person?",
        "options": [
            "Invest immediately",
            "Borrow money to invest more",
            "Verify the provider and be cautious of promises of guaranteed high returns",
            "Share your bank password"
        ],
        "answer": 2,
        "explanation": "Promises of unusually high guaranteed returns can be a warning sign. Verify independently.",
        "topic": "Investment Safety"
    },
    {
        "question": "What should you do before approving a UPI payment?",
        "options": [
            "Check the recipient and amount",
            "Ignore the amount",
            "Share your PIN with the recipient",
            "Approve every request automatically"
        ],
        "answer": 0,
        "explanation": "Always check the recipient and amount before authorising a transaction.",
        "topic": "UPI Safety"
    },
    {
        "question": "What is a sensible way to save money regularly?",
        "options": [
            "Save only if money is left after every unnecessary purchase",
            "Set a realistic savings target and track progress",
            "Stop paying essential bills",
            "Give your savings to an unknown person"
        ],
        "answer": 1,
        "explanation": "A realistic savings target makes it easier to build a consistent habit.",
        "topic": "Savings"
    },
    {
        "question": "If you lose money through suspected financial cyber fraud in India, which helpline can you call?",
        "options": [
            "1000",
            "1930",
            "5555",
            "1234"
        ],
        "answer": 1,
        "explanation": "Call India's cyber financial fraud helpline 1930 promptly and report at cybercrime.gov.in.",
        "topic": "Fraud Reporting"
    },
    {
        "question": "Why should you read loan terms before accepting a loan?",
        "options": [
            "To understand interest, fees, and repayment obligations",
            "Because every loan is free",
            "To avoid knowing the repayment amount",
            "Because the terms never matter"
        ],
        "answer": 0,
        "explanation": "Understanding the total repayment and fees helps you make an informed decision.",
        "topic": "Borrowing"
    },
    {
        "question": "Which information should you keep confidential?",
        "options": [
            "A public bank branch address",
            "A published government website",
            "Your banking password and UPI PIN",
            "A general budgeting tip"
        ],
        "answer": 2,
        "explanation": "Keep passwords and PINs private. Never disclose them to callers or strangers.",
        "topic": "Privacy"
    }
]

# Start and reset controls
if "quiz_started" not in st.session_state:
    st.session_state["quiz_started"] = False

if "quiz_answers" not in st.session_state:
    st.session_state["quiz_answers"] = {}

if "quiz_submitted" not in st.session_state:
    st.session_state["quiz_submitted"] = False

col1, col2 = st.columns(2)

with col1:
    if st.button(
        tr("▶️ Start / Restart Quiz"),
        use_container_width=True
    ):
        st.session_state["quiz_started"] = True
        st.session_state["quiz_answers"] = {}
        st.session_state["quiz_submitted"] = False
        st.rerun()

with col2:
    st.metric(tr("Total Questions"), len(questions))

if not st.session_state["quiz_started"]:
    st.markdown("### " + tr("Topics covered"))
    st.write(
        tr("Banking • Savings • Budgeting • UPI • Fraud Safety • "
           "Interest • Investments • Borrowing • Privacy")
    )
    st.write(tr("Press Start / Restart Quiz to begin."))
    st.stop()

st.markdown("---")

# Answer each question
for index, item in enumerate(questions):
    st.markdown(
        f"### {tr('Question')} {index + 1}: {tr(item['question'])}"
    )

    selected_answer = st.radio(
        tr("Choose one answer"),
        options=range(len(item["options"])),
        format_func=lambda option, item=item: tr(item["options"][option]),
        key=f"quiz_answer_{index}",
        index=st.session_state["quiz_answers"].get(index)
    )

    st.session_state["quiz_answers"][index] = selected_answer

    if st.session_state["quiz_submitted"]:
        if selected_answer == item["answer"]:
            st.success(tr("✅ Correct answer!"))
        else:
            st.error(
                tr("❌ Not quite. Correct answer: ")
                + tr(item["options"][item["answer"]])
            )

        st.info(tr(item["explanation"]))

    st.markdown("---")

# Progress
answered_count = len(st.session_state["quiz_answers"])
st.progress(answered_count / len(questions))

st.caption(
    tr("Questions answered: ")
    + f"{answered_count}/{len(questions)}"
)

if not st.session_state["quiz_submitted"]:
    if st.button(
        tr("✅ Submit Quiz"),
        type="primary",
        use_container_width=True
    ):
        if answered_count < len(questions):
            st.warning(tr("Please answer every question before submitting."))
        else:
            st.session_state["quiz_submitted"] = True
            st.rerun()

# Results
if st.session_state["quiz_submitted"]:
    score = sum(
        1
        for index, item in enumerate(questions)
        if st.session_state["quiz_answers"].get(index) == item["answer"]
    )

    percentage = score / len(questions) * 100

    st.balloons()
    st.header(tr("🏆 Your Quiz Results"))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            tr("Score"),
            f"{score}/{len(questions)}"
        )

    with col2:
        st.metric(
            tr("Percentage"),
            f"{percentage:.1f}%"
        )

    with col3:
        st.metric(
            tr("Correct Answers"),
            f"{score}"
        )

    if percentage >= 80:
        st.success(
            tr("Excellent work! You understand many important financial safety habits.")
        )
    elif percentage >= 50:
        st.info(
            tr("Good effort! Review the explanations to strengthen your financial knowledge.")
        )
    else:
        st.warning(
            tr("Keep learning! Visit the Banking, UPI, Savings, Budget, and Fraud Safety pages and try again.")
        )

    # Topic-wise results
    topic_results = {}

    for index, item in enumerate(questions):
        topic = item["topic"]

        if topic not in topic_results:
            topic_results[topic] = {"correct": 0, "total": 0}

        topic_results[topic]["total"] += 1

        if st.session_state["quiz_answers"].get(index) == item["answer"]:
            topic_results[topic]["correct"] += 1

    st.subheader(tr("Topic-wise Performance"))

    for topic, result in topic_results.items():
        topic_percentage = result["correct"] / result["total"]
        st.write(
            f"**{tr(topic)}:** "
            f"{result['correct']}/{result['total']}"
        )
        st.progress(topic_percentage)

    st.markdown("---")

    st.subheader(tr("Keep Improving"))
    st.write(
        tr("Financial literacy improves with practice. "
           "Review the explanations, learn from mistakes, and repeat the quiz.")
    )

    if st.button(
        tr("🔄 Try Again"),
        use_container_width=True
    ):
        st.session_state["quiz_answers"] = {}
        st.session_state["quiz_submitted"] = False
        st.rerun()

st.markdown("---")

st.caption(
    tr("FinSaathi — Learn Finance. Stay Safe. "
       "This quiz is for educational purposes.")
)
