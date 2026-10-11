
import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi - Savings",
    page_icon="💰",
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

# Savings page
st.title("💰 " + t("Savings Made Easy"))

st.write(
    t("Learn how to save money regularly and work towards your goals.")
)

st.info(
    t("Small, regular savings can help you prepare for future needs.")
)

st.divider()

# Why save?
st.header("🌱 " + t("Why Should You Save?"))

st.markdown(
    "- Prepare for emergencies.\n"
    "- Plan for education and important purchases.\n"
    "- Avoid unnecessary borrowing.\n"
    "- Work towards your personal goals."
)

st.divider()

# Savings calculator
st.header("🧮 " + t("Savings Calculator"))

monthly_saving = st.number_input(
    t("How much can you save each month? (₹)"),
    min_value=0,
    max_value=1000000,
    value=500,
    step=100,
    key="monthly_saving"
)

saving_months = st.number_input(
    t("For how many months?"),
    min_value=1,
    max_value=600,
    value=12,
    step=1,
    key="saving_months"
)

total_savings = monthly_saving * saving_months

st.metric(
    t("Total savings"),
    f"₹{total_savings:,.2f}"
)

st.caption(
    t("This estimate does not include interest or fees.")
)

st.divider()

# Saving tips
st.header("💡 " + t("Smart Saving Tips"))

st.markdown(
    "1. Set a realistic savings goal.\n"
    "2. Save a small amount regularly when possible.\n"
    "3. Track your income and expenses.\n"
    "4. Compare needs and wants before buying something.\n"
    "5. Keep savings in a safe, suitable account.\n"
    "6. Avoid offers promising guaranteed, unrealistic returns."
)

st.divider()

# Savings goal planner
st.header("🎯 " + t("My Savings Goal"))

goal_name = st.text_input(
    t("What are you saving for?"),
    placeholder="Example: Books, education or a bicycle",
    key="savings_goal_name"
)

goal_amount = st.number_input(
    t("Target amount (₹)"),
    min_value=1,
    max_value=10000000,
    value=5000,
    step=500,
    key="savings_goal_amount"
)

if st.button(t("Calculate Goal Plan"), use_container_width=True):
    if not goal_name.strip():
        st.warning(t("Please enter your savings goal."))
    else:
        st.success(
            f"{t('Goal')}: {goal_name}\n\n"
            f"{t('Target amount')}: ₹{goal_amount:,.2f}"
        )

        if monthly_saving > 0:
            months_needed = (
                goal_amount + monthly_saving - 1
            ) // monthly_saving

            st.write(
                f"{t('Estimated time needed')}: "
                f"{months_needed} {t('months')}"
            )
        else:
            st.info(
                t("Enter a monthly savings amount greater than zero "
                  "to estimate the time needed.")
            )

st.divider()

# Knowledge check
st.header("🧠 " + t("Savings Quiz"))

answer = st.radio(
    t("Which is a good saving habit?"),
    [
        t("Spend all money immediately"),
        t("Save regularly according to your budget"),
        t("Share bank PINs to get saving advice")
    ],
    key="savings_quiz"
)

if st.button(t("Check Answer"), key="savings_check"):
    if answer == t("Save regularly according to your budget"):
        st.success(t("Correct! Regular saving helps build good habits."))
    else:
        st.error(t("Try again. Choose the option about regular saving."))

st.divider()

if st.button("🏠 " + t("Home"), use_container_width=True):
    st.switch_page("app.py")

st.caption("💙 FinSaathi — " + t("Learn Finance. Stay Safe."))
