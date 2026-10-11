
import streamlit as st

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💙",
    layout="wide"
)

# Remember the selected language across page navigation
LANGUAGES = ["English", "ಕನ್ನಡ", "हिन्दी", "मराठी"]

if "language" not in st.session_state:
    st.session_state["language"] = "English"

def change_language():
    st.session_state["language"] = st.session_state["language_picker"]

st.sidebar.title("💙 FinSaathi")
st.sidebar.caption("Learn Finance. Stay Safe.")

st.sidebar.selectbox(
    "Choose your language / ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ",
    LANGUAGES,
    key="language_picker",
    index=LANGUAGES.index(st.session_state["language"]),
    on_change=change_language
)

# Keep the selected language available to every page
language = st.session_state["language"]

st.sidebar.markdown("---")
st.sidebar.subheader("📚 Menu")

pages = [
    ("🏠 Home", "app.py"),
    ("🏦 Banking", "pages/1_Banking.py"),
    ("💰 Savings", "pages/Savings.py"),
    ("📱 UPI", "pages/UPI.py"),
    ("🛡️ Fraud Safety", "pages/Fraud_Safety.py"),
    ("🤖 AI Assistant", "pages/AI_Assistant.py"),
    ("📊 Budget", "pages/Budget.py"),
    ("📝 Quiz", "pages/Quiz.py"),
]

for label, path in pages:
    st.sidebar.page_link(path, label=label)

# Home page text
HOME_TEXT = {
    "English": {
        "title": "Learn Finance. Stay Safe.",
        "welcome": "Welcome to FinSaathi!",
        "intro": "Your financial literacy companion for safer banking, smarter savings, and fraud awareness.",
        "banking": "Learn about bank accounts, ATMs, and banking services.",
        "savings": "Discover simple ways to save money.",
        "upi": "Learn how to use UPI safely.",
        "fraud": "Recognize suspicious messages and avoid online scams.",
        "assistant": "Get help with basic financial questions.",
        "budget": "Plan your income, expenses, and savings.",
        "quiz": "Test your financial knowledge.",
        "safety": "Never share your OTP, UPI PIN, or bank password."
    },
    "ಕನ್ನಡ": {
        "title": "ಹಣಕಾಸು ಕಲಿಯಿರಿ. ಸುರಕ್ಷಿತವಾಗಿರಿ.",
        "welcome": "ಫಿನ್‌ಸಾಥಿಗೆ ಸ್ವಾಗತ!",
        "intro": "ಸುರಕ್ಷಿತ ಬ್ಯಾಂಕಿಂಗ್, ಉತ್ತಮ ಉಳಿತಾಯ ಮತ್ತು ವಂಚನೆಗಳ ಬಗ್ಗೆ ತಿಳಿಯಲು ನಿಮ್ಮ ಸಹಾಯಕ.",
        "banking": "ಬ್ಯಾಂಕ್ ಖಾತೆ, ಎಟಿಎಂ ಮತ್ತು ಬ್ಯಾಂಕಿಂಗ್ ಸೇವೆಗಳ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ.",
        "savings": "ಹಣ ಉಳಿಸುವ ಸರಳ ವಿಧಾನಗಳನ್ನು ತಿಳಿಯಿರಿ.",
        "upi": "ಯುಪಿಐ ಅನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಬಳಸುವುದನ್ನು ಕಲಿಯಿರಿ.",
        "fraud": "ಸಂದೇಹಾಸ್ಪದ ಸಂದೇಶಗಳನ್ನು ಗುರುತಿಸಿ ಮತ್ತು ಆನ್‌ಲೈನ್ ವಂಚನೆಯನ್ನು ತಪ್ಪಿಸಿ.",
        "assistant": "ಹಣಕಾಸಿನ ಪ್ರಶ್ನೆಗಳಿಗೆ ಸಹಾಯ ಪಡೆಯಿರಿ.",
        "budget": "ನಿಮ್ಮ ಆದಾಯ, ಖರ್ಚು ಮತ್ತು ಉಳಿತಾಯವನ್ನು ಯೋಜಿಸಿ.",
        "quiz": "ನಿಮ್ಮ ಹಣಕಾಸಿನ ಜ್ಞಾನವನ್ನು ಪರೀಕ್ಷಿಸಿ.",
        "safety": "ನಿಮ್ಮ OTP, UPI PIN ಅಥವಾ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ."
    },
    "हिन्दी": {
        "title": "वित्त सीखें। सुरक्षित रहें।",
        "welcome": "फिनसाथी में आपका स्वागत है!",
        "intro": "सुरक्षित बैंकिंग, बेहतर बचत और धोखाधड़ी से बचने में आपका साथी।",
        "banking": "बैंक खाते, एटीएम और बैंकिंग सेवाओं के बारे में जानें।",
        "savings": "पैसे बचाने के सरल तरीके जानें।",
        "upi": "UPI का सुरक्षित उपयोग करना सीखें।",
        "fraud": "संदिग्ध संदेश पहचानें और ऑनलाइन धोखाधड़ी से बचें।",
        "assistant": "वित्तीय सवालों के लिए मदद लें।",
        "budget": "अपनी आय, खर्च और बचत की योजना बनाएं।",
        "quiz": "अपना वित्तीय ज्ञान जांचें।",
        "safety": "अपना OTP, UPI PIN या बैंक पासवर्ड किसी से साझा न करें।"
    },
    "मराठी": {
        "title": "आर्थिक ज्ञान शिका. सुरक्षित राहा.",
        "welcome": "फिनसाथीमध्ये स्वागत आहे!",
        "intro": "सुरक्षित बँकिंग, चांगली बचत आणि फसवणूक टाळण्यासाठी तुमचा साथी.",
        "banking": "बँक खाती, एटीएम आणि बँकिंग सेवांबद्दल जाणून घ्या.",
        "savings": "पैसे वाचवण्याचे सोपे मार्ग जाणून घ्या.",
        "upi": "UPI सुरक्षितपणे वापरायला शिका.",
        "fraud": "संशयास्पद संदेश ओळखा आणि ऑनलाइन फसवणूक टाळा.",
        "assistant": "आर्थिक प्रश्नांसाठी मदत मिळवा.",
        "budget": "तुमचे उत्पन्न, खर्च आणि बचतीचे नियोजन करा.",
        "quiz": "तुमचे आर्थिक ज्ञान तपासा.",
        "safety": "तुमचा OTP, UPI PIN किंवा बँक पासवर्ड कोणाशीही शेअर करू नका."
    }
}

t = HOME_TEXT.get(language, HOME_TEXT["English"])

st.title("💙 FinSaathi")
st.subheader(t["title"])
st.markdown("---")
st.header(t["welcome"])
st.write(t["intro"])

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏦 Banking")
    st.write(t["banking"])
    st.page_link("pages/1_Banking.py", label="🏦 Banking")

with col2:
    st.markdown("### 💰 Savings")
    st.write(t["savings"])
    st.page_link("pages/Savings.py", label="💰 Savings")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### 📱 UPI")
    st.write(t["upi"])
    st.page_link("pages/UPI.py", label="📱 UPI")

with col4:
    st.markdown("### 🛡️ Fraud Safety")
    st.write(t["fraud"])
    st.page_link("pages/Fraud_Safety.py", label="🛡️ Fraud Safety")

col5, col6 = st.columns(2)

with col5:
    st.markdown("### 🤖 AI Assistant")
    st.write(t["assistant"])
    st.page_link("pages/AI_Assistant.py", label="🤖 AI Assistant")

with col6:
    st.markdown("### 📊 Budget")
    st.write(t["budget"])
    st.page_link("pages/Budget.py", label="📊 Budget")

st.markdown("### 📝 Quiz")
st.write(t["quiz"])
st.page_link("pages/Quiz.py", label="📝 Quiz")

st.markdown("---")
st.warning("🔒 " + t["safety"])
st.caption("FinSaathi 💙")
