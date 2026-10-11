
import streamlit as st

LANGUAGES = ["English", "ಕನ್ನಡ", "हिन्दी", "मराठी"]

TRANSLATIONS = {
    "ಕನ್ನಡ": {
        "Home": "ಮುಖಪುಟ",
        "Banking": "ಬ್ಯಾಂಕಿಂಗ್",
        "Savings": "ಉಳಿತಾಯ",
        "UPI": "ಯುಪಿಐ",
        "Fraud Safety": "ವಂಚನೆ ಸುರಕ್ಷತೆ",
        "AI Assistant": "AI ಸಹಾಯಕ",
        "Budget": "ಬಜೆಟ್",
        "Quiz": "ರಸಪ್ರಶ್ನೆ",
        "Welcome": "ಸ್ವಾಗತ",
        "Learn Finance. Stay Safe.": "ಹಣಕಾಸು ಕಲಿಯಿರಿ. ಸುರಕ್ಷಿತವಾಗಿರಿ.",
        "Choose your language": "ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "Save Money": "ಹಣ ಉಳಿಸಿ",
        "Check Fraud": "ವಂಚನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ",
        "Ask a Question": "ಪ್ರಶ್ನೆ ಕೇಳಿ",
        "Income": "ಆದಾಯ",
        "Expenses": "ವೆಚ್ಚಗಳು",
        "Savings Goal": "ಉಳಿತಾಯದ ಗುರಿ",
        "Welcome to FinSaathi!": "ಫಿನ್‌ಸಾಥಿಗೆ ಸ್ವಾಗತ!",
        "Banking Basics": "ಬ್ಯಾಂಕಿಂಗ್ ಮೂಲಭೂತಗಳು",
        "UPI Safety": "ಯುಪಿಐ ಸುರಕ್ಷತೆ",
        "Budget Planner": "ಬಜೆಟ್ ಯೋಜಕ",
        "Explore": "ವೀಕ್ಷಿಸಿ",
        "Financial Knowledge Quiz": "ಹಣಕಾಸಿನ ಜ್ಞಾನ ರಸಪ್ರಶ್ನೆ",
    },
    "हिन्दी": {
        "Home": "होम",
        "Banking": "बैंकिंग",
        "Savings": "बचत",
        "UPI": "यूपीआई",
        "Fraud Safety": "धोखाधड़ी से सुरक्षा",
        "AI Assistant": "AI सहायक",
        "Budget": "बजट",
        "Quiz": "प्रश्नोत्तरी",
        "Welcome": "स्वागत है",
        "Learn Finance. Stay Safe.": "वित्त सीखें। सुरक्षित रहें।",
        "Choose your language": "अपनी भाषा चुनें",
        "Save Money": "पैसे बचाएं",
        "Check Fraud": "धोखाधड़ी जांचें",
        "Ask a Question": "प्रश्न पूछें",
        "Income": "आय",
        "Expenses": "खर्च",
        "Savings Goal": "बचत का लक्ष्य",
        "Welcome to FinSaathi!": "फिनसाथी में आपका स्वागत है!",
        "Banking Basics": "बैंकिंग की मूल बातें",
        "UPI Safety": "UPI सुरक्षा",
        "Budget Planner": "बजट योजनाकार",
        "Explore": "देखें",
        "Financial Knowledge Quiz": "वित्तीय ज्ञान प्रश्नोत्तरी",
    },
    "मराठी": {
        "Home": "मुख्यपृष्ठ",
        "Banking": "बँकिंग",
        "Savings": "बचत",
        "UPI": "यूपीआय",
        "Fraud Safety": "फसवणुकीपासून सुरक्षा",
        "AI Assistant": "AI सहाय्यक",
        "Budget": "अर्थसंकल्प",
        "Quiz": "प्रश्नमंजुषा",
        "Welcome": "स्वागत आहे",
        "Learn Finance. Stay Safe.": "आर्थिक ज्ञान शिका. सुरक्षित राहा.",
        "Choose your language": "तुमची भाषा निवडा",
        "Save Money": "पैसे वाचवा",
        "Check Fraud": "फसवणूक तपासा",
        "Ask a Question": "प्रश्न विचारा",
        "Income": "उत्पन्न",
        "Expenses": "खर्च",
        "Savings Goal": "बचतीचे उद्दिष्ट",
        "Welcome to FinSaathi!": "फिनसाथीमध्ये स्वागत आहे!",
        "Banking Basics": "बँकिंगची मूलतत्त्वे",
        "UPI Safety": "UPI सुरक्षा",
        "Budget Planner": "अर्थसंकल्प नियोजक",
        "Explore": "पहा",
        "Financial Knowledge Quiz": "आर्थिक ज्ञान प्रश्नमंजुषा",
    },
}


def get_selected_language():
    return st.session_state.get("language", "English")


def tr(text):
    language = get_selected_language()
    if language == "English":
        return text
    return TRANSLATIONS.get(language, {}).get(text, text)
