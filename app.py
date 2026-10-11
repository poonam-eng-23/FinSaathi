
import streamlit as st

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💙",
    layout="wide"
)

# All 22 scheduled Indian languages + English
LANGUAGES = {
    "English": "English",
    "অসমীয়া — Assamese": "Assamese",
    "বাংলা — Bengali": "Bengali",
    "बड़ो — Bodo": "Bodo",
    "डोगरी — Dogri": "Dogri",
    "ગુજરાતી — Gujarati": "Gujarati",
    "हिन्दी — Hindi": "Hindi",
    "ಕನ್ನಡ — Kannada": "Kannada",
    "کٲشُر — Kashmiri": "Kashmiri",
    "कोंकणी — Konkani": "Konkani",
    "मैथिली — Maithili": "Maithili",
    "മലയാളം — Malayalam": "Malayalam",
    "মৈতৈলোন্ — Manipuri": "Manipuri",
    "मराठी — Marathi": "Marathi",
    "नेपाली — Nepali": "Nepali",
    "ଓଡ଼ିଆ — Odia": "Odia",
    "ਪੰਜਾਬੀ — Punjabi": "Punjabi",
    "संस्कृतम् — Sanskrit": "Sanskrit",
    "ᱥᱟᱱᱛᱟᱲᱤ — Santali": "Santali",
    "سنڌي — Sindhi": "Sindhi",
    "தமிழ் — Tamil": "Tamil",
    "తెలుగు — Telugu": "Telugu",
    "اردو — Urdu": "Urdu",
}

# Language selection
st.sidebar.title("🌐 Language / ಭಾಷೆ")

language_names = list(LANGUAGES.keys())

current_language = st.session_state.get(
    "selected_language",
    "English"
)

if current_language not in language_names:
    current_language = "English"

selected_language = st.sidebar.selectbox(
    "Choose your language",
    language_names,
    index=language_names.index(current_language),
    key="language_selector"
)

st.session_state["selected_language"] = selected_language

# Keep compatibility with your existing pages.
# The existing page translations support English,
# Kannada, Hindi and Marathi.
supported_languages = ["English", "Kannada", "Hindi", "Marathi"]

if LANGUAGES[selected_language] in supported_languages:
    st.session_state["language_code"] = LANGUAGES[selected_language]
else:
    st.session_state["language_code"] = "English"

# Home page
st.title("💙 FinSaathi")
st.subheader("Learn Finance. Stay Safe.")

st.write(
    "Your friendly guide to banking, savings, budgeting "
    "and digital payment safety."
)

st.info(
    "Choose a topic below to learn about managing money "
    "and staying safe from financial fraud."
)

st.divider()

st.header("📚 Learn About Finance")

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/1_Banking.py",
        label="🏦 Banking Basics",
        icon="🏦"
    )

    st.page_link(
        "pages/Savings.py",
        label="💰 Savings",
        icon="💰"
    )

    st.page_link(
        "pages/UPI.py",
        label="📱 UPI Payments",
        icon="📱"
    )

    st.page_link(
        "pages/Budget.py",
        label="📊 Budget Planner",
        icon="📊"
    )

with col2:
    st.page_link(
        "pages/Fraud_safety.py",
        label="🛡️ Fraud Safety",
        icon="🛡️"
    )

    st.page_link(
        "pages/AI_Assistant.py",
        label="🤖 Saathi Assistant",
        icon="🤖"
    )

    st.page_link(
        "pages/Quiz.py",
        label="📝 Financial Quiz",
        icon="📝"
    )

st.divider()

st.subheader("💡 Financial Safety Tip")

st.write(
    "Never share your OTP, ATM PIN, UPI PIN or banking "
    "password with anyone. Banks will not ask you to "
    "share these secrets over a call or message."
)

st.caption(
    "FinSaathi is an educational project. It does not "
    "replace advice from a qualified financial professional."
)

if LANGUAGES[selected_language] not in supported_languages:
    st.warning(
        "Your selected language is available in the menu, "
        "but its page content is not translated yet. "
        "Automatic translation needs to be connected separately."
    )
