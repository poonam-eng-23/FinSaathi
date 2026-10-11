
import streamlit as st
from translation import tr

st.set_page_config(
    page_title="FinSaathi - Budget",
    page_icon="💰",
    layout="wide"
)

def t(text):
    return tr(text)

if "language" not in st.session_state:
    st.session_state["language"] = "English"

st.title(t("💰 Budget Planner"))
st.write(t("Plan your money wisely and build better saving habits."))

st.divider()

st.subheader(t("Monthly Budget"))

income = st.number_input(
    t("Enter your monthly income or allowance (₹)"),
    min_value=0.0,
    value=5000.0,
    step=500.0
)

st.subheader(t("Choose Your Budget Rule"))

budget_rule = st.selectbox(
    t("Select a budget plan"),
    [
        "50/30/20 Rule",
        "60/20/20 Rule",
        "70/20/10 Rule"
    ],
    format_func=t
)

if budget_rule == "50/30/20 Rule":
    needs_percent = 50
    wants_percent = 30
    savings_percent = 20
elif budget_rule == "60/20/20 Rule":
    needs_percent = 60
    wants_percent = 20
    savings_percent = 20
else:
    needs_percent = 70
    wants_percent = 20
    savings_percent = 10

needs_amount = income * needs_percent / 100
wants_amount = income * wants_percent / 100
savings_amount = income * savings_percent / 100

st.divider()
st.subheader(t("Your Suggested Budget"))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        t("Needs"),
        f"₹{needs_amount:,.2f}",
        f"{needs_percent}%"
    )
    st.caption(t("Food, travel, bills and essentials"))

with col2:
    st.metric(
        t("Wants"),
        f"₹{wants_amount:,.2f}",
        f"{wants_percent}%"
    )
    st.caption(t("Entertainment and non-essential purchases"))

with col3:
    st.metric(
        t("Savings"),
        f"₹{savings_amount:,.2f}",
        f"{savings_percent}%"
    )
    st.caption(t("Money kept for future needs"))

st.divider()
st.subheader(t("Calculate Your Actual Expenses"))

food = st.number_input(
    t("Food expenses (₹)"),
    min_value=0.0,
    value=0.0,
    step=100.0
)

travel = st.number_input(
    t("Travel expenses (₹)"),
    min_value=0.0,
    value=0.0,
    step=100.0
)

bills = st.number_input(
    t("Bills and education (₹)"),
    min_value=0.0,
    value=0.0,
    step=100.0
)

other = st.number_input(
    t("Other expenses (₹)"),
    min_value=0.0,
    value=0.0,
    step=100.0
)

total_expenses = food + travel + bills + other
remaining = income - total_expenses

st.metric(
    t("Total Expenses"),
    f"₹{total_expenses:,.2f}"
)

st.metric(
    t("Money Left"),
    f"₹{remaining:,.2f}"
)

if remaining > 0:
    st.success(
        t("You have money left. Consider saving some of it.")
    )
elif remaining == 0:
    st.info(
        t("Your entire budget has been used. Plan for savings next month.")
    )
else:
    st.warning(
        t("Your expenses are higher than your income. Review your spending.")
    )

st.divider()
st.subheader(t("Smart Saving Tips"))

tips = [
    "Save a small amount regularly.",
    "Write down your daily expenses.",
    "Avoid unnecessary purchases.",
    "Never share your ATM PIN or UPI PIN.",
    "Keep emergency savings for unexpected needs."
]

for tip in tips:
    st.write("💡 " + t(tip))

st.divider()
st.caption(t("FinSaathi — Learn Finance. Stay Safe. 💙"))

if st.button(t("🏠 Home"), use_container_width=True):
    st.switch_page("app.py")
