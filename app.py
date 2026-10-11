
import streamlit as st
from translation import tr

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💙",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "language" not in st.session_state:
    st.session_state.language = "English"

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# ---------- LANGUAGE ----------
st.sidebar.title("💙 FinSaathi")
st.sidebar.caption("Learn Finance. Stay Safe.")

language = st.sidebar.selectbox(
    "Choose Language / भाषा ಆಯ್ಕೆಮಾಡಿ",
    ["English", "ಕನ್ನಡ", "हिन्दी", "मराठी"],
    index=(
        ["English", "ಕನ್ನಡ", "हिन्दी", "मराठी"].index(
            st.session_state.language
        )
        if st.session_state.language
        in ["English", "ಕನ್ನಡ", "हिन्दी", "मराठी"]
        else 0
    )
)

st.session_state.language = language

# ---------- NAVIGATION ----------
st.sidebar.markdown("---")
st.sidebar.subheader("📚 Menu")

pages = {
    "🏠 Home": None,
    "🏦 Banking": "pages/1_Banking.py",
    "💰 Savings": "pages/Savings.py",
    "📱 UPI": "pages/UPI.py",
    "🛡️ Fraud Safety": "pages/fraud_safety.py",
    "🤖 AI Assistant": "pages/AI_Assistant.py",
    "📊 Budget": "pages/Budget.py",
    "📝 Quiz": "pages/Quiz.py",
}

for label, path in pages.items():
    if path is None:
        st.sidebar.page_link("app.py", label=label)
    else:
        st.sidebar.page_link(path, label=label)

# ---------- HOME PAGE ----------
st.title("💙 FinSaathi")
st.subheader("Learn Finance. Stay Safe.")

if language == "ಕನ್ನಡ":
    st.write("ಗ್ರಾಮೀಣ ಕುಟುಂಬಗಳಿಗಾಗಿ ಹಣಕಾಸಿನ ಜಾಗೃತಿ ಅಪ್ಲಿಕೇಶನ್.")
    st.info("ಹಣವನ್ನು ತಿಳಿಯಿರಿ, ಸುರಕ್ಷಿತವಾಗಿ ಉಳಿಸಿ ಮತ್ತು ಮೋಸಗಳಿಂದ ದೂರವಿರಿ.")
elif language == "हिन्दी":
    st.write("ग्रामीण परिवारों के लिए वित्तीय जागरूकता ऐप।")
    st.info("पैसे के बारे में सीखें, बचत करें और धोखाधड़ी से सुरक्षित रहें।")
elif language == "मराठी":
    st.write("ग्रामीण कुटुंबांसाठी आर्थिक साक्षरता अ‍ॅप.")
    st.info("आर्थिक गोष्टी शिका, बचत करा आणि फसवणुकीपासून सुरक्षित राहा.")
else:
    st.write(
        "A financial literacy awareness app for rural households."
    )
    st.info(
        "Learn about money, build savings habits, and stay safe from scams."
    )

st.markdown("---")

# ---------- WELCOME ----------
if language == "ಕನ್ನಡ":
    st.header("ನಿಮ್ಮ ಹಣಕಾಸಿನ ಪ್ರಯಾಣಕ್ಕೆ ಸ್ವಾಗತ! 👋")
    st.write("ನೀವು ಇಂದು ಏನು ಕಲಿಯಲು ಬಯಸುತ್ತೀರಿ?")
elif language == "हिन्दी":
    st.header("आपकी वित्तीय यात्रा में आपका स्वागत है! 👋")
    st.write("आज आप क्या सीखना चाहते हैं?")
elif language == "मराठी":
    st.header("तुमच्या आर्थिक प्रवासात स्वागत आहे! 👋")
    st.write("आज तुम्हाला काय शिकायचे आहे?")
else:
    st.header("Welcome to your financial journey! 👋")
    st.write("What would you like to learn today?")

# ---------- FEATURE CARDS ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏦 Banking Basics")
    if language == "ಕನ್ನಡ":
        st.write("ಬ್ಯಾಂಕ್ ಖಾತೆ, ಎಟಿಎಂ ಮತ್ತು ಬ್ಯಾಂಕಿಂಗ್ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ.")
    elif language == "हिन्दी":
        st.write("बैंक खाते, एटीएम और बैंकिंग के बारे में जानें।")
    elif language == "मराठी":
        st.write("बँक खाते, एटीएम आणि बँकिंगबद्दल जाणून घ्या.")
    else:
        st.write("Learn about bank accounts, ATMs, and banking.")

    st.page_link(
        "pages/1_Banking.py",
        label="Explore Banking",
        icon="🏦"
    )

with col2:
    st.markdown("### 💰 Savings")
    if language == "ಕನ್ನಡ":
        st.write("ಹಣ ಉಳಿಸುವ ಸರಳ ವಿಧಾನಗಳನ್ನು ಕಲಿಯಿರಿ.")
    elif language == "हिन्दी":
        st.write("पैसे बचाने के आसान तरीके सीखें।")
    elif language == "मराठी":
        st.write("पैसे वाचवण्याचे सोपे मार्ग शिका.")
    else:
        st.write("Learn simple ways to save money.")

    st.page_link(
        "pages/Savings.py",
        label="Explore Savings",
        icon="💰"
    )

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 📱 UPI Safety")
    if language == "ಕನ್ನಡ":
        st.write("ಯುಪಿಐ ಬಳಸುವಾಗ ಸುರಕ್ಷಿತವಾಗಿರುವುದನ್ನು ಕಲಿಯಿರಿ.")
    elif language == "हिन्दी":
        st.write("UPI का सुरक्षित उपयोग करना सीखें।")
    elif language == "मराठी":
        st.write("UPI सुरक्षितपणे वापरायला शिका.")
    else:
        st.write("Learn how to use UPI safely.")

    st.page_link(
        "pages/UPI.py",
        label="Explore UPI",
        icon="📱"
    )

with col4:
    st.markdown("### 🛡️ Fraud Safety")
    if language == "ಕನ್ನಡ":
        st.write("ಆನ್‌ಲೈನ್ ವಂಚನೆಗಳನ್ನು ಗುರುತಿಸಿ ಮತ್ತು ತಪ್ಪಿಸಿ.")
    elif language == "हिन्दी":
        st.write("ऑनलाइन धोखाधड़ी को पहचानें और उससे बचें।")
    elif language == "मराठी":
        st.write("ऑनलाइन फसवणूक ओळखा आणि टाळा.")
    else:
        st.write("Recognize and avoid online scams.")

    st.page_link(
        "pages/fraud_safety.py",
        label="Explore Fraud Safety",
        icon="🛡️"
    )

col5, col6 = st.columns(2)

with col5:
    st.markdown("### 🤖 AI Assistant")
    if language == "ಕನ್ನಡ":
        st.write("ಹಣಕಾಸಿನ ಪ್ರಶ್ನೆಗಳಿಗೆ ಸಹಾಯ ಪಡೆಯಿರಿ.")
    elif language == "हिन्दी":
        st.write("वित्तीय सवालों के जवाब पाने में मदद लें।")
    elif language == "मराठी":
        st.write("आर्थिक प्रश्नांसाठी मदत मिळवा.")
    else:
        st.write("Get help with basic financial questions.")

    st.page_link(
        "pages/AI_Assistant.py",
        label="Ask Saathi",
        icon="🤖"
    )

with col6:
    st.markdown("### 📊 Budget Planner")
    if language == "ಕನ್ನಡ":
        st.write("ನಿಮ್ಮ ಆದಾಯ ಮತ್ತು ಖರ್ಚುಗಳನ್ನು ಯೋಜಿಸಿ.")
    elif language == "हिन्दी":
        st.write("अपनी आय और खर्च की योजना बनाएं।")
    elif language == "मराठी":
        st.write("तुमचे उत्पन्न आणि खर्च यांचे नियोजन करा.")
    else:
        st.write("Plan your income and expenses.")

    st.page_link(
        "pages/Budget.py",
        label="Plan Budget",
        icon="📊"
    )

st.markdown("---")

# ---------- SAFETY REMINDER ----------
if language == "ಕನ್ನಡ":
    st.warning(
        "🔒 ನಿಮ್ಮ OTP, UPI PIN ಅಥವಾ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ."
    )
elif language == "हिन्दी":
    st.warning(
        "🔒 अपना OTP, UPI PIN या बैंक पासवर्ड किसी के साथ साझा न करें।"
    )
elif language == "मराठी":
    st.warning(
        "🔒 तुमचा OTP, UPI PIN किंवा बँक पासवर्ड कोणाशीही शेअर करू नका."
    )
else:
    st.warning(
        "🔒 Never share your OTP, UPI PIN, or bank password with anyone."
    )

st.caption("FinSaathi — Learn Finance. Stay Safe. 💙")
