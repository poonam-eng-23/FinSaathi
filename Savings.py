import streamlit as st

st.set_page_config(
    page_title="Savings - FinSaathi",
    page_icon="💰"
)

st.title("💰 Savings")
st.subheader("Learn how to save money wisely")

st.write(
    "Saving means keeping some of your money for future needs."
)

st.divider()

st.header("🌱 Why is Saving Important?")

st.write("Saving money can help you:")
st.write("✅ Handle emergencies")
st.write("✅ Meet future needs")
st.write("✅ Reduce financial stress")
st.write("✅ Plan for education and other goals")

st.divider()

st.header("💡 Simple Saving Method")

income = st.number_input(
    "Enter your monthly income (₹)",
    min_value=0,
    value=10000,
    step=500
)

expenses = st.number_input(
    "Enter your monthly expenses (₹)",
    min_value=0,
    value=7000,
    step=500
)

if st.button("Calculate"):
    savings = income - expenses

    if savings > 0:
        st.success(
            f"Your remaining amount is ₹{savings:,}."
        )

        st.info(
            "You can consider keeping some of the remaining money "
            "as savings according to your needs."
        )

    elif savings == 0:
        st.warning(
            "Your income and expenses are equal. "
            "Try reviewing your expenses."
        )

    else:
        st.error(
            f"Your expenses are ₹{abs(savings):,} more than your income."
        )

st.divider()

st.header("🚨 Remember")

st.warning(
    "Save regularly, avoid unnecessary spending, "
    "and keep emergency money safely."
)