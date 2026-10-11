
import streamlit as st
from translation import tr

st.set_page_config(
    page_title="FinSaathi - Savings",
    page_icon="💰",
    layout="wide"
)


def t(text):
    return tr(text)


if "language" not in st.session_state:
    st.session_state["language"] = "English"


st.title(t("💰 Learn About Savings"))
st.write(t("Small savings today can help you in the future."))

st.divider()

st.subheader(t("What is saving?"))
st.write(
    t(
        "Saving means keeping some money aside instead of "
        "spending all your income."
    )
)

st.subheader(t("Simple Ways to Save Money"))
st.write("1. " + t("Set aside a small amount regularly."))
st.write("2. " + t("Make a list before shopping."))
st.write("3. " + t("Avoid unnecessary expenses."))

st.divider()

st.subheader(t("Savings Goal Calculator"))

income = st.number_input(
    t("Monthly income (₹)"),
    min_value=0.0,
    step=500.0
)

expenses = st.number_input(
    t("Monthly expenses (₹)"),
    min_value=0.0,
    step=500.0
)

remaining = income - expenses

st.metric(
    t("Money left after expenses"),
    f"₹{remaining:,.2f}"
)

if remaining > 0:
    st.success(
        t("Try to save a manageable amount regularly.")
    )
elif remaining < 0:
    st.warning(
        t(
            "Expenses cannot be greater than income if you "
            "want to have money left over."
        )
    )

st.divider()

st.caption(t("FinSaathi — Learn Finance. Stay Safe. 💙"))

if st.button(t("🏠 Home")):
    st.switch_page("app.py")
