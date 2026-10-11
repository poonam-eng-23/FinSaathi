
import streamlit as st
from translation import tr

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💙",
    layout="wide"
)

# ---------- LANGUAGE ----------
LANGUAGES = ["English", "ಕನ್ನಡ", "हिन्दी", "मराठी"]

if "language" not in st.session_state:
    st.session_state.language = "English"

st.sidebar.title("💙 FinSaathi")
st.sidebar.caption("Learn Finance. Stay Safe.")

selected_language = st.sidebar.selectbox(
    "Choose your language / ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ",
    LANGUAGES,
    index=LANGUAGES.index(st.session_state.language)
    if st.session_state.language in LANGUAGES else 0
)

st.session_state.language = selected_language

# ---------- TRANSLATED HOME CONTENT ----------
HOME_CONTENT = {
    "English": {
        "subtitle": "A Financial Literacy Awareness App for Rural Households",
        "welcome": "Welcome to your financial journey! 👋",
        "intro": "Learn about money, save wisely, and stay safe from online fraud.",
        "banking": "Learn about bank accounts, ATMs, and banking services.",
        "savings": "Discover simple and useful ways to save money.",
        "upi": "Learn how to use UPI safely and responsibly.",
        "fraud": "Recognize suspicious messages and avoid online scams.",
        "assistant": "Get help with basic financial questions.",
        "budget": "Plan your income, expenses, and savings.",
        "quiz": "Test your financial knowledge with a fun quiz.",
        "safety": "Never share your OTP, UPI PIN, or bank password with anyone.",
        "explore": "Explore",
    },
    "ಕನ್ನಡ": {
        "subtitle": "ಗ್ರಾಮೀಣ ಕುಟುಂಬಗಳಿಗಾಗಿ ಹಣಕಾಸಿನ ಅರಿವು ಮೂಡಿಸುವ ಅಪ್ಲಿಕೇಶನ್",
        "welcome": "ನಿಮ್ಮ ಹಣಕಾಸಿನ ಪ್ರಯಾಣಕ್ಕೆ ಸ್ವಾಗತ! 👋",
        "intro": "ಹಣದ ಬಗ್ಗೆ ಕಲಿಯಿರಿ, ಉಳಿತಾಯ ಮಾಡಿ ಮತ್ತು ಆನ್‌ಲೈನ್ ವಂಚನೆಯಿಂದ ಸುರಕ್ಷಿತರಾಗಿರಿ.",
        "banking": "ಬ್ಯಾಂಕ್ ಖಾತೆ, ಎಟಿಎಂ ಮತ್ತು ಬ್ಯಾಂಕಿಂಗ್ ಸೇವೆಗಳ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ.",
        "savings": "ಹಣ ಉಳಿಸುವ ಸರಳ ಮತ್ತು ಉಪಯುಕ್ತ ವಿಧಾನಗಳನ್ನು ತಿಳಿಯಿರಿ.",
        "upi": "ಯುಪಿಐ ಅನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಬಳಸುವುದನ್ನು ಕಲಿಯಿರಿ.",
        "fraud": "ಸಂದೇಹಾಸ್ಪದ ಸಂದೇಶಗಳನ್ನು ಗುರುತಿಸಿ ಮತ್ತು ಆನ್‌ಲೈನ್ ವಂಚನೆಯನ್ನು ತಪ್ಪಿಸಿ.",
        "assistant": "ಹಣಕಾಸಿನ ಮೂಲಭೂತ ಪ್ರಶ್ನೆಗಳಿಗೆ ಸಹಾಯ ಪಡೆಯಿರಿ.",
        "budget": "ನಿಮ್ಮ ಆದಾಯ, ಖರ್ಚು ಮತ್ತು ಉಳಿತಾಯವನ್ನು ಯೋಜಿಸಿ.",
        "quiz": "ರಸಪ್ರಶ್ನೆಯ ಮೂಲಕ ನಿಮ್ಮ ಹಣಕಾಸಿನ ಜ್ಞಾನವನ್ನು ಪರೀಕ್ಷಿಸಿ.",
        "safety": "ನಿಮ್ಮ OTP, UPI PIN ಅಥವಾ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ.",
        "explore": "ವೀಕ್ಷಿಸಿ",
    },
    "हिन्दी": {
        "subtitle": "ग्रामीण परिवारों के लिए वित्तीय जागरूकता ऐप",
        "welcome": "आपकी वित्तीय यात्रा में आपका स्वागत है! 👋",
        "intro": "पैसों के बारे में सीखें, बचत करें और ऑनलाइन धोखाधड़ी से सुरक्षित रहें।",
        "banking": "बैंक खाते, एटीएम और बैंकिंग सेवाओं के बारे में जानें।",
        "savings": "पैसे बचाने के सरल और उपयोगी तरीके जानें।",
        "upi": "UPI का सुरक्षित उपयोग करना सीखें।",
        "fraud": "संदिग्ध संदेश पहचानें और ऑनलाइन धोखाधड़ी से बचें।",
        "assistant": "वित्तीय सवालों के लिए सहायता प्राप्त करें।",
        "budget": "अपनी आय, खर्च और बचत की योजना बनाएं।",
        "quiz": "रोचक प्रश्नोत्तरी से अपना वित्तीय ज्ञान जांचें।",
        "safety": "अपना OTP, UPI PIN या बैंक पासवर्ड किसी के साथ साझा न करें।",
        "explore": "देखें",
    },
    "मराठी": {
        "subtitle": "ग्रामीण कुटुंबांसाठी आर्थिक साक्षरता जागरूकता अ‍ॅप",
        "welcome": "तुमच्या आर्थिक प्रवासात स्वागत आहे! 👋",
        "intro": "पैशांबद्दल शिका, बचत करा आणि ऑनलाइन फसवणुकीपासून सुरक्षित राहा.",
        "banking": "बँक खाते, एटीएम आणि बँकिंग सेवांबद्दल जाणून घ्या.",
        "savings": "पैसे वाचवण्याचे सोपे आणि उपयुक्त मार्ग शिका.",
        "upi": "UPI सुरक्षितपणे वापरायला शिका.",
        "fraud": "संशयास्पद संदेश ओळखा आणि ऑनलाइन फसवणूक टाळा.",
        "assistant": "आर्थिक प्रश्नांसाठी मदत मिळवा.",
        "budget": "तुमचे उत्पन्न, खर्च आणि बचतीचे नियोजन करा.",
        "quiz": "प्रश्नमंजुषेद्वारे तुमचे आर्थिक ज्ञान तपासा.",
        "safety": "तुमचा OTP, UPI PIN किंवा बँक पासवर्ड कोणाशीही शेअर करू नका.",
        "explore": "पहा",
    },
}

content = HOME_CONTENT[selected_language]

# ---------- SIDEBAR NAVIGATION ----------
st.sidebar.markdown("---")
st.sidebar.subheader("📚 Menu")

pages = [
    ("🏦 Banking", "pages/1_Banking.py"),
    ("💰 Savings", "pages/Savings.py"),
    ("📱 UPI", "pages/UPI.py"),
    ("🛡️ Fraud Safety", "pages/Fraud_Safety.py"),
    ("🤖 AI Assistant", "pages/AI_Assistant.py"),
    ("📊 Budget", "pages/Budget.py"),
    ("📝 Quiz", "pages/Quiz.py"),
]

st.sidebar.page_link("app.py", label="🏠 Home")

for label, path in pages:
    st.sidebar.page_link(path, label=label)

# ---------- HOME PAGE ----------
st.title("💙 FinSaathi")
st.subheader(content["subtitle"])
st.markdown("---")

st.header(content["welcome"])
st.write(content["intro"])

# ---------- FEATURE CARDS ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏦 Banking Basics")
    st.write(content["banking"])
    st.page_link(
        "pages/1_Banking.py",
        label=f'{content["explore"]} Banking',
        icon="🏦"
    )

with col2:
    st.markdown("### 💰 Savings")
    st.write(content["savings"])
    st.page_link(
        "pages/Savings.py",
        label=f'{content["explore"]} Savings',
        icon="💰"
    )

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 📱 UPI Safety")
    st.write(content["upi"])
    st.page_link(
        "pages/UPI.py",
        label=f'{content["explore"]} UPI',
        icon="📱"
    )

with col4:
    st.markdown("### 🛡️ Fraud Safety")
    st.write(content["fraud"])
    st.page_link(
        "pages/Fraud_Safety.py",
        label=f'{content["explore"]} Fraud Safety',
        icon="🛡️"
    )

col5, col6 = st.columns(2)

with col5:
    st.markdown("### 🤖 AI Assistant")
    st.write(content["assistant"])
    st.page_link(
        "pages/AI_Assistant.py",
        label="AI Assistant",
        icon="🤖"
    )

with col6:
    st.markdown("### 📊 Budget Planner")
    st.write(content["budget"])
    st.page_link(
        "pages/Budget.py",
        label=f'{content["explore"]} Budget',
        icon="📊"
    )

st.markdown("### 📝 Financial Knowledge Quiz")
st.write(content["quiz"])
st.page_link(
    "pages/Quiz.py",
    label=f'{content["explore"]} Quiz',
    icon="📝"
)

st.markdown("---")
st.warning("🔒 " + content["safety"])
st.caption("FinSaathi — Learn Finance. Stay Safe. 💙")
