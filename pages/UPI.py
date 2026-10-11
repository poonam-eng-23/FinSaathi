
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="UPI Payments - FinSaathi",
    page_icon="📱",
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
    key="upi_language"
)

st.session_state["language"] = selected_language
st.query_params["language"] = selected_language

# UPI page
st.title("📱 " + tr("UPI Payments"))
st.write(tr("Learn how to make digital payments safely."))

st.markdown("---")

st.subheader("💳 " + tr("What is UPI?"))
st.write(tr(
    "UPI stands for Unified Payments Interface. It lets you send and "
    "receive money instantly using a supported payment app."
))

st.subheader("✅ " + tr("Safe UPI Rules"))

rules = [
    "Never share your UPI PIN with anyone.",
    "You do not need to enter your PIN to receive money.",
    "Check the receiver's name before making a payment.",
    "Never click suspicious payment links.",
    "Do not approve unknown payment requests.",
    "Contact your bank immediately if you notice an unauthorised transaction."
]

for rule in rules:
    st.markdown("- " + tr(rule))

st.warning(
    "⚠️ " + tr(
        "Your UPI PIN is secret. Never share it with anyone, "
        "including people claiming to be bank employees."
    )
)

st.markdown("---")

st.subheader("🧠 " + tr("Scam or Safe?"))
st.write(tr("Read each situation and choose the safest answer."))

question = st.radio(
    tr("Someone says you must enter your UPI PIN to receive a prize. What should you do?"),
    [
        tr("Enter the PIN immediately"),
        tr("Do not enter the PIN; it may be a scam"),
        tr("Share the PIN with the caller")
    ],
    index=None,
    key="upi_scam_question"
)

if st.button("Check Answer", use_container_width=True):
    if question is None:
        st.info(tr("Please select an answer first."))
    elif question == tr("Do not enter the PIN; it may be a scam"):
        st.success(
            "✅ " + tr(
                "Correct! Never enter your UPI PIN to receive a prize or money."
            )
        )
    else:
        st.error(
            "❌ " + tr(
                "Incorrect. Never share your UPI PIN or enter it for an unknown request."
            )
        )

st.markdown("---")

st.subheader("🧪 " + tr("Practice Payment Calculator"))
st.caption(
    tr("This is only a demonstration. It does not transfer real money.")
)

amount = st.number_input(
    tr("Enter a practice payment amount (₹)"),
    min_value=1,
    max_value=100000,
    value=100,
    step=50
)

if st.button("Review Practice Payment", use_container_width=True):
    st.info(
        tr("Practice amount") + f": ₹{amount:,}"
    )
    st.write(
        "🔒 " + tr(
            "Before any real payment, verify the recipient and amount "
            "in your official payment app."
        )
    )

st.markdown("---")
st.caption(tr("FinSaathi — Learn Finance. Stay Safe."))

