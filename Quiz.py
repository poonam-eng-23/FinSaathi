import streamlit as st

st.set_page_config(
    page_title="Financial Quiz - FinSaathi",
    page_icon="📝"
)

st.title("📝 Financial Quiz")
st.subheader("Learn finance by answering simple questions")

st.write("Choose the correct answer for each question.")

st.divider()

score = 0

q1 = st.radio(
    "1. What should you never share with anyone?",
    ["Your name", "OTP or UPI PIN", "Your favourite color", "Your city"]
)

q2 = st.radio(
    "2. What is saving?",
    [
        "Spending all your money",
        "Keeping some money for future needs",
        "Borrowing money",
        "Giving away your money"
    ]
)

q3 = st.radio(
    "3. What does UPI help us do?",
    [
        "Cook food",
        "Make digital payments",
        "Drive a vehicle",
        "Print documents"
    ]
)

q4 = st.radio(
    "4. What should you do with a suspicious link?",
    [
        "Click immediately",
        "Share it with everyone",
        "Avoid clicking and verify it",
        "Enter your PIN"
    ]
)

q5 = st.radio(
    "5. What is a budget used for?",
    [
        "Planning income and expenses",
        "Playing games",
        "Sending messages",
        "Watching videos"
    ]
)

st.divider()

if st.button("✅ Submit Quiz"):

    if q1 == "OTP or UPI PIN":
        score += 1

    if q2 == "Keeping some money for future needs":
        score += 1

    if q3 == "Make digital payments":
        score += 1

    if q4 == "Avoid clicking and verify it":
        score += 1

    if q5 == "Planning income and expenses":
        score += 1

    st.header("🏆 Your Result")

    st.success(f"You scored {score} out of 5!")

    if score == 5:
        st.balloons()
        st.success("Excellent! 🎉 You have a good understanding of basic financial safety.")

    elif score >= 3:
        st.info("Good job! 👍 Keep learning about financial safety.")

    else:
        st.warning("Keep learning! 📚 You can try the quiz again.")

st.divider()

st.warning(
    "🛡️ Remember: Never share your OTP, UPI PIN, ATM PIN or password."
)

st.caption("FinSaathi – Learn Finance. Stay Safe. 💰")