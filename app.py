
import streamlit as st

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Language selection
if "language" not in st.session_state:
    st.session_state.language = "English"

# English and Kannada home-page text
kn = st.session_state.language == "ಕನ್ನಡ"

T = {
    "title": "ಫಿನ್‌ಸಾಥಿ" if kn else "FinSaathi",
    "tagline": "ಹಣಕಾಸು ಕಲಿಯಿರಿ. ಸುರಕ್ಷಿತವಾಗಿರಿ." if kn else "Learn Finance. Stay Safe.",
    "language": "ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ" if kn else "Choose Language",
    "welcome": "ಫಿನ್‌ಸಾಥಿಗೆ ಸ್ವಾಗತ!" if kn else "Welcome to FinSaathi!",
    "intro": "ಹಣಕಾಸಿನ ಅರಿವಿಗೆ ನಿಮ್ಮ ಸ್ನೇಹಪರ ಸಂಗಾತಿ." if kn else "Your friendly companion for financial awareness.",
    "description": "ಹಣ ಉಳಿಸುವುದು, ಡಿಜಿಟಲ್ ಪಾವತಿಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಬಳಸುವುದು, ಬ್ಯಾಂಕಿಂಗ್ ತಿಳಿಯುವುದು ಮತ್ತು ವಂಚನೆಯಿಂದ ನಿಮ್ಮನ್ನು ರಕ್ಷಿಸಿಕೊಳ್ಳುವುದನ್ನು ಕಲಿಯಿರಿ." if kn else "Learn to save money, use digital payments safely, understand banking and protect yourself from fraud.",
    "explore": "ಫಿನ್‌ಸಾಥಿಯನ್ನು ಅನ್ವೇಷಿಸಿ" if kn else "Explore FinSaathi",
    "choose": "ಪ್ರಾರಂಭಿಸಲು ಒಂದು ವಿಷಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ." if kn else "Choose a topic to get started.",
    "banking": "🏦 ಬ್ಯಾಂಕಿಂಗ್ ಮೂಲಭೂತಗಳು" if kn else "🏦 Banking Basics",
    "savings": "🌱 ಉಳಿತಾಯ" if kn else "🌱 Savings",
    "upi": "📱 ಯುಪಿಐ ಪಾವತಿಗಳು" if kn else "📱 UPI Payments",
    "budget": "💵 ಬಜೆಟ್ ಯೋಜನೆ" if kn else "💵 Budget Planner",
    "fraud": "🛡️ ವಂಚನೆ ಸುರಕ್ಷತೆ" if kn else "🛡️ Fraud Safety",
    "assistant": "🤖 AI ಸಹಾಯಕ" if kn else "🤖 AI Assistant",
    "quiz": "📝 ಹಣಕಾಸಿನ ರಸಪ್ರಶ್ನೆ" if kn else "📝 Financial Quiz",
    "safety": "🔐 ಹಣಕಾಸಿನ ಸುರಕ್ಷತೆ" if kn else "🔐 Stay Financially Safe",
    "tip1": "ನಿಮ್ಮ OTP, UPI PIN ಅಥವಾ ಬ್ಯಾಂಕಿಂಗ್ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ." if kn else "Never share your OTP, UPI PIN or banking password.",
    "tip2": "ಪಾವತಿ ವಿನಂತಿಯನ್ನು ಅನುಮೋದಿಸುವ ಮೊದಲು ಪರಿಶೀಲಿಸಿ." if kn else "Verify payment requests before approving them.",
    "tip3": "ಸಂದೇಹಾಸ್ಪದ ಲಿಂಕ್‌ಗಳು ಮತ್ತು ಅಪರಿಚಿತ ಹಣದ ವಿನಂತಿಗಳನ್ನು ತಪ್ಪಿಸಿ." if kn else "Avoid suspicious links and unexpected money requests.",
    "tip4": "ವಂಚನೆಯ ಅನುಮಾನವಿದ್ದರೆ ಅಧಿಕೃತ ಬ್ಯಾಂಕ್ ಸಂಪರ್ಕ ಮಾರ್ಗಗಳನ್ನು ಬಳಸಿ." if kn else "Contact your bank through its official channels if you suspect fraud.",
    "notice": "ಫಿನ್‌ಸಾಥಿ ಒಂದು ಶೈಕ್ಷಣಿಕ ಅಪ್ಲಿಕೇಶನ್. ಇದು ನೈಜ ಬ್ಯಾಂಕ್ ಖಾತೆಗಳನ್ನು ಪ್ರವೇಶಿಸುವುದಿಲ್ಲ ಅಥವಾ ನೈಜ ಪಾವತಿಗಳನ್ನು ಮಾಡುವುದಿಲ್ಲ." if kn else "FinSaathi is an educational application. It does not access real bank accounts or make actual payments.",
}

# Website design
st.markdown("""
<style>
.stApp {background-color: #f5f9ff;}
header[data-testid="stHeader"] {background-color: #f5f9ff;}
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #145da0;
    padding-top: 10px;
}
.tagline {
    text-align: center;
    font-size: 20px;
    color: #328c87;
    margin-bottom: 25px;
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

# Sidebar
with st.sidebar:
    st.markdown("## 💰 FinSaathi")

    st.selectbox(
        T["language"],
        ["English", "ಕನ್ನಡ"],
        key="language"
    )

    st.caption(T["tagline"])
    st.divider()

    st.markdown(
        "ನಿಮ್ಮ ಹಣಕಾಸಿನ ಕಲಿಕೆಯ ಸಂಗಾತಿ"
        if kn else "Your Financial Learning Partner"
    )

    st.write(
        "ಬ್ಯಾಂಕಿಂಗ್, ಉಳಿತಾಯ, ಡಿಜಿಟಲ್ ಪಾವತಿಗಳು, ಬಜೆಟ್ ಮತ್ತು ವಂಚನೆ ಸುರಕ್ಷತೆಯನ್ನು ಕಲಿಯಿರಿ."
        if kn else
        "Learn banking, savings, digital payments, budgeting and fraud safety."
    )

# Main heading
st.markdown(
    f'<div class="main-title">💰 {T["title"]}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="tagline">{T["tagline"]}</div>',
    unsafe_allow_html=True
)

# Welcome section
st.markdown(
    f"""
    <div class="welcome">
        <h2>{T["welcome"]}</h2>
        <p>{T["intro"]}</p>
        <p>{T["description"]}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Learning modules
st.subheader("📚 " + T["explore"])
st.write(T["choose"])

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Banking.py", label=T["banking"])
    st.page_link("pages/Savings.py", label=T["savings"])
    st.page_link("pages/UPI.py", label=T["upi"])
    st.page_link("pages/Budget.py", label=T["budget"])

with col2:
    st.page_link("pages/Fraud_safety.py", label=T["fraud"])
    st.page_link("pages/AI_Assistant.py", label=T["assistant"])
    st.page_link("pages/Quiz.py", label=T["quiz"])

st.divider()

st.subheader(T["safety"])
for key in ["tip1", "tip2", "tip3", "tip4"]:
    st.markdown("- " + T[key])

st.info(T["notice"])
st.caption("© FinSaathi | " + T["tagline"])
