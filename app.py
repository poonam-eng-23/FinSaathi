
import streamlit as st

st.set_page_config(
    page_title="FinSaathi",
    page_icon="💰",
    layout="centered"
)

# All home-page translations
LANGUAGES = {
    "English": {
        "title": "💰 FinSaathi",
        "tagline": "Learn Finance. Stay Safe.",
        "intro": "A simple financial literacy app for everyone.",
        "choose": "🌐 Choose Your Language",
        "select": "Select language",
        "selected": "Selected language",
        "learn": "📚 Learn & Explore",
        "choose_module": "Choose a module to learn:",
        "banking": "🏦 Banking",
        "savings": "💰 Savings",
        "upi": "📱 UPI & Payments",
        "fraud": "🛡️ Fraud Safety",
        "budget": "📊 Budget",
        "assistant": "🤖 AI Assistant",
        "quiz": "📝 Financial Quiz",
        "tip_title": "🚨 Today's Safety Tip",
        "tip": "Never share your OTP, UPI PIN, ATM PIN or password with anyone.",
        "info": "💡 FinSaathi helps you learn banking, savings, digital payments, budgeting and fraud protection in simple language.",
        "footer": "FinSaathi – Learn Finance. Stay Safe. 💰"
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "💰 ಫಿನ್‌ಸಾಥಿ",
        "tagline": "ಹಣಕಾಸು ಕಲಿಯಿರಿ. ಸುರಕ್ಷಿತವಾಗಿರಿ.",
        "intro": "ಎಲ್ಲರಿಗೂ ಸರಳವಾದ ಹಣಕಾಸಿನ ಅರಿವು ನೀಡುವ ಅಪ್ಲಿಕೇಶನ್.",
        "choose": "🌐 ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "select": "ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "selected": "ಆಯ್ಕೆ ಮಾಡಿದ ಭಾಷೆ",
        "learn": "📚 ಕಲಿಯಿರಿ ಮತ್ತು ತಿಳಿಯಿರಿ",
        "choose_module": "ಕಲಿಯಲು ಒಂದು ವಿಭಾಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "banking": "🏦 ಬ್ಯಾಂಕಿಂಗ್",
        "savings": "💰 ಉಳಿತಾಯ",
        "upi": "📱 ಯುಪಿಐ ಮತ್ತು ಪಾವತಿಗಳು",
        "fraud": "🛡️ ವಂಚನೆಗಳಿಂದ ಸುರಕ್ಷತೆ",
        "budget": "📊 ಬಜೆಟ್",
        "assistant": "🤖 ಎಐ ಸಹಾಯಕ",
        "quiz": "📝 ಹಣಕಾಸಿನ ರಸಪ್ರಶ್ನೆ",
        "tip_title": "🚨 ಇಂದಿನ ಸುರಕ್ಷತಾ ಸಲಹೆ",
        "tip": "ನಿಮ್ಮ ಒಟಿಪಿ, ಯುಪಿಐ ಪಿನ್, ಎಟಿಎಂ ಪಿನ್ ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ.",
        "info": "💡 ಫಿನ್‌ಸಾಥಿ ಬ್ಯಾಂಕಿಂಗ್, ಉಳಿತಾಯ, ಡಿಜಿಟಲ್ ಪಾವತಿಗಳು, ಬಜೆಟ್ ಮತ್ತು ಆರ್ಥಿಕ ವಂಚನೆಗಳಿಂದ ರಕ್ಷಣೆ ಪಡೆಯುವುದನ್ನು ಸರಳವಾಗಿ ಕಲಿಸುತ್ತದೆ.",
        "footer": "ಫಿನ್‌ಸಾಥಿ – ಹಣಕಾಸು ಕಲಿಯಿರಿ. ಸುರಕ್ಷಿತವಾಗಿರಿ. 💰"
    },
    "हिन्दी (Hindi)": {
        "title": "💰 फिनसाथी",
        "tagline": "वित्त सीखें। सुरक्षित रहें।",
        "intro": "सभी के लिए एक सरल वित्तीय साक्षरता ऐप।",
        "choose": "🌐 अपनी भाषा चुनें",
        "select": "भाषा चुनें",
        "selected": "चुनी गई भाषा",
        "learn": "📚 सीखें और जानें",
        "choose_module": "सीखने के लिए एक विषय चुनें:",
        "banking": "🏦 बैंकिंग",
        "savings": "💰 बचत",
        "upi": "📱 यूपीआई और भुगतान",
        "fraud": "🛡️ धोखाधड़ी से सुरक्षा",
        "budget": "📊 बजट",
        "assistant": "🤖 एआई सहायक",
        "quiz": "📝 वित्तीय प्रश्नोत्तरी",
        "tip_title": "🚨 आज की सुरक्षा सलाह",
        "tip": "अपना ओटीपी, यूपीआई पिन, एटीएम पिन या पासवर्ड किसी के साथ साझा न करें।",
        "info": "💡 फिनसाथी आपको बैंकिंग, बचत, डिजिटल भुगतान, बजट और वित्तीय धोखाधड़ी से बचाव के बारे में सरल भाषा में सिखाता है।",
        "footer": "फिनसाथी – वित्त सीखें। सुरक्षित रहें। 💰"
    },
    "मराठी (Marathi)": {
        "title": "💰 फिनसाथी",
        "tagline": "आर्थिक ज्ञान मिळवा. सुरक्षित राहा.",
        "intro": "प्रत्येकासाठी एक सोपे आर्थिक साक्षरता अॅप.",
        "choose": "🌐 तुमची भाषा निवडा",
        "select": "भाषा निवडा",
        "selected": "निवडलेली भाषा",
        "learn": "📚 शिका आणि जाणून घ्या",
        "choose_module": "शिकण्यासाठी एक विभाग निवडा:",
        "banking": "🏦 बँकिंग",
        "savings": "💰 बचत",
        "upi": "📱 यूपीआय आणि पेमेंट",
        "fraud": "🛡️ फसवणुकीपासून संरक्षण",
        "budget": "📊 अर्थसंकल्प",
        "assistant": "🤖 एआय सहाय्यक",
        "quiz": "📝 आर्थिक प्रश्नमंजुषा",
        "tip_title": "🚨 आजचा सुरक्षिततेचा सल्ला",
        "tip": "तुमचा ओटीपी, यूपीआय पिन, एटीएम पिन किंवा पासवर्ड कोणालाही सांगू नका.",
        "info": "💡 फिनसाथी तुम्हाला बँकिंग, बचत, डिजिटल पेमेंट, बजेट आणि आर्थिक फसवणुकीपासून संरक्षण याबद्दल सोप्या भाषेत शिकवते.",
        "footer": "फिनसाथी – आर्थिक ज्ञान मिळवा. सुरक्षित राहा. 💰"
    }
}

# Language selector
st.title("💰 FinSaathi")

language = st.selectbox(
    "🌐 Select language / ಭಾಷೆ / भाषा",
    list(LANGUAGES.keys()),
    key="language_selector"
)

# Save language so other pages can use it
st.session_state["language_code"] = language
T = LANGUAGES[language]

st.subheader(T["tagline"])
st.write(T["intro"])

st.divider()

st.header(T["choose"])
st.success(f'{T["selected"]}: {language}')

st.divider()

st.header(T["learn"])
st.write(T["choose_module"])

if st.button(T["banking"], use_container_width=True):
    st.switch_page("pages/1_Banking.py")

if st.button(T["savings"], use_container_width=True):
    st.switch_page("pages/Savings.py")

if st.button(T["upi"], use_container_width=True):
    st.switch_page("pages/UPI.py")

if st.button(T["fraud"], use_container_width=True):
    st.switch_page("pages/Fraud_safety.py")

if st.button(T["budget"], use_container_width=True):
    st.switch_page("pages/Budget.py")

if st.button(T["assistant"], use_container_width=True):
    st.switch_page("pages/AI_Assistant.py")

if st.button(T["quiz"], use_container_width=True):
    st.switch_page("pages/Quiz.py")

st.divider()

st.header(T["tip_title"])
st.warning(T["tip"])

st.divider()

st.info(T["info"])
st.caption(T["footer"])
