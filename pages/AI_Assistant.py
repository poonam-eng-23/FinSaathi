
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="AI Assistant - FinSaathi",
    page_icon="🤖",
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
    key="assistant_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

# AI Assistant page
st.title("🤖 " + tr("FinSaathi AI Assistant"))
st.write(
    tr("Ask questions about saving, banking, budgeting, and digital payment safety.")
)

st.info(
    "💡 " + tr(
        "This assistant provides general financial education. "
        "Never share your PIN, OTP, password, or bank account details."
    )
)

st.markdown("---")

st.subheader("💬 " + tr("Choose a question"))

suggestions = [
    "How can I save money?",
    "How do I open a bank account?",
    "How can I identify online scams?",
    "How can I use UPI safely?",
    "How can I make a monthly budget?"
]

selected_question = st.selectbox(
    tr("Select a question"),
    [tr(item) for item in suggestions]
)

if st.button("Ask Saathi", use_container_width=True):
    answers = {
        "How can I save money?": (
            "Start by setting a small savings goal. "
            "Record your spending and save regularly, even if the amount is small."
        ),
        "How do I open a bank account?": (
            "Visit a bank or its official website. Ask about account types, "
            "required documents, fees, and minimum balance rules."
        ),
        "How can I identify online scams?": (
            "Be cautious of urgent messages, suspicious links, prize claims, "
            "and requests for OTPs, PINs, or passwords. Verify through official channels."
        ),
        "How can I use UPI safely?": (
            "Check the recipient's name and payment amount before paying. "
            "Never share your UPI PIN. You do not need a PIN to receive money."
        ),
        "How can I make a monthly budget?": (
            "Write down your monthly income and expenses. Separate needs from wants, "
            "plan savings, and review your spending regularly."
        )
    }

    original_question = next(
        (
            item for item in suggestions
            if tr(item) == selected_question
        ),
        None
    )

    if original_question:
        st.subheader("📘 " + tr("Saathi's Answer"))
        st.write(tr(answers[original_question]))

st.markdown("---")

st.subheader("✍️ " + tr("Ask your own question"))

user_question = st.text_area(
    tr("Type your financial literacy question"),
    placeholder=tr("For example: How can I avoid UPI scams?")
)

if st.button("Get Guidance", use_container_width=True):
    if not user_question.strip():
        st.warning(tr("Please type a question first."))
    else:
        st.write(
            tr("Your question") + ": " + user_question
        )

        st.info(
            tr(
                "For this version, use the suggested questions above for "
                "prepared answers. Personalised AI responses require connecting "
                "a suitable AI service."
            )
        )

st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
