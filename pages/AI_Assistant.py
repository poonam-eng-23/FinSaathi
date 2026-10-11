
import streamlit as st
from translation import tr

st.set_page_config(
    page_title="FinSaathi - AI Assistant",
    page_icon="🤖",
    layout="wide"
)

def t(text):
    return tr(text)

if "language" not in st.session_state:
    st.session_state["language"] = "English"

st.title(t("🤖 Saathi - Your Financial Assistant"))

st.write(
    t("Ask questions about banking, savings, budgeting, UPI and online fraud safety.")
)

st.info(
    t("Educational assistant: never share your PIN, password, OTP or bank details.")
)

st.divider()

st.subheader(t("What would you like to learn?"))

suggestions = [
    "How can I save money?",
    "What is UPI?",
    "How can I identify online fraud?",
    "What is a bank account?",
    "How can I make a monthly budget?",
    "What should I do if I receive a suspicious message?"
]

cols = st.columns(2)

for i, suggestion in enumerate(suggestions):
    with cols[i % 2]:
        if st.button(t(suggestion), key=f"suggestion_{i}", use_container_width=True):
            st.session_state["assistant_question"] = suggestion

question = st.text_area(
    t("Type your question here"),
    key="assistant_question",
    height=100,
    placeholder=t("Example: How can I protect my bank account?")
)

def get_answer(text):
    q = text.lower()

    if any(word in q for word in ["otp", "pin", "password", "secret"]):
        return (
            "Never share your OTP, UPI PIN, ATM PIN or password with anyone. "
            "Bank staff will not ask you to reveal these secrets. "
            "Enter your UPI PIN only in your trusted payment app when you are making a payment."
        )

    if any(word in q for word in ["fraud", "scam", "fake", "suspicious", "phishing", "cheat", "link", "message"]):
        return (
            "Be careful with unexpected calls, messages and links. "
            "Do not click suspicious links or share OTPs or PINs. "
            "Verify requests through your bank's official app or phone number. "
            "If you suspect financial cyber fraud in India, contact your bank promptly "
            "and report it through the official cybercrime helpline 1930 or cybercrime.gov.in."
        )

    if any(word in q for word in ["upi", "payment", "receive money", "gpay", "phonepe", "paytm"]):
        return (
            "UPI lets you transfer money between bank accounts using a supported payment app. "
            "Check the receiver's name and amount before paying. "
            "You do not need to enter your UPI PIN just to receive money. "
            "Never approve an unexpected collect request without checking it."
        )

    if any(word in q for word in ["save", "saving", "savings", "future", "goal"]):
        return (
            "Start by deciding what you are saving for. "
            "Set aside an affordable amount regularly, track your spending and keep emergency "
            "money separate when possible. Choose a suitable, regulated bank savings option "
            "and understand its terms before using it."
        )

    if any(word in q for word in ["budget", "expense", "spend", "income", "allowance", "money left"]):
        return (
            "A budget is a plan for your income and expenses. "
            "Write down your income, list essential expenses, set a limit for optional spending "
            "and decide how much you can save. Review your spending regularly and adjust the plan "
            "when your needs change."
        )

    if any(word in q for word in ["bank", "account", "atm", "passbook", "debit card"]):
        return (
            "A bank account helps you keep money safely and make deposits or payments. "
            "Ask a regulated bank about suitable account types, required documents, fees and "
            "minimum-balance rules. Keep your ATM card and banking credentials secure."
        )

    if any(word in q for word in ["loan", "borrow", "interest", "emi"]):
        return (
            "Before taking a loan, compare the interest rate, processing fees, repayment amount "
            "and due dates. Borrow only what you can reasonably repay. Avoid unknown lenders "
            "who demand advance fees or ask for sensitive banking information."
        )

    if any(word in q for word in ["hello", "hi", "namaste", "ನಮಸ್ಕಾರ", "ನಮಸ್ತೆ"]):
        return (
            "Hello! I am Saathi, your financial learning assistant. "
            "You can ask me about banking, savings, budgeting, UPI and fraud prevention."
        )

    return (
        "I can help with basic banking, UPI payments, savings, budgeting, loans and fraud safety. "
        "Please ask a specific question about one of these topics. "
        "For personal financial decisions, verify important details with your bank or a qualified adviser."
    )

if st.button(t("Ask Saathi"), use_container_width=True):
    if question.strip():
        answer = get_answer(question)
        st.session_state["assistant_last_question"] = question
        st.session_state["assistant_last_answer"] = answer
    else:
        st.warning(t("Please type a question first."))

if "assistant_last_answer" in st.session_state:
    st.divider()
    st.subheader(t("Saathi's Answer"))
    st.write(t(st.session_state["assistant_last_answer"]))

st.caption(
    t("Note: This is a basic rule-based educational assistant, not a live AI model.")
)

st.divider()
st.caption(t("FinSaathi — Learn Finance. Stay Safe. 💙"))

if st.button(t("🏠 Home"), use_container_width=True):
    st.switch_page("app.py")
