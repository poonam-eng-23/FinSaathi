
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Budget Planner - FinSaathi",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Budget Planner")
st.write("Plan your monthly money and understand where it goes.")

st.markdown("---")

st.subheader("Enter Your Monthly Income")

income = st.number_input(
    "Monthly income or allowance (₹)",
    min_value=0.0,
    value=5000.0,
    step=500.0
)

st.subheader("Choose a Budget Plan")

budget_plan = st.selectbox(
    "Select your preferred plan",
    [
        "50/30/20 — Needs, Wants, Savings",
        "60/20/20 — Needs, Wants, Savings",
        "70/20/10 — Needs, Wants, Savings"
    ]
)

if budget_plan.startswith("50"):
    needs_percent, wants_percent, savings_percent = 50, 30, 20
elif budget_plan.startswith("60"):
    needs_percent, wants_percent, savings_percent = 60, 20, 20
else:
    needs_percent, wants_percent, savings_percent = 70, 20, 10

needs = income * needs_percent / 100
wants = income * wants_percent / 100
savings = income * savings_percent / 100

st.markdown("---")
st.subheader("Your Suggested Monthly Budget")

col1, col2, col3 = st.columns(3)

col1.metric("Needs", f"₹{needs:.2f}")
col2.metric("Wants", f"₹{wants:.2f}")
col3.metric("Savings", f"₹{savings:.2f}")

st.write(f"**Needs:** {needs_percent}% for essential expenses.")
st.write(f"**Wants:** {wants_percent}% for non-essential spending.")
st.write(f"**Savings:** {savings_percent}% towards your savings goals.")

st.markdown("---")
st.subheader("Track Your Expenses")

expense_name = st.text_input(
    "Expense name",
    placeholder="For example: Bus fare"
)

expense_amount = st.number_input(
    "Expense amount (₹)",
    min_value=0.0,
    value=0.0,
    step=10.0
)

if "budget_expenses" not in st.session_state:
    st.session_state.budget_expenses = []

if st.button("Add Expense"):
    if expense_name.strip() and expense_amount > 0:
        st.session_state.budget_expenses.append(
            {
                "name": expense_name.strip(),
                "amount": expense_amount
            }
        )
        st.success("Expense added!")
    else:
        st.warning("Enter an expense name and an amount greater than zero.")

total_expenses = sum(
    item["amount"] for item in st.session_state.budget_expenses
)

st.subheader("Expense Summary")
st.metric("Total expenses entered", f"₹{total_expenses:.2f}")
st.metric("Income left after entered expenses", f"₹{income - total_expenses:.2f}")

if st.session_state.budget_expenses:
    for index, item in enumerate(st.session_state.budget_expenses):
        st.write(f"{index + 1}. {item['name']} — ₹{item['amount']:.2f}")

    if st.button("Clear All Expenses"):
        st.session_state.budget_expenses = []
        st.rerun()
else:
    st.info("No expenses have been added yet.")

st.caption(
    "Budget percentages are suggestions. Adjust your plan to suit your needs."
)

st.markdown("---")
st.caption("FinSaathi — Learn Finance. Stay Safe.")
