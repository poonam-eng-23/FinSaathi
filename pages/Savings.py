
import streamlit as st

st.set_page_config(page_title="FinSaathi - Savings", page_icon="💰")

language = st.session_state.get("language_code", "English")

TEXT = {
    "English": {
        "title": "💰 Learn About Savings",
        "intro": "Small savings today can help you in the future.",
        "meaning": "What is saving?",
        "meaning_info": "Saving means keeping some money aside instead of spending all your income.",
        "ways": "Simple Ways to Save Money",
        "tip1": "Set aside a small amount regularly.",
        "tip2": "Make a list before shopping.",
        "tip3": "Avoid unnecessary expenses.",
        "goal": "Savings Goal Calculator",
        "income": "Monthly income (₹)",
        "expenses": "Monthly expenses (₹)",
        "result": "Money left after expenses",
        "suggestion": "Try to save a manageable amount regularly.",
        "invalid": "Expenses cannot be greater than income if you want to have money left over."
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "💰 ಉಳಿತಾಯದ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ",
        "intro": "ಇಂದಿನ ಸಣ್ಣ ಉಳಿತಾಯವು ನಿಮ್ಮ ಭವಿಷ್ಯಕ್ಕೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "meaning": "ಉಳಿತಾಯ ಎಂದರೇನು?",
        "meaning_info": "ನಿಮ್ಮ ಆದಾಯವನ್ನೆಲ್ಲ ಖರ್ಚು ಮಾಡದೆ ಸ್ವಲ್ಪ ಹಣವನ್ನು ಉಳಿಸಿಡುವುದೇ ಉಳಿತಾಯ.",
        "ways": "ಹಣ ಉಳಿಸುವ ಸರಳ ವಿಧಾನಗಳು",
        "tip1": "ನಿಯಮಿತವಾಗಿ ಸ್ವಲ್ಪ ಹಣವನ್ನು ಉಳಿಸಿ.",
        "tip2": "ವಸ್ತುಗಳನ್ನು ಖರೀದಿಸುವ ಮೊದಲು ಪಟ್ಟಿಯನ್ನು ತಯಾರಿಸಿ.",
        "tip3": "ಅನಗತ್ಯ ಖರ್ಚುಗಳನ್ನು ತಪ್ಪಿಸಿ.",
        "goal": "ಉಳಿತಾಯ ಗುರಿ ಲೆಕ್ಕಾಚಾರ",
        "income": "ಮಾಸಿಕ ಆದಾಯ (₹)",
        "expenses": "ಮಾಸಿಕ ಖರ್ಚುಗಳು (₹)",
        "result": "ಖರ್ಚಿನ ನಂತರ ಉಳಿದ ಹಣ",
        "suggestion": "ನಿಮಗೆ ಸಾಧ್ಯವಾದಷ್ಟು ಹಣವನ್ನು ನಿಯಮಿತವಾಗಿ ಉಳಿಸಲು ಪ್ರಯತ್ನಿಸಿ.",
        "invalid": "ಹಣ ಉಳಿಯಬೇಕಾದರೆ ಖರ್ಚು ಆದಾಯಕ್ಕಿಂತ ಹೆಚ್ಚಿರಬಾರದು."
    },
    "हिन्दी (Hindi)": {
        "title": "💰 बचत के बारे में जानें",
        "intro": "आज की छोटी बचत भविष्य में आपकी मदद कर सकती है।",
        "meaning": "बचत क्या है?",
        "meaning_info": "अपनी पूरी आय खर्च करने के बजाय कुछ पैसे अलग रखना बचत कहलाता है।",
        "ways": "पैसे बचाने के आसान तरीके",
        "tip1": "नियमित रूप से थोड़े पैसे बचाएँ।",
        "tip2": "खरीदारी से पहले सूची बनाएँ।",
        "tip3": "अनावश्यक खर्चों से बचें।",
        "goal": "बचत लक्ष्य कैलकुलेटर",
        "income": "मासिक आय (₹)",
        "expenses": "मासिक खर्च (₹)",
        "result": "खर्च के बाद बची राशि",
        "suggestion": "नियमित रूप से अपनी क्षमता के अनुसार बचत करें।",
        "invalid": "पैसे बचाने के लिए खर्च आय से अधिक नहीं होना चाहिए।"
    },
    "मराठी (Marathi)": {
        "title": "💰 बचतीबद्दल जाणून घ्या",
        "intro": "आजची छोटी बचत भविष्यात उपयोगी पडू शकते.",
        "meaning": "बचत म्हणजे काय?",
        "meaning_info": "आपले संपूर्ण उत्पन्न खर्च न करता काही पैसे बाजूला ठेवणे म्हणजे बचत.",
        "ways": "पैसे वाचवण्याचे सोपे मार्ग",
        "tip1": "नियमितपणे थोडे पैसे वाचवा.",
        "tip2": "खरेदीपूर्वी यादी तयार करा.",
        "tip3": "अनावश्यक खर्च टाळा.",
        "goal": "बचत ध्येय कॅल्क्युलेटर",
        "income": "मासिक उत्पन्न (₹)",
        "expenses": "मासिक खर्च (₹)",
        "result": "खर्चानंतर शिल्लक रक्कम",
        "suggestion": "आपल्या क्षमतेनुसार नियमित बचत करण्याचा प्रयत्न करा.",
        "invalid": "पैसे शिल्लक राहण्यासाठी खर्च उत्पन्नापेक्षा जास्त नसावा."
    }
}

T = TEXT.get(language, TEXT["English"])

st.title(T["title"])
st.write(T["intro"])

st.divider()

st.subheader(T["meaning"])
st.write(T["meaning_info"])

st.subheader(T["ways"])
st.write("1. " + T["tip1"])
st.write("2. " + T["tip2"])
st.write("3. " + T["tip3"])

st.divider()

st.subheader(T["goal"])

income = st.number_input(T["income"], min_value=0.0, step=500.0)
expenses = st.number_input(T["expenses"], min_value=0.0, step=500.0)

remaining = income - expenses

st.metric(T["result"], f"₹{remaining:,.2f}")

if remaining > 0:
    st.success(T["suggestion"])
elif remaining < 0:
    st.warning(T["invalid"])

if st.button("🏠 Home / ಮುಖಪುಟ / होम / मुख्यपृष्ठ"):
    st.switch_page("app.py")
