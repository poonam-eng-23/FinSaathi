import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Savings - FinSaathi",
    page_icon="💰",
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
    key="savings_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

# Savings page
st.title("💰 " + tr("Smart Savings"))
st.write(tr("Learn simple ways to save money and build good financial habits."))

st.markdown("---")

st.subheader("🎯 " + tr("Why Should You Save Money?"))

st.write(tr(
    "Saving money helps you handle emergencies, achieve your goals, "
    "pay for education, and prepare for future needs."
))

st.subheader("💡 " + tr("Simple Saving Tips"))

tips = [
    "Save a small amount regularly, even if it is only a little.",
    "Keep your savings separate from your everyday spending money.",
    "Make a list of your needs before spending money.",
    "Avoid unnecessary purchases and compare prices.",
    "Use a bank savings account to keep your money safer.",
    "Set a clear goal, such as education or buying something important."
]

for tip in tips:
    st.markdown("- " + tr(tip))

st.markdown("---")

st.subheader("🧮 " + tr("Savings Calculator"))

income = st.number_input(
    tr("Enter your monthly income or allowance (₹)"),
    min_value=0.0,
    value=5000.0,
    step=500.0
)

expenses = st.number_input(
    tr("Enter your monthly expenses (₹)"),
    min_value=0.0,
    value=3500.0,
    step=500.0
)

if st.button("Calculate Savings", use_container_width=True):
    savings = income - expenses

    if savings > 0:
        st.success(
            tr("Your estimated monthly savings are") +
            f": ₹{savings:,.2f}"
        )

        st.info(
            tr("Your estimated savings in one year are") +
            f": ₹{savings * 12:,.2f}"
        )

    elif savings == 0:
        st.warning(
            tr("Your income and expenses are equal. "
               "Look for ways to save a small amount.")
        )

    else:
        st.error(
            tr("Your expenses are greater than your income. "
               "Review your spending and make a budget.")
        )

st.markdown("---")

st.subheader("🌱 " + tr("Start a Savings Goal"))

goal = st.selectbox(
    tr("Choose a savings goal"),
    [
        "Education",
        "Emergency Fund",
        "Books and Study Materials",
        "Household Needs",
        "Other"
    ]
)

target = st.number_input(
    tr("Enter your savings target (₹)"),
    min_value=1.0,
    value=5000.0,
    step=500.0,
    key="savings_target"
)

monthly_saving = st.number_input(
    tr("How much can you save each month? (₹)"),
    min_value=1.0,
    value=500.0,
    step=100.0,
    key="monthly_saving"
)

if st.button("Estimate Goal Time", use_container_width=True):
    months = int((target + monthly_saving - 1) // monthly_saving)

    st.info(
        tr("For your goal") + " (" + tr(goal) + "), " +
        tr("you may need approximately") +
        f" {months} " +
        tr("months to reach") +
        f" ₹{target:,.2f}."
    )

st.markdown("---")
st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
