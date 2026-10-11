
import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi - Budget",
    page_icon="📊",
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

# Budget page
st.title("📊 " + t("My Monthly Budget"))

st.write(
    t("Plan your money, manage expenses and set realistic savings goals.")
)

st.info(
    t("A budget is a plan for how you will use your available money.")
)

st.divider()

# Monthly income
st.header("💰 " + t("Monthly Income"))

income = st.number_input(
    t("Enter your monthly income or allowance (₹)"),
    min_value=0,
    max_value=10000000,
    value=5000,
    step=500,
    key="budget_income"
)

st.divider()

# Budget allocation
st.header("🧮 " + t("Choose a Budget Plan"))

plan = st.selectbox(
    t("Budget allocation"),
    [
        "50/30/20",
        "60/20/20",
        "70/20/10"
    ],
    key="budget_plan"
)

if plan == "50/30/20":
    needs_pct = 50
    wants_pct = 30
    savings_pct = 20
elif plan == "60/20/20":
    needs_pct = 60
    wants_pct = 20
    savings_pct = 20
else:
    needs_pct = 70
    wants_pct = 20
    savings_pct = 10

needs_amount = income * needs_pct / 100
wants_amount = income * wants_pct / 100
savings_amount = income * savings_pct / 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        t("Needs"),
        f"₹{needs_amount:,.2f}",
        f"{needs_pct}%"
    )

with col2:
    st.metric(
        t("Wants"),
        f"₹{wants_amount:,.2f}",
        f"{wants_pct}%"
    )

with col3:
    st.metric(
        t("Savings"),
        f"₹{savings_amount:,.2f}",
        f"{savings_pct}%"
    )

st.caption(
    t("These percentages are examples. Adjust them to your actual "
      "income, essential expenses and circumstances.")
)

st.divider()

# Expense tracker
st.header("🧾 " + t("Expense Planner"))

st.write(
    t("Enter an expense to see how it compares with your available budget.")
)

expense_name = st.text_input(
    t("Expense name"),
    placeholder="Example: Travel or books",
    key="budget_expense_name"
)

expense_category = st.selectbox(
    t("Expense category"),
    [
        "Needs",
        "Wants",
        "Savings",
        "Other"
    ],
    key="budget_expense_category"
)

expense_amount = st.number_input(
    t("Expense amount (₹)"),
    min_value=0,
    max_value=10000000,
    value=0,
    step=100,
    key="budget_expense_amount"
)

if "budget_expenses" not in st.session_state:
    st.session_state["budget_expenses"] = []

if st.button(t("Add Expense"), use_container_width=True):
    if not expense_name.strip():
        st.warning(t("Please enter an expense name."))
    elif expense_amount <= 0:
        st.warning(t("Please enter an amount greater than zero."))
    else:
        st.session_state["budget_expenses"].append({
            "name": expense_name.strip(),
            "category": expense_category,
            "amount": float(expense_amount)
        })
        st.success(t("Expense added successfully."))

expenses = st.session_state["budget_expenses"]

if expenses:
    st.subheader(t("Your Expenses"))

    total_expenses = sum(item["amount"] for item in expenses)

    st.metric(
        t("Total recorded expenses"),
        f"₹{total_expenses:,.2f}"
    )

    for index, item in enumerate(expenses):
        expense_col, delete_col = st.columns([4, 1])

        with expense_col:
            st.write(
                f"**{item['name']}** — {item['category']}: "
                f"₹{item['amount']:,.2f}"
            )

        with delete_col:
            if st.button("🗑️", key=f"delete_budget_expense_{index}"):
                st.session_state["budget_expenses"].pop(index)
                st.rerun()

    remaining = income - total_expenses

    st.metric(
        t("Income remaining after recorded expenses"),
        f"₹{remaining:,.2f}"
    )

    if remaining < 0:
        st.warning(
            t("Your recorded expenses exceed your entered income. "
              "Review your budget.")
        )
else:
    st.caption(t("No expenses added yet."))

st.divider()

# Budget tips
st.header("💡 " + t("Budgeting Tips"))

st.markdown(
    "- Write down your income and regular expenses.\n"
    "- Prioritise food, housing, education and other essential needs.\n"
    "- Set realistic savings goals.\n"
    "- Review spending before making non-essential purchases.\n"
    "- Avoid borrowing money without understanding the repayment terms."
)

st.divider()

if st.button("🏠 " + t("Home"), use_container_width=True):
    st.switch_page("app.py")

st.caption("💙 FinSaathi — " + t("Learn Finance. Stay Safe."))
