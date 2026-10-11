
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="AI Assistant - FinSaathi",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 FinSaathi AI Assistant")
st.write("Ask questions about banking, savings, budgeting, and fraud safety.")

st.markdown("---")

st.subheader("Choose a question")

suggestions = {
    "How can I save money?": (
        "Start by tracking your expenses, setting a realistic goal, "
        "and saving a manageable amount regularly."
    ),
    "How can I stay safe from UPI fraud?": (
        "Never share your UPI PIN or OTP. Verify the recipient before "
        "paying, and remember that receiving money does not require "
        "entering your UPI PIN."
    ),
    "What is a savings account?": (
        "A savings account is a bank account used to keep money safely. "
        "Depending on the account, the bank may pay interest."
    ),
    "How can I plan a budget?": (
        "List your income and expenses, separate needs from wants, "
        "and set a savings goal that suits your situation."
    )
}

selected_question = st.selectbox(
    "Select a suggested question",
    ["Choose a question..."] + list(suggestions.keys())
)

if selected_question != "Choose a question...":
    st.info(suggestions[selected_question])

st.markdown("---")

st.subheader("Ask your own question")

user_question = st.text_area(
    "Type your financial question",
    placeholder="For example: How do I open a bank account?"
)

if st.button("Get Guidance"):
    if not user_question.strip():
        st.warning("Please type a question first.")
    else:
        st.info(
            "Your question: " + user_question
        )
        st.write(
            "For reliable guidance, check your bank's official website "
            "or contact an authorized banking representative. "
            "Never share your PIN, OTP, or password."
        )

st.caption(
    "This is a basic educational assistant with suggested answers. "
    "It is not connected to a live AI service."
)

st.markdown("---")
st.caption("FinSaathi — Learn Finance. Stay Safe.")
