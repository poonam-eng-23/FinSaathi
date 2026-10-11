
import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi - AI Assistant",
    page_icon="🤖",
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

# AI Assistant page
st.title("🤖 " + t("Meet Saathi"))

st.write(
    t("Your friendly guide to learning everyday financial skills.")
)

st.info(
    t("Saathi provides basic financial education. Never share your "
      "OTP, PIN, password or complete bank account details here.")
)

# Suggested questions
st.header("💡 " + t("Choose a Question"))

suggestions = {
    "Banking": "How can I open a bank account?",
    "Savings": "How can I start saving money?",
    "UPI Safety": "How can I use UPI safely?",
    "Fraud": "How can I recognise a financial scam?",
    "Budget": "How can I make a monthly budget?"
}

selected_topic = st.selectbox(
    t("Select a topic"),
    list(suggestions.keys()),
    key="assistant_topic"
)

if st.button(t("Ask Saathi"), use_container_width=True):
    st.session_state["assistant_question"] = suggestions[selected_topic]

# Question input
st.header("💬 " + t("Ask Your Question"))

question = st.text_input(
    t("Type your financial question"),
    placeholder="Example: How can I save money every month?",
    key="assistant_question_input"
)

if st.button(t("Get Answer"), use_container_width=True):
    if not question.strip():
        st.warning(t("Please enter a question first."))
    else:
        q = question.lower()

        if any(word in q for word in ["bank", "account", "atm"]):
            answer = (
                "A bank account helps you keep money safe, receive "
                "payments and make transactions. Ask a bank about "
                "account options and required documents. Never share "
                "your PIN or OTP."
            )

        elif any(word in q for word in ["save", "saving", "savings"]):
            answer = (
                "Start by choosing a realistic goal. Track your income "
                "and expenses, then save a manageable amount regularly "
                "when possible. Keep emergency needs in mind."
            )

        elif any(word in q for word in ["upi", "payment", "pin"]):
            answer = (
                "Use a trusted UPI app, check the recipient and amount, "
                "and enter your UPI PIN only to authorise a payment. "
                "You do not need a UPI PIN to receive money."
            )

        elif any(word in q for word in ["fraud", "scam", "otp", "fake"]):
            answer = (
                "Never share an OTP, PIN or password. Avoid unknown "
                "links and unexpected payment requests. Verify with "
                "your bank through official contact details."
            )

        elif any(word in q for word in ["budget", "expense", "spend", "money"]):
            answer = (
                "Write down your expected income and necessary expenses. "
                "Plan for needs first, set a realistic savings goal, "
                "and review your spending regularly."
            )

        else:
            answer = (
                "I can help with basic banking, savings, budgeting, "
                "UPI safety and scam awareness. Try asking about one "
                "of these topics. This assistant uses simple topic-based "
                "responses and does not understand every question."
            )

        st.session_state["assistant_answer"] = answer

if "assistant_answer" in st.session_state:
    st.subheader("📘 " + t("Saathi's Answer"))
    st.write(st.session_state["assistant_answer"])

st.divider()

st.caption(
    t("Educational information only. For account-specific issues, "
      "contact your bank through official channels.")
)

if st.button("🏠 " + t("Home"), use_container_width=True):
    st.switch_page("app.py")

st.caption("💙 FinSaathi — " + t("Learn Finance. Stay Safe."))
