
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="AI Assistant | FinSaathi",
    page_icon="🤖",
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
    key="assistant_language"
)

if selected_language != st.session_state["language"]:
    st.session_state["language"] = selected_language
    st.query_params["language"] = selected_language
    st.rerun()

st.title(tr("🤖 Saathi - Your Financial Learning Assistant"))
st.subheader(tr("Ask questions. Learn money skills. Make safer decisions."))

st.info(
    tr("Saathi provides general financial education. "
       "It cannot access your bank account, make payments, or replace a qualified financial adviser.")
)

# Educational response system
def get_response(question):
    q = question.lower()

    if any(word in q for word in [
        "otp", "fraud", "scam", "cheated", "cybercrime",
        "cyber crime", "fake call", "phishing", "stolen money"
    ]):
        return (
            "🛡️ **Fraud safety**\n\n"
            "1. Never share your OTP, UPI PIN, ATM PIN, or password.\n"
            "2. Do not click suspicious links or install apps suggested by unknown callers.\n"
            "3. Verify requests through official bank channels.\n"
            "4. If money is lost to financial cyber fraud in India, call **1930** promptly "
            "and report it at https://cybercrime.gov.in/.\n"
            "5. Contact your bank immediately about unauthorised transactions."
        )

    if any(word in q for word in [
        "upi", "google pay", "phonepe", "payment", "qr code",
        "send money", "receive money"
    ]):
        return (
            "📱 **UPI safety and payments**\n\n"
            "• Check the recipient's name and amount before paying.\n"
            "• Enter your UPI PIN only when authorising a payment in your trusted UPI app.\n"
            "• You generally do not need a UPI PIN to receive money.\n"
            "• Never approve an unexpected collect request.\n"
            "• Check your app's transaction history before trying a failed payment again."
        )

    if any(word in q for word in [
        "save", "saving", "savings", "emergency fund", "saving money"
    ]):
        return (
            "💰 **How to build savings**\n\n"
            "1. Set a clear goal, such as education expenses or emergencies.\n"
            "2. Record your income and regular expenses.\n"
            "3. Decide on an affordable amount to save regularly.\n"
            "4. Keep emergency money accessible and separate from everyday spending.\n"
            "5. Compare account fees, withdrawal rules, and risks before choosing a product.\n\n"
            "**Example:** If you receive ₹2,000 in a month and can comfortably save ₹200, "
            "you would save ₹2,400 over 12 months, excluding interest."
        )

    if any(word in q for word in [
        "budget", "allowance", "expenses", "spending",
        "monthly income", "manage money"
    ]):
        return (
            "📊 **Make a simple budget**\n\n"
            "1. Write down your monthly income or allowance.\n"
            "2. List necessary expenses first.\n"
            "3. Set a realistic savings target.\n"
            "4. Keep a limit for optional spending.\n"
            "5. Compare planned spending with actual spending at the end of each week.\n\n"
            "**Example:** With ₹5,000 available, you might plan ₹3,000 for needs, "
            "₹1,000 for savings, and ₹1,000 for optional expenses. Adjust these amounts "
            "to suit your real responsibilities."
        )

    if any(word in q for word in [
        "bank account", "open account", "banking", "passbook",
        "atm", "debit card"
    ]):
        return (
            "🏦 **Banking basics**\n\n"
            "• Choose a bank and account suitable for your needs.\n"
            "• Ask the bank about required documents, minimum balance, and fees.\n"
            "• Submit the official application and complete identity verification.\n"
            "• Keep your passbook and transaction records safe.\n"
            "• Never share your ATM PIN, OTP, or online banking password.\n\n"
            "Official information: https://www.rbi.org.in/"
        )

    if any(word in q for word in [
        "interest", "simple interest", "compound interest"
    ]):
        return (
            "📈 **Understanding interest**\n\n"
            "Interest is money earned on savings or paid when borrowing.\n\n"
            "**Simple interest formula:**\n"
            "Interest = Principal × Rate × Time ÷ 100\n\n"
            "**Example:** ₹1,000 at 5% simple interest per year for 2 years:\n"
            "₹1,000 × 5 × 2 ÷ 100 = ₹100 interest.\n\n"
            "The total would be ₹1,100, assuming the stated rate and no fees or other changes."
        )

    if any(word in q for word in [
        "loan", "borrow", "debt", "emi", "lending"
    ]):
        return (
            "💳 **Borrowing safely**\n\n"
            "• Compare the interest rate, fees, repayment period, and total repayment.\n"
            "• Borrow only an amount you reasonably expect to repay.\n"
            "• Read the agreement before accepting a loan.\n"
            "• Avoid lenders who demand suspicious advance fees or access to your contacts.\n"
            "• Never share an OTP or banking PIN with a loan agent."
        )

    if any(word in q for word in [
        "government scheme", "jan dhan", "pmjdy", "insurance",
        "pension", "subsidy"
    ]):
        return (
            "🇮🇳 **Government financial schemes**\n\n"
            "You can learn about banking access, insurance, pensions, and small-savings schemes "
            "through official government sources.\n\n"
            "• Jan Dhan and banking information: https://pmjdy.gov.in/\n"
            "• Public information from RBI: https://www.rbi.org.in/\n"
            "• Post Office savings information: https://www.indiapost.gov.in/\n\n"
            "Eligibility and benefits vary by scheme. Confirm the latest rules through official sources."
        )

    if any(word in q for word in [
        "invest", "investment", "stock", "share market", "mutual fund"
    ]):
        return (
            "📚 **Investment basics**\n\n"
            "• Learn about risk, returns, fees, and the possibility of losing money.\n"
            "• Be suspicious of guaranteed high returns.\n"
            "• Do not invest money you need immediately for essential expenses.\n"
            "• Verify investment providers through official regulatory sources.\n\n"
            "Investor education: https://investor.sebi.gov.in/\n\n"
            "This is general education, not a recommendation to buy a particular investment."
        )

    if any(word in q for word in [
        "hello", "hi", "hey", "namaste", "ನಮಸ್ಕಾರ"
    ]):
        return (
            "👋 Hello! I am Saathi, your financial learning helper.\n\n"
            "You can ask me about saving money, banking, budgeting, UPI safety, "
            "loans, interest, investments, or financial scams."
        )

    return (
        "I can help you learn about everyday financial topics.\n\n"
        "Try asking one of these questions:\n"
        "• How can I save money every month?\n"
        "• How do I identify a UPI scam?\n"
        "• What is simple interest?\n"
        "• How can I create a budget?\n"
        "• How do I open a bank account?\n\n"
        "For a question outside these topics, consult an appropriate official source "
        "or qualified professional."
    )


# Suggested questions
st.markdown("### " + tr("💡 Try asking Saathi"))

suggestions = [
    "How can I save money every month?",
    "How do I identify a UPI scam?",
    "What is simple interest?",
    "How can I create a budget?",
    "How do I open a bank account?",
    "How can I borrow money safely?"
]

columns = st.columns(2)

for index, suggestion in enumerate(suggestions):
    with columns[index % 2]:
        if st.button(tr(suggestion), key=f"assistant_suggestion_{index}",
                     use_container_width=True):
            st.session_state["saathi_question"] = suggestion

st.markdown("---")

# Chat history
if "saathi_messages" not in st.session_state:
    st.session_state["saathi_messages"] = []

for item in st.session_state["saathi_messages"]:
    with st.chat_message(item["role"]):
        st.markdown(tr(item["content"]))

question = st.chat_input(tr("Ask Saathi a financial question..."))

if st.session_state.get("saathi_question"):
    question = st.session_state.pop("saathi_question")

if question:
    st.session_state["saathi_messages"].append(
        {"role": "user", "content": question}
    )

    answer = get_response(question)

    st.session_state["saathi_messages"].append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()

if st.session_state["saathi_messages"]:
    if st.button(tr("🗑️ Clear conversation"), key="clear_saathi_chat"):
        st.session_state["saathi_messages"] = []
        st.rerun()

st.markdown("---")

# Quick learning cards
st.header(tr("📘 Quick Financial Lessons"))

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(tr("💰 Save"))
    st.write(tr("Set a realistic savings goal and review your progress regularly."))

with col2:
    st.subheader(tr("🔐 Protect"))
    st.write(tr("Keep your PINs, passwords, and OTPs private."))

with col3:
    st.subheader(tr("📊 Plan"))
    st.write(tr("Track income and expenses to make informed spending decisions."))

st.markdown("---")

st.caption(
    tr("FinSaathi — Learn Finance. Stay Safe. "
       "Educational information only; verify important decisions with official sources.")
)
