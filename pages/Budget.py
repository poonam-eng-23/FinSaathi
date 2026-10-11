
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Budget Planner - FinSaathi",
    page_icon="📊",
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
    key="budget_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

# Budget planner
st.title("📊 " + tr("Monthly Budget Planner"))
st.write(
    tr("Plan your spending, manage your money, and work towards your savings goals.")
)

st.markdown("---")

st.subheader("💰 " + tr("Enter Your Monthly Income"))

income = st.number_input(
    tr("Monthly income or allowance (₹)"),
    min_value=0.0,
    value=5000.0,
    step=500.0
)

st.subheader("🧾 " + tr("Enter Your Monthly Expenses"))

food = st.number_input(
    tr("Food and household needs (₹)"),
    min_value=0.0,
    value=1000.0,
    step=100.0
)

education = st.number_input(
    tr("Education and books (₹)"),
    min_value=0.0,
    value=1000.0,
    step=100.0
)

travel = st.number_input(
    tr("Travel (₹)"),
    min_value=0.0,
    value=500.0,
    step=100.0
)

other = st.number_input(
    tr("Other expenses (₹)"),
    min_value=0.0,
    value=500.0,
    step=100.0
)

expenses = food + education + travel + other
balance = income - expenses

st.markdown("---")

st.subheader("📈 " + tr("Your Budget Summary"))

col1, col2, col3 = st.columns(3)

col1.metric(
    tr("Monthly Income"),
    f"₹{income:,.2f}"
)

col2.metric(
    tr("Total Expenses"),
    f"₹{expenses:,.2f}"
)

col3.metric(
    tr("Money Remaining"),
    f"₹{balance:,.2f}"
)

if income > 0:
    st.progress(min(expenses / income, 1.0))
    st.caption(
        tr("Percentage of income spent") +
        f": {expenses / income * 100:.1f}%"
    )

if balance > 0:
    st.success(
        "✅ " + tr("You have money remaining. Consider saving some of it.")
    )
elif balance == 0:
    st.info(
        tr("Your entire income is allocated. Look for opportunities to save.")
    )
else:
    st.error(
        "⚠️ " + tr("Your expenses exceed your income. Review your budget.")
    )

st.markdown("---")

st.subheader("📋 " + tr("Simple Budgeting Guide"))

guide = [
    "List your income and expenses every month.",
    "Prioritise essential needs such as food and education.",
    "Set aside some money for savings when possible.",
    "Avoid unnecessary spending and review your budget regularly."
]

for item in guide:
    st.markdown("- " + tr(item))

st.caption(
    tr("Budget estimates are for learning and planning only.")
)

st.markdown("---")
st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
