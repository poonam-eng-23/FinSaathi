
import streamlit as st
from translation import tr, LANGUAGES

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💙",
    layout="wide"
)

# ---------- PERSISTENT LANGUAGE ----------
if "language" not in st.session_state:
    st.session_state["language"] = "English"

def update_language():
    st.session_state["language"] = st.session_state["language_picker"]

def get_text(english, kannada=None, hindi=None, marathi=None):
    language = st.session_state["language"]
    direct = {
        "ಕನ್ನಡ": kannada,
        "हिन्दी": hindi,
        "मराठी": marathi,
    }
    return direct.get(language) or tr(english)

st.sidebar.title("💙 FinSaathi")
st.sidebar.caption("Learn Finance. Stay Safe.")

# Keep the widget key separate from the shared language value
if "language_picker" not in st.session_state:
    st.session_state["language_picker"] = st.session_state["language"]

st.sidebar.selectbox(
    "Choose your language / ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ",
    LANGUAGES,
    key="language_picker",
    on_change=update_language
)

language = st.session_state["language"]

# ---------- NAVIGATION ----------
st.sidebar.markdown("---")
st.sidebar.subheader(get_text(
    "Menu", "ಮೆನು", "मेनू", "मेनू"
))

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

# ---------- HOME ----------
st.title("💙 FinSaathi")

st.subheader(get_text(
    "Learn Finance. Stay Safe.",
    "ಹಣಕಾಸು ಕಲಿಯಿರಿ. ಸುರಕ್ಷಿತವಾಗಿರಿ.",
    "वित्त सीखें। सुरक्षित रहें।",
    "आर्थिक ज्ञान शिका. सुरक्षित राहा."
))

st.markdown("---")

st.header(get_text(
    "Welcome to FinSaathi!",
    "ಫಿನ್‌ಸಾಥಿಗೆ ಸ್ವಾಗತ!",
    "फिनसाथी में आपका स्वागत है!",
    "फिनसाथीमध्ये स्वागत आहे!"
))

st.write(get_text(
    "Your financial literacy companion for safer banking, smarter savings, and fraud awareness.",
    "ಸುರಕ್ಷಿತ ಬ್ಯಾಂಕಿಂಗ್, ಉತ್ತಮ ಉಳಿತಾಯ ಮತ್ತು ವಂಚನೆಗಳ ಬಗ್ಗೆ ತಿಳಿಯಲು ನಿಮ್ಮ ಸಹಾಯಕ.",
    "सुरक्षित बैंकिंग, बेहतर बचत और धोखाधड़ी से बचने में आपका साथी।",
    "सुरक्षित बँकिंग, चांगली बचत आणि फसवणूक टाळण्यासाठी तुमचा साथी."
))

features = [
    (
        "🏦 Banking",
        "pages/1_Banking.py",
        "Learn about bank accounts, ATMs, and banking services.",
        "ಬ್ಯಾಂಕ್ ಖಾತೆ, ಎಟಿಎಂ ಮತ್ತು ಬ್ಯಾಂಕಿಂಗ್ ಸೇವೆಗಳ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ.",
        "बैंक खाते, एटीएम और बैंकिंग सेवाओं के बारे में जानें।",
        "बँक खाते, एटीएम आणि बँकिंग सेवांबद्दल जाणून घ्या."
    ),
    (
        "💰 Savings",
        "pages/Savings.py",
        "Discover simple ways to save money.",
        "ಹಣ ಉಳಿಸುವ ಸರಳ ವಿಧಾನಗಳನ್ನು ತಿಳಿಯಿರಿ.",
        "पैसे बचाने के सरल तरीके जानें।",
        "पैसे वाचवण्याचे सोपे मार्ग जाणून घ्या."
    ),
    (
        "📱 UPI",
        "pages/UPI.py",
        "Learn how to use UPI safely.",
        "ಯುಪಿಐ ಅನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಬಳಸುವುದನ್ನು ಕಲಿಯಿರಿ.",
        "UPI का सुरक्षित उपयोग करना सीखें।",
        "UPI सुरक्षितपणे वापरायला शिका."
    ),
    (
        "🛡️ Fraud Safety",
        "pages/Fraud_Safety.py",
        "Recognize suspicious messages and avoid online scams.",
        "ಸಂದೇಹಾಸ್ಪದ ಸಂದೇಶಗಳನ್ನು ಗುರುತಿಸಿ ಮತ್ತು ಆನ್‌ಲೈನ್ ವಂಚನೆಯನ್ನು ತಪ್ಪಿಸಿ.",
        "संदिग्ध संदेश पहचानें और ऑनलाइन धोखाधड़ी से बचें।",
        "संशयास्पद संदेश ओळखा आणि ऑनलाइन फसवणूक टाळा."
    ),
    (
        "🤖 AI Assistant",
        "pages/AI_Assistant.py",
        "Get help with basic financial questions.",
        "ಹಣಕಾಸಿನ ಪ್ರಶ್ನೆಗಳಿಗೆ ಸಹಾಯ ಪಡೆಯಿರಿ.",
        "वित्तीय सवालों के लिए मदद लें।",
        "आर्थिक प्रश्नांसाठी मदत मिळवा."
    ),
    (
        "📊 Budget",
        "pages/Budget.py",
        "Plan your income, expenses, and savings.",
        "ನಿಮ್ಮ ಆದಾಯ, ಖರ್ಚು ಮತ್ತು ಉಳಿತಾಯವನ್ನು ಯೋಜಿಸಿ.",
        "अपनी आय, खर्च और बचत की योजना बनाएं।",
        "तुमचे उत्पन्न, खर्च आणि बचतीचे नियोजन करा."
    ),
    (
        "📝 Quiz",
        "pages/Quiz.py",
        "Test your financial knowledge.",
        "ನಿಮ್ಮ ಹಣಕಾಸಿನ ಜ್ಞಾನವನ್ನು ಪರೀಕ್ಷಿಸಿ.",
        "अपना वित्तीय ज्ञान जांचें।",
        "तुमचे आर्थिक ज्ञान तपासा."
    ),
]

for start in range(0, len(features), 2):
    columns = st.columns(2)
    for column, feature in zip(columns, features[start:start + 2]):
        title, path, en, kn, hi, mr = feature
        with column:
            st.markdown(f"### {title}")
            st.write(get_text(en, kn, hi, mr))
            st.page_link(path, label=get_text(
                "Explore", "ವೀಕ್ಷಿಸಿ", "देखें", "पहा"
            ))

st.markdown("---")
st.warning(get_text(
    "🔒 Never share your OTP, UPI PIN, or bank password with anyone.",
    "🔒 ನಿಮ್ಮ OTP, UPI PIN ಅಥವಾ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ.",
    "🔒 अपना OTP, UPI PIN या बैंक पासवर्ड किसी से साझा न करें।",
    "🔒 तुमचा OTP, UPI PIN किंवा बँक पासवर्ड कोणाशीही शेअर करू नका."
))

st.caption("FinSaathi — Learn Finance. Stay Safe. 💙")

