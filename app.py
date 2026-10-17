
import streamlit as st

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Website design
st.markdown("""
<style>
.stApp {
    background-color: #f5f9ff;
}

header[data-testid="stHeader"] {
    background-color: #f5f9ff;
}

.main-title {
    text-align: center;
    font-size: 48px;
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
    padding: 30px;
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
    st.caption("Learn Finance. Stay Safe.")
    st.divider()
    st.markdown("### Your Financial Learning Partner")
    st.write(
        "Learn banking, savings, digital payments, "
        "budgeting and fraud safety."
    )

# Main heading
st.markdown(
    '<div class="main-title">💰 FinSaathi</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">Learn Finance. Stay Safe.</div>',
    unsafe_allow_html=True
)

# Welcome section
st.markdown("""
<div class="welcome">
    <h2>Welcome to FinSaathi!</h2>
    <p>Your friendly companion for financial awareness.</p>
    <p>Learn to save money, use digital payments safely,
    understand banking and protect yourself from fraud.</p>
</div>
""", unsafe_allow_html=True)

# Learning modules
st.subheader("📚 Explore FinSaathi")
st.write("Choose a topic to get started.")

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/1_Banking.py",
        label="🏦 Banking Basics",
        icon="➡️"
    )
    st.page_link(
        "pages/Savings.py",
        label="🌱 Savings",
        icon="➡️"
    )
    st.page_link(
        "pages/UPI.py",
        label="📱 UPI Payments",
        icon="➡️"
    )
    st.page_link(
        "pages/Budget.py",
        label="💵 Budget Planner",
        icon="➡️"
    )

with col2:
    st.page_link(
        "pages/Fraud_Safety.py",
        label="🛡️ Fraud Safety",
        icon="➡️"
    )
    st.page_link(
        "pages/AI_Assistant.py",
        label="🤖 AI Assistant",
        icon="➡️"
    )
    st.page_link(
        "pages/Quiz.py",
        label="📝 Financial Quiz",
        icon="➡️"
    )

st.divider()

# Safety tips
st.subheader("🔐 Stay Financially Safe")

st.markdown("""
- Never share your OTP, UPI PIN or banking password.
- Verify payment requests before approving them.
- Avoid suspicious links and unexpected money requests.
- Contact your bank through its official channels if you suspect fraud.
""")

st.info(
    "FinSaathi is an educational application. "
    "It does not access real bank accounts or make actual payments."
)

st.caption("© FinSaathi | Learn Finance. Stay Safe.")
