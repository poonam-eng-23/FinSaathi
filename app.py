
import streamlit as st
from translation import tr, LANGUAGES
from accessibility import apply_accessibility

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💙",
    layout="wide"
)

if "language" not in st.session_state:
    st.session_state["language"] = "English"

if "language_picker" not in st.session_state:
    st.session_state["language_picker"] = st.session_state["language"]

if "accessibility_mode" not in st.session_state:
    st.session_state["accessibility_mode"] = False


def update_language():
    st.session_state["language"] = st.session_state["language_picker"]


def t(text):
    return tr(text)


st.sidebar.title("💙 FinSaathi")

st.sidebar.selectbox(
    t("Choose your language"),
    LANGUAGES,
    key="language_picker",
    on_change=update_language
)

st.sidebar.markdown("---")
st.sidebar.subheader(t("Accessibility"))

# Accessibility Mode ON/OFF
apply_accessibility()

st.sidebar.markdown("---")
st.sidebar.subheader(t("Menu"))

pages = [
    ("🏠", "Home", "app.py"),
    ("🏦", "Banking", "pages/1_Banking.py"),
    ("💰", "Savings", "pages/Savings.py"),
    ("📱", "UPI", "pages/UPI.py"),
    ("🛡️", "Fraud Safety", "pages/Fraud_Safety.py"),
    ("🤖", "AI Assistant", "pages/AI_Assistant.py"),
    ("📊", "Budget", "pages/Budget.py"),
    ("📝", "Quiz", "pages/Quiz.py"),
]

for emoji, label, path in pages:
    st.sidebar.page_link(
        path,
        label=f"{emoji} {t(label)}"
    )

st.title("💙 FinSaathi")
st.subheader(t("Learn Finance. Stay Safe."))

st.markdown("---")
st.header(t("Welcome to FinSaathi!"))

st.write(
    t(
        "Your financial literacy companion for safer banking, "
        "smarter savings, and fraud awareness."
    )
)

# Accessibility information on the home page
st.markdown("---")
st.subheader(t("♿ Make FinSaathi easier to use"))

st.write(
    t(
        "Turn on Accessibility Mode in the sidebar to make text "
        "larger and buttons easier to use."
    )
)

features = [
    (
        "🏦",
        "Banking",
        "pages/1_Banking.py",
        "Learn about bank accounts, ATMs, and banking services."
    ),
    (
        "💰",
        "Savings",
        "pages/Savings.py",
        "Discover simple ways to save money."
    ),
    (
        "📱",
        "UPI",
        "pages/UPI.py",
        "Learn how to use UPI safely."
    ),
    (
        "🛡️",
        "Fraud Safety",
        "pages/Fraud_Safety.py",
        "Recognize suspicious messages and avoid online scams."
    ),
    (
        "🤖",
        "AI Assistant",
        "pages/AI_Assistant.py",
        "Get help with basic financial questions."
    ),
    (
        "📊",
        "Budget",
        "pages/Budget.py",
        "Plan your income, expenses, and savings."
    ),
    (
        "📝",
        "Quiz",
        "pages/Quiz.py",
        "Test your financial knowledge."
    ),
]

for start in range(0, len(features), 2):
    columns = st.columns(2)

    for column, feature in zip(
        columns,
        features[start:start + 2]
    ):
        emoji, title, path, description = feature

        with column:
            st.markdown(f"### {emoji} {t(title)}")
            st.write(t(description))
            st.page_link(
                path,
                label=t("Explore")
            )

st.markdown("---")

st.warning(
    t(
        "Never share your OTP, UPI PIN, or bank password with anyone."
    )
)

st.caption(
    t("FinSaathi — Learn Finance. Stay Safe. 💙")
)
