
import math
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="Savings | FinSaathi",
    page_icon="💰",
    layout="wide"
)

# Restore the selected language
if "language" not in st.session_state:
    saved_language = st.query_params.get("language", "English")
    if saved_language not in LANGUAGES:
        saved_language = "English"
    st.session_state["language"] = saved_language

st.sidebar.title("🌐 " + tr("Language Settings"))

selected_language = st.sidebar.selectbox(
    tr("Choose your language"),
    LANGUAGES,
    index=LANGUAGES.index(st.session_state["language"]),
    key="savings_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

st.title("💰 " + tr("Savings and Smart Money Habits"))
st.write(
    tr(
        "Learn how to save regularly, set financial goals, prepare for "
        "unexpected expenses, and understand savings products."
    )
)

st.info(
    "🌱 " + tr(
        "Small, regular savings can help you prepare for future needs. "
        "Start with an amount that fits your circumstances."
    )
)

st.markdown("---")

# SECTION 1: WHY SAVE?
st.header("1. " + tr("Why Is Saving Money Important?"))

st.write(
    tr(
        "Saving means keeping some money aside instead of spending all "
        "the money you receive. Savings can help with education, household "
        "needs, emergencies, and future plans."
    )
)

st.markdown("**" + tr("Benefits of saving") + "**")
st.markdown(
    "- " + tr("Helps prepare for unexpected expenses.") + "\n"
    "- " + tr("Supports education and important family needs.") + "\n"
    "- " + tr("Reduces dependence on borrowing for planned expenses.") + "\n"
    "- " + tr("Helps people work towards long-term goals.") + "\n"
    "- " + tr("Builds a habit of planning before spending.")
)

st.success(
    "📌 " + tr(
        "Example: If you receive ₹1,000 and can comfortably save ₹100, "
        "you can set aside ₹100 and plan your remaining expenses with ₹900."
    )
)

st.markdown("---")

# SECTION 2: TYPES OF SAVINGS GOALS
st.header("2. " + tr("Short-Term and Long-Term Goals"))

goal_data = [
    {
        tr("Goal type"): tr("Short-term"),
        tr("Example"): tr("Books, school supplies, or a small household purchase"),
        tr("Planning approach"): tr("Choose a target and save regularly")
    },
    {
        tr("Goal type"): tr("Medium-term"),
        tr("Example"): tr("Education expenses or a planned appliance purchase"),
        tr("Planning approach"): tr("Set a timeline and compare suitable savings options")
    },
    {
        tr("Goal type"): tr("Long-term"),
        tr("Example"): tr("Higher education or another major future expense"),
        tr("Planning approach"): tr("Review progress and understand product terms")
    }
]

st.table(goal_data)

st.subheader("Create your savings goal")

goal_name = st.text_input(
    tr("What are you saving for?"),
    placeholder=tr("Example: Books or education")
)

goal_amount = st.number_input(
    tr("Target amount (₹)"),
    min_value=0,
    max_value=10000000,
    value=5000,
    step=500
)

current_savings = st.number_input(
    tr("Amount already saved (₹)"),
    min_value=0,
    max_value=10000000,
    value=500,
    step=100
)

monthly_contribution = st.number_input(
    tr("Amount you can save each month (₹)"),
    min_value=0,
    max_value=1000000,
    value=500,
    step=100
)

remaining = max(0, goal_amount - current_savings)

col1, col2 = st.columns(2)

with col1:
    st.metric(tr("Target remaining"), f"₹{remaining:,.0f}")

with col2:
    progress = min(
        1.0,
        current_savings / goal_amount if goal_amount > 0 else 0.0
    )
    st.metric(tr("Goal progress"), f"{progress * 100:.1f}%")

st.progress(progress)

if goal_name.strip():
    st.write(tr("Your goal") + ": " + goal_name.strip())

if remaining == 0:
    st.success(tr("You have reached your savings target!"))
elif monthly_contribution > 0:
    months_needed = math.ceil(remaining / monthly_contribution)
    st.info(
        tr("Estimated time to reach your target")
        + f": {months_needed} "
        + tr("months, assuming regular contributions and no withdrawals.")
    )
else:
    st.warning(
        tr("Enter a monthly savings amount greater than zero to estimate the time.")
    )

st.caption(
    tr(
        "This calculator does not include interest, fees, inflation, or changes "
        "in your savings. It is an estimate, not a financial guarantee."
    )
)

st.markdown("---")

# SECTION 3: BUILD A SAVINGS HABIT
st.header("3. " + tr("How to Build a Savings Habit"))

st.markdown(
    "1. " + tr("Write down the money you receive each month.") + "\n"
    "2. " + tr("List essential expenses such as food, travel, and education.") + "\n"
    "3. " + tr("Choose a realistic savings amount.") + "\n"
    "4. " + tr("Save regularly when money becomes available.") + "\n"
    "5. " + tr("Review your progress at the end of each month.") + "\n"
    "6. " + tr("Adjust the plan if your income or needs change.")
)

st.subheader("Illustrative monthly plan")

budget_data = [
    {
        tr("Item"): tr("Monthly money received"),
        tr("Example amount"): "₹5,000"
    },
    {
        tr("Item"): tr("Essential expenses"),
        tr("Example amount"): "₹3,000"
    },
    {
        tr("Item"): tr("Other planned expenses"),
        tr("Example amount"): "₹1,000"
    },
    {
        tr("Item"): tr("Savings"),
        tr("Example amount"): "₹1,000"
    }
]

st.table(budget_data)

st.caption(
    tr(
        "This is only an example. Your own plan should reflect your actual "
        "income, household responsibilities, and essential expenses."
    )
)

st.markdown("---")

# SECTION 4: EMERGENCY SAVINGS
st.header("4. " + tr("Emergency Savings"))

st.write(
    tr(
        "Emergency savings are money kept aside for unexpected needs, "
        "such as urgent travel, essential repairs, or a sudden loss of income."
    )
)

st.markdown("**" + tr("Ways to get started") + "**")
st.markdown(
    "- " + tr("Begin with a small amount you can manage.") + "\n"
    "- " + tr("Keep emergency money accessible when needed.") + "\n"
    "- " + tr("Separate emergency savings from everyday spending where practical.") + "\n"
    "- " + tr("Rebuild the fund gradually after using it.") + "\n"
    "- " + tr("Do not sacrifice essential food, health, or education needs to meet a target.")
)

st.info(
    "💡 " + tr(
        "There is no single correct emergency-fund amount for every family. "
        "Choose a target based on your household's essential expenses and situation."
    )
)

st.markdown("---")

# SECTION 5: UNDERSTANDING INTEREST
st.header("5. " + tr("Understanding Savings Interest"))

st.write(
    tr(
        "Interest is money paid on eligible deposits according to the product's "
        "terms. The amount earned depends on the balance, rate, duration, "
        "compounding method, and other conditions."
    )
)

st.subheader("Simple interest example")

principal = st.number_input(
    tr("Example deposit amount (₹)"),
    min_value=0,
    max_value=10000000,
    value=10000,
    step=1000
)

annual_rate = st.number_input(
    tr("Illustrative annual interest rate (%)"),
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.5
)

years = st.number_input(
    tr("Duration (years)"),
    min_value=1,
    max_value=50,
    value=2,
    step=1
)

interest_earned = principal * (annual_rate / 100) * years
total_amount = principal + interest_earned

col1, col2 = st.columns(2)

with col1:
    st.metric(tr("Illustrative interest"), f"₹{interest_earned:,.2f}")

with col2:
    st.metric(tr("Principal plus interest"), f"₹{total_amount:,.2f}")

st.code(
    "Simple Interest = Principal × Rate × Time / 100",
    language="text"
)

st.caption(
    tr(
        "The rate above is an example chosen for learning, not a current bank "
        "or government scheme rate. Actual products may calculate interest differently."
    )
)

st.markdown("---")

# SECTION 6: SAVINGS PRODUCTS
st.header("6. " + tr("Compare Savings Options"))

savings_options = [
    {
        tr("Option"): tr("Savings account"),
        tr("Common use"): tr("Everyday access to money"),
        tr("Consider"): tr("Interest rate, fees, access, and account rules")
    },
    {
        tr("Option"): tr("Recurring deposit"),
        tr("Common use"): tr("Regular deposits over a chosen period"),
        tr("Consider"): tr("Deposit schedule, maturity, and early closure rules")
    },
    {
        tr("Option"): tr("Fixed deposit"),
        tr("Common use"): tr("Keeping a lump sum for a selected period"),
        tr("Consider"): tr("Rate, tenure, withdrawal terms, and applicable tax")
    },
    {
        tr("Option"): tr("Government small-savings product"),
        tr("Common use"): tr("Saving under the rules of a specific scheme"),
        tr("Consider"): tr("Eligibility, lock-in, current rate, and withdrawal rules")
    }
]

st.table(savings_options)

st.warning(
    "⚠️ " + tr(
        "Do not choose a financial product based only on its advertised rate. "
        "Read the official terms, understand access restrictions, and check "
        "whether the product suits your needs."
    )
)

st.markdown("---")

# SECTION 7: GOVERNMENT SAVINGS SCHEMES
st.header("7. " + tr("Government Savings Schemes in India"))

st.write(
    tr(
        "India offers several small-savings products. The eligibility, deposit "
        "limits, interest rates, tax treatment, and withdrawal rules differ. "
        "Always verify the current rules through official government sources."
    )
)

scheme_data = [
    {
        tr("Scheme"): "Public Provident Fund (PPF)",
        tr("General purpose"): tr("Long-term savings under scheme rules"),
        tr("Official source"): "https://www.indiapost.gov.in/"
    },
    {
        tr("Scheme"): "Sukanya Samriddhi Account",
        tr("General purpose"): tr("Savings for an eligible girl child, subject to scheme rules"),
        tr("Official source"): "https://www.indiapost.gov.in/"
    },
    {
        tr("Scheme"): "National Savings Certificate (NSC)",
        tr("General purpose"): tr("Savings through a government small-savings product"),
        tr("Official source"): "https://www.indiapost.gov.in/"
    },
    {
        tr("Scheme"): "Post Office Recurring Deposit",
        tr("General purpose"): tr("Regular deposits under the product's terms"),
        tr("Official source"): "https://www.indiapost.gov.in/"
    }
]

st.dataframe(
    scheme_data,
    use_container_width=True,
    hide_index=True
)

st.markdown("**" + tr("Before opening an account") + "**")

st.markdown(
    "- " + tr("Check the latest official interest rate.") + "\n"
    "- " + tr("Confirm eligibility and permitted deposit amounts.") + "\n"
    "- " + tr("Understand maturity and early withdrawal rules.") + "\n"
    "- " + tr("Ask about tax treatment and required documents.") + "\n"
    "- " + tr("Use an authorised bank or post office.")
)

st.markdown(
    tr("Official reference: National Savings Institute")
    + " — https://www.nsiindia.gov.in/"
)

st.markdown("---")

# SECTION 8: CASE STUDY
st.header("8. " + tr("Savings Case Study"))

st.write(
    tr(
        "A family wants to save ₹6,000 for an important school expense "
        "six months from now. They can set aside ₹1,000 each month."
    )
)

with st.expander(tr("View the worked example")):
    st.write(
        tr("Monthly savings") + ": ₹1,000"
    )
    st.write(
        tr("Number of months") + ": 6"
    )
    st.write(
        tr("Total planned savings") + ": ₹1,000 × 6 = ₹6,000"
    )
    st.success(
        tr(
            "If the family saves the planned amount each month and does not "
            "withdraw it, the target can be reached in six months, excluding interest."
        )
    )

st.subheader("Try a different monthly amount")

case_monthly = st.number_input(
    tr("Your planned monthly savings (₹)"),
    min_value=0,
    max_value=1000000,
    value=1000,
    step=100
)

case_target = st.number_input(
    tr("Your target amount (₹)"),
    min_value=0,
    max_value=10000000,
    value=6000,
    step=500
)

if case_target == 0:
    st.success(tr("Your target is already zero."))
elif case_monthly > 0:
    case_months = math.ceil(case_target / case_monthly)
    st.metric(
        tr("Estimated months needed"),
        str(case_months)
    )
else:
    st.warning(tr("Enter a monthly amount greater than zero."))

st.markdown("---")

# SECTION 9: SAVINGS SAFETY
st.header("9. " + tr("Savings Safety Tips"))

st.markdown(
    "- " + tr("Be cautious of people promising guaranteed unusually high returns.") + "\n"
    "- " + tr("Never share your OTP, PIN, password, or confidential banking credentials.") + "\n"
    "- " + tr("Do not transfer money to receive a promised prize or investment return.") + "\n"
    "- " + tr("Verify financial institutions and schemes through official sources.") + "\n"
    "- " + tr("Read fees, lock-in periods, and withdrawal conditions before investing.") + "\n"
    "- " + tr("Do not borrow money just to join an investment you do not understand.") + "\n"
    "- " + tr("Discuss major financial decisions with a trusted, knowledgeable adult.")
)

st.error(
    "🚨 " + tr(
        "If you suspect a financial scam, contact your bank promptly. "
        "In India, you can report cyber financial fraud through the official "
        "National Cyber Crime Reporting Portal at https://cybercrime.gov.in/ "
        "or call 1930 as soon as possible."
    )
)

st.markdown("---")

# FINAL SUMMARY
st.header("10. " + tr("Your Savings Action Plan"))

action_items = [
    tr("Choose one realistic savings goal."),
    tr("Decide how much you can save regularly."),
    tr("Choose a suitable and trustworthy place to keep your savings."),
    tr("Review your progress every month."),
    tr("Check official terms before opening any savings product.")
]

for index, item in enumerate(action_items):
    st.checkbox(
        item,
        key=f"savings_action_{index}"
    )

st.success(
    "🌱 " + tr(
        "Remember: saving is about building a sustainable habit. "
        "Start with what you can manage and review your plan regularly."
    )
)

st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))
