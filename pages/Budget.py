import streamlit as st

st.set_page_config(
    page_title="Budget - FinSaathi",
    page_icon="📊"
)

st.title("📊 My Budget")
st.subheader("Plan your monthly money easily")

st.write(
    "A budget helps you understand your income, expenses and savings."
)

st.divider()

st.header("💰 Enter Your Monthly Details")

income = st.number_input(
    "Monthly Income (₹)",
    min_value=0,
    value=10000,
    step=500
)

food = st.number_input(
    "Food & Groceries (₹)",
    min_value=0,
    value=2000,
    step=100
)

travel = st.number_input(
    "Travel (₹)",
    min_value=0,
    value=1000,
    step=100
)

education = st.number_input(
    "Education (₹)",
    min_value=0,
    value=1000,
    step=100
)

other = st.number_input(
    "Other Expenses (₹)",
    min_value=0,
    value=1000,
    step=100
)

if st.button("📊 Calculate Budget"):

    total_expenses = food + travel + education + other
    remaining = income - total_expenses

    st.divider()

    st.header("📋 Your Budget Summary")

    st.write(f"💰 Income: ₹{income:,}")
    st.write(f"💸 Total Expenses: ₹{total_expenses:,}")

    if remaining > 0:
        st.success(
            f"✅ Money remaining: ₹{remaining:,}"
        )
        st.info(
            "You can save some of the remaining money "
            "for future needs."
        )

    elif remaining == 0:
        st.warning(
            "⚠️ Your income and expenses are equal."
        )

    else:
        st.error(
            f"❌ Your expenses are ₹{abs(remaining):,} "
            "more than your income."
        )

st.divider()

st.header("💡 Budget Tip")

st.info(
    "Try to track your expenses regularly and avoid "
    "unnecessary spending."
)

st.caption("FinSaathi – Learn Finance. Stay Safe. 💰")