
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Savings - FinSaathi",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Savings")
st.write("Learn how to save money and build good financial habits.")

st.markdown("---")

st.subheader("Why is saving money important?")
st.write(
    "Saving helps you prepare for emergencies, meet future goals, "
    "and avoid borrowing money unnecessarily."
)

st.subheader("Simple ways to save money")

st.markdown("""
1. Set a small savings goal.
2. Save a part of the money you receive.
3. Write down your expenses.
4. Avoid unnecessary purchases.
5. Keep your savings in a safe place, such as a bank account.
""")

st.subheader("Example: Monthly Savings")

income = st.number_input(
    "Monthly money received (₹)",
    min_value=0,
    value=1000,
    step=100
)

expenses = st.number_input(
    "Monthly expenses (₹)",
    min_value=0,
    value=700,
    step=100
)

if st.button("Calculate Savings"):
    savings = income - expenses

    if savings > 0:
        st.success(f"You could save ₹{savings} this month.")
    elif savings == 0:
        st.info("Your income and expenses are equal.")
    else:
        st.warning(
            f"Your expenses exceed your income by ₹{abs(savings)}."
        )

st.subheader("Savings Tips")
st.info(
    "Start with an amount that suits your situation. "
    "Even small, regular savings can help over time."
)

st.markdown("---")
st.caption("FinSaathi — Learn Finance. Stay Safe.")
