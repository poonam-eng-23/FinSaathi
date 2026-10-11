
import streamlit as st
import pandas as pd
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Budget Planner | FinSaathi",
    page_icon="💰",
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
    key="budget_language"
)

if selected_language != st.session_state["language"]:
    st.session_state["language"] = selected_language
    st.query_params["language"] = selected_language
    st.rerun()

st.title(tr("💰 Smart Budget Planner"))
st.subheader(tr("Plan your income, manage expenses, and build savings."))

st.info(
    tr("A budget is a plan for how you will use the money available to you. "
       "Your needs and responsibilities may differ from the examples below.")
)

# 1. Monthly income
st.header(tr("1. Enter Your Monthly Income"))

income = st.number_input(
    tr("Total monthly income or allowance (₹)"),
    min_value=0.0,
    max_value=10000000.0,
    value=5000.0,
    step=500.0,
    key="budget_income"
)

other_income = st.number_input(
    tr("Other monthly income (₹)"),
    min_value=0.0,
    max_value=10000000.0,
    value=0.0,
    step=100.0,
    key="budget_other_income"
)

total_income = income + other_income

st.metric(tr("Total money available"), f"₹{total_income:,.2f}")

st.markdown("---")

# 2. Choose a budget rule
st.header(tr("2. Choose a Budget Plan"))

plan = st.selectbox(
    tr("Select a suggested allocation"),
    [
        "50/30/20: Needs / Wants / Savings",
        "60/20/20: Needs / Wants / Savings",
        "70/20/10: Needs / Wants / Savings",
        "Custom percentages"
    ],
    key="budget_plan"
)

if plan.startswith("50/30/20"):
    needs_pct, wants_pct, savings_pct = 50, 30, 20
elif plan.startswith("60/20/20"):
    needs_pct, wants_pct, savings_pct = 60, 20, 20
elif plan.startswith("70/20/10"):
    needs_pct, wants_pct, savings_pct = 70, 20, 10
else:
    needs_pct = st.slider(
        tr("Needs (%)"), 0, 100, 50, key="custom_needs"
    )
    wants_pct = st.slider(
        tr("Wants (%)"), 0, 100, 30, key="custom_wants"
    )
    savings_pct = st.slider(
        tr("Savings (%)"), 0, 100, 20, key="custom_savings"
    )

percentage_total = needs_pct + wants_pct + savings_pct

st.write(
    tr("Allocation total: ") + f"{percentage_total}%"
)

if percentage_total != 100:
    st.warning(
        tr("Your percentages should total 100%. Adjust the values before using this plan.")
    )

needs_budget = total_income * needs_pct / 100
wants_budget = total_income * wants_pct / 100
savings_budget = total_income * savings_pct / 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(tr("Needs budget"), f"₹{needs_budget:,.2f}")

with col2:
    st.metric(tr("Wants budget"), f"₹{wants_budget:,.2f}")

with col3:
    st.metric(tr("Savings target"), f"₹{savings_budget:,.2f}")

st.caption(
    tr("Needs include essentials such as food, transport, and required bills. "
       "Wants are optional purchases. Savings depend on your circumstances.")
)

st.markdown("---")

# 3. Record expenses
st.header(tr("3. Enter Your Monthly Expenses"))

st.write(
    tr("Enter the amount you expect to spend in each category. "
       "You can change these amounts to match your real situation.")
)

expense_categories = [
    "Food and groceries",
    "Transport",
    "Education",
    "Housing and bills",
    "Healthcare",
    "Mobile and internet",
    "Shopping and entertainment",
    "Family responsibilities",
    "Other expenses"
]

expense_values = {}

col1, col2 = st.columns(2)

for index, category in enumerate(expense_categories):
    with (col1 if index % 2 == 0 else col2):
        expense_values[category] = st.number_input(
            tr(category) + " (₹)",
            min_value=0.0,
            max_value=10000000.0,
            value=0.0,
            step=100.0,
            key=f"budget_expense_{index}"
        )

total_expenses = sum(expense_values.values())
balance = total_income - total_expenses

st.markdown("---")

# 4. Budget summary
st.header(tr("4. Your Budget Summary"))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(tr("Monthly income"), f"₹{total_income:,.2f}")

with col2:
    st.metric(tr("Planned expenses"), f"₹{total_expenses:,.2f}")

with col3:
    st.metric(
        tr("Money remaining"),
        f"₹{balance:,.2f}",
        delta=f"₹{balance:,.2f}"
    )

if total_income == 0 and total_expenses > 0:
    st.error(tr("Your expenses are greater than your available income. Review your plan."))
elif balance < 0:
    st.error(
        tr("Your planned expenses exceed your income. "
           "Review optional expenses where possible. Avoid cutting essential needs.")
    )
elif balance == 0 and total_income > 0:
    st.warning(
        tr("Your entire income is allocated. Consider whether you can make room for emergency savings.")
    )
elif total_income > 0:
    st.success(
        tr("Your planned expenses fit within your available income.")
    )

if total_income > 0:
    st.progress(min(total_expenses / total_income, 1.0))
    st.caption(
        tr("Share of income allocated to expenses: ")
        + f"{total_expenses / total_income * 100:.1f}%"
    )

# Expense breakdown
if total_expenses > 0:
    chart_data = pd.DataFrame({
        tr("Category"): [tr(c) for c, v in expense_values.items() if v > 0],
        tr("Amount (₹)"): [v for v in expense_values.values() if v > 0]
    })

    st.subheader(tr("Expense Breakdown"))
    st.bar_chart(
        chart_data.set_index(tr("Category"))
    )

    st.dataframe(
        chart_data,
        use_container_width=True,
        hide_index=True
    )
else:
    st.info(tr("Enter some expenses to see your spending breakdown."))

st.markdown("---")

# 5. Compare planned categories
st.header(tr("5. Compare Spending with Your Plan"))

needs_categories = [
    "Food and groceries",
    "Transport",
    "Education",
    "Housing and bills",
    "Healthcare",
    "Family responsibilities",
    "Other expenses"
]

wants_categories = [
    "Shopping and entertainment",
    "Mobile and internet"
]

needs_spent = sum(expense_values[c] for c in needs_categories)
wants_spent = sum(expense_values[c] for c in wants_categories)

comparison = [
    {
        tr("Category"): tr("Needs"),
        tr("Suggested budget (₹)"): needs_budget,
        tr("Entered expenses (₹)"): needs_spent,
        tr("Remaining (₹)"): needs_budget - needs_spent
    },
    {
        tr("Category"): tr("Wants"),
        tr("Suggested budget (₹)"): wants_budget,
        tr("Entered expenses (₹)"): wants_spent,
        tr("Remaining (₹)"): wants_budget - wants_spent
    },
    {
        tr("Category"): tr("Savings"),
        tr("Suggested budget (₹)"): savings_budget,
        tr("Entered expenses (₹)"): 0.0,
        tr("Remaining (₹)"): savings_budget
    }
]

st.dataframe(
    pd.DataFrame(comparison),
    use_container_width=True,
    hide_index=True
)

st.caption(
    tr("This comparison is approximate. For example, a mobile bill may be a need, "
       "while entertainment spending may be a want. Categorise expenses based on your circumstances.")
)

st.markdown("---")

# 6. Savings projection
st.header(tr("6. Estimate Your Savings"))

monthly_saving = st.number_input(
    tr("Amount you plan to save each month (₹)"),
    min_value=0.0,
    max_value=10000000.0,
    value=min(savings_budget, max(balance, 0.0)),
    step=100.0,
    key="budget_monthly_saving"
)

months = st.slider(
    tr("Number of months"),
    min_value=1,
    max_value=60,
    value=12,
    key="budget_saving_months"
)

projected_savings = monthly_saving * months

col1, col2 = st.columns(2)

with col1:
    st.metric(
        tr("Estimated savings"),
        f"₹{projected_savings:,.2f}"
    )

with col2:
    st.metric(
        tr("Months"),
        str(months)
    )

st.caption(
    tr("This estimate excludes interest, fees, inflation, and unexpected expenses.")
)

if monthly_saving > max(balance, 0.0):
    st.warning(
        tr("Your savings target is higher than the money currently remaining in your plan. "
           "Adjust the target or revise your expenses without neglecting essential needs.")
    )

st.markdown("---")

# 7. Practical tips
st.header(tr("7. Simple Budgeting Tips"))

tips = [
    "Write down every expense for one week to understand your spending.",
    "Plan for school or college fees and other known future costs.",
    "Keep a small emergency reserve if your circumstances allow.",
    "Review subscriptions and optional purchases regularly.",
    "Avoid loans or credit purchases you cannot reasonably repay.",
    "Compare prices and check bills before paying.",
    "Review your budget at the end of every month and adjust it."
]

for tip in tips:
    st.write("✅ " + tr(tip))

st.markdown("---")

# 8. Weekly action plan
st.header(tr("8. My Weekly Money Plan"))

weekly_tasks = [
    "I will record my spending every day.",
    "I will review my expenses at the end of the week.",
    "I will check whether my spending fits my plan.",
    "I will set a realistic savings goal.",
    "I will check for suspicious transactions and messages."
]

for index, task in enumerate(weekly_tasks):
    st.checkbox(
        tr(task),
        key=f"budget_weekly_task_{index}"
    )

st.success(
    tr("A useful budget is realistic, flexible, and updated when your needs change.")
)

st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
