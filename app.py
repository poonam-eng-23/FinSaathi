
import streamlit as st

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App styling
st.markdown("""
<style>
    .stApp {
        background-color: #f5f9ff;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #145da0;
        text-align: center;
        margin-bottom: 0;
    }

    .tagline {
        font-size: 18px;
        color: #328c87;
        text-align: center;
        margin-top: 5px;
    }

    .welcome {
        background: linear-gradient(120deg, #145da0, #328c87);
        padding: 25px;
        border-radius: 18px;
        color: white;
        text-align: center;
        margin: 20px 0;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        min-height: 45px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Supported language choices
LANGUAGES = [
    "English",
    "ಕನ್ನಡ (Kannada)",
    "हिन्दी (Hindi)",
    "मराठी (Marathi)",
    "தமிழ் (Tamil)",
    "తెలుగు (Telugu)",
    "മലയാളം (Malayalam)",
    "বাংলা (Bengali)",
    "ગુજરાતી (Gujarati)",
    "ਪੰਜਾਬੀ (Punjabi)",
    "ଓଡ଼ିଆ (Odia)",
    "অসমীয়া (Assamese)",
    "اردو (Urdu)",
    "संस्कृतम् (Sanskrit)",
    "कोंकणी (Konkani)",
    "नेपाली (Nepali)",
    "मैथिली (Maithili)",
    "डोगरी (Dogri)",
    "کٲشُر (Kashmiri)",
    "سنڌي (Sindhi)",
    "बोडो (Bodo)",
    "मणिपुरी (Manipuri)",
    "संताली (Santali)"
]

# Sidebar
with st.sidebar:
    st.markdown("## 💰 FinSaathi")
    st.caption("Learn Finance. Stay Safe.")

    selected_language = st.selectbox(
        "🌐 Select Language",
        LANGUAGES,
        key="finsaathi_language"
    )

    st.divider()
    st.markdown("### 📚 Learning Modules")
    st.caption("Choose a topic from the links below.")

# Main home page
st.markdown(
    '<div class="main-title">💰 FinSaathi</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">Learn Finance. Stay Safe.</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="welcome">
    <h2>Welcome to FinSaathi!</h2>
    <p>Your friendly companion for financial awareness.</p>
    <p>Learn about banking, savings, digital payments,
    budgeting and financial safety.</p>
</div>
""", unsafe_allow_html=True)

st.info(
    f"Selected language: {selected_language}. "
    "Full translation depends on your translation integration and API configuration."
)

st.subheader("Explore FinSaathi")

# Links to existing Streamlit pages
pages = [
    ("🏦 Banking", "pages/1_Banking.py"),
    ("🌱 Savings", "pages/Savings.py"),
    ("📱 UPI Payments", "pages/UPI.py"),
    ("🛡️ Fraud Safety", "pages/Fraud_Safety.py"),
    ("🤖 AI Voice Assistant", "pages/AI_Assistant.py"),
    ("💵 Budget Planner", "pages/Budget.py"),
    ("📝 Financial Quiz", "pages/Quiz.py"),
]

for title, page_path in pages:
    st.page_link(page_path, label=title, icon="➡️")

st.divider()

st.subheader("🔐 Stay Financially Safe")
st.markdown("""
- Never share your OTP, UPI PIN or banking password.
- Verify payment requests before approving them.
- Do not trust unexpected links or urgent money requests.
- Contact your bank through its official website or phone number
  if you suspect fraud.
""")

st.caption(
    "FinSaathi is an educational awareness application. "
    "It does not access real bank accounts or perform actual payments."
)
