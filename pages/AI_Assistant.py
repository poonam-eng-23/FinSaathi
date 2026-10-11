
import streamlit as st

st.set_page_config(page_title="FinSaathi Assistant", page_icon="🤖")

language = st.session_state.get("language_code", "English")

TEXT = {
    "English": {
        "title": "🤖 FinSaathi Assistant",
        "subtitle": "Ask simple questions about money and banking.",
        "question": "Type your question",
        "button": "Get Answer",
        "home": "🏠 Back to Home",
        "empty": "Please type a question first.",
        "fallback": "I could not find a matching answer. Please ask about banking, savings, UPI, budgeting, or fraud safety.",
        "bank": "A bank account helps you keep money safely. You can deposit and withdraw money through a bank or ATM.",
        "save": "Save regularly, set a savings goal, and keep some money aside for emergencies.",
        "upi": "UPI lets you transfer money digitally. Never share your UPI PIN. You enter your PIN only when you are authorising a payment.",
        "fraud": "Never share your OTP, ATM PIN, UPI PIN, or password. Avoid suspicious links. In India, report cyber financial fraud by calling 1930 or visiting cybercrime.gov.in.",
        "budget": "A budget records your income and expenses. First list your income, then essential expenses, savings, and other spending.",
        "safe": "Please do not enter your real account number, password, OTP, UPI PIN, or other private banking details."
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "🤖 ಫಿನ್‌ಸಾಥಿ ಸಹಾಯಕ",
        "subtitle": "ಹಣ ಮತ್ತು ಬ್ಯಾಂಕಿಂಗ್ ಕುರಿತು ಸರಳ ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳಿ.",
        "question": "ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಬರೆಯಿರಿ",
        "button": "ಉತ್ತರ ಪಡೆಯಿರಿ",
        "home": "🏠 ಮುಖಪುಟಕ್ಕೆ ಹಿಂತಿರುಗಿ",
        "empty": "ದಯವಿಟ್ಟು ಮೊದಲು ಪ್ರಶ್ನೆಯನ್ನು ಬರೆಯಿರಿ.",
        "fallback": "ಉತ್ತರ ಸಿಗಲಿಲ್ಲ. ಬ್ಯಾಂಕಿಂಗ್, ಉಳಿತಾಯ, UPI, ಬಜೆಟ್ ಅಥವಾ ವಂಚನೆ ಸುರಕ್ಷತೆ ಕುರಿತು ಕೇಳಿ.",
        "bank": "ಬ್ಯಾಂಕ್ ಖಾತೆಯಲ್ಲಿ ಹಣವನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಇಡಬಹುದು. ಬ್ಯಾಂಕ್ ಅಥವಾ ATM ಮೂಲಕ ಹಣ ಜಮಾ ಮಾಡಬಹುದು ಮತ್ತು ತೆಗೆಯಬಹುದು.",
        "save": "ನಿಯಮಿತವಾಗಿ ಉಳಿತಾಯ ಮಾಡಿ, ಉಳಿತಾಯದ ಗುರಿ ಇಡಿ ಮತ್ತು ತುರ್ತು ಸಂದರ್ಭಗಳಿಗೆ ಸ್ವಲ್ಪ ಹಣವನ್ನು ಉಳಿಸಿ.",
        "upi": "UPI ಮೂಲಕ ಡಿಜಿಟಲ್ ಆಗಿ ಹಣ ವರ್ಗಾಯಿಸಬಹುದು. ನಿಮ್ಮ UPI PIN ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ. ಪಾವತಿಯನ್ನು ಅನುಮೋದಿಸುವಾಗ ಮಾತ್ರ PIN ನಮೂದಿಸಿ.",
        "fraud": "ನಿಮ್ಮ OTP, ATM PIN, UPI PIN ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್ ಯಾರಿಗೂ ನೀಡಬೇಡಿ. ಅನುಮಾನಾಸ್ಪದ ಲಿಂಕ್‌ಗಳನ್ನು ತೆರೆಯಬೇಡಿ. ಭಾರತದಲ್ಲಿ ಸೈಬರ್ ಹಣಕಾಸು ವಂಚನೆ ವರದಿ ಮಾಡಲು 1930 ಗೆ ಕರೆ ಮಾಡಿ ಅಥವಾ cybercrime.gov.in ಬಳಸಿ.",
        "budget": "ಬಜೆಟ್ ನಿಮ್ಮ ಆದಾಯ ಮತ್ತು ಖರ್ಚುಗಳ ದಾಖಲೆಯಾಗಿದೆ. ಮೊದಲು ಆದಾಯ, ನಂತರ ಅಗತ್ಯ ಖರ್ಚುಗಳು, ಉಳಿತಾಯ ಮತ್ತು ಇತರ ಖರ್ಚುಗಳನ್ನು ಬರೆಯಿರಿ.",
        "safe": "ನಿಮ್ಮ ನಿಜವಾದ ಖಾತೆ ಸಂಖ್ಯೆ, ಪಾಸ್‌ವರ್ಡ್, OTP, UPI PIN ಅಥವಾ ಖಾಸಗಿ ಬ್ಯಾಂಕಿಂಗ್ ಮಾಹಿತಿಯನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಬೇಡಿ."
    },
    "हिन्दी (Hindi)": {
        "title": "🤖 फिनसाथी सहायक",
        "subtitle": "पैसे और बैंकिंग से जुड़े आसान सवाल पूछें।",
        "question": "अपना सवाल लिखें",
        "button": "जवाब पाएं",
        "home": "🏠 होम पर वापस जाएं",
        "empty": "कृपया पहले अपना सवाल लिखें।",
        "fallback": "इस सवाल का जवाब नहीं मिला। बैंकिंग, बचत, UPI, बजट या धोखाधड़ी से सुरक्षा के बारे में पूछें।",
        "bank": "बैंक खाता आपके पैसे को सुरक्षित रखने में मदद करता है। आप बैंक या ATM से पैसे जमा और निकाल सकते हैं।",
        "save": "नियमित रूप से बचत करें, बचत का लक्ष्य बनाएं और आपातकाल के लिए कुछ पैसे अलग रखें।",
        "upi": "UPI से डिजिटल तरीके से पैसे भेज सकते हैं। अपना UPI PIN किसी को न बताएं। PIN केवल भुगतान को मंजूरी देते समय डालें।",
        "fraud": "अपना OTP, ATM PIN, UPI PIN या पासवर्ड किसी को न बताएं। संदिग्ध लिंक न खोलें। भारत में साइबर वित्तीय धोखाधड़ी की शिकायत के लिए 1930 पर कॉल करें या cybercrime.gov.in पर जाएं।",
        "budget": "बजट आपकी आय और खर्चों का हिसाब रखता है। पहले आय, फिर जरूरी खर्च, बचत और अन्य खर्च लिखें।",
        "safe": "अपना असली खाता नंबर, पासवर्ड, OTP, UPI PIN या निजी बैंकिंग जानकारी यहां न लिखें।"
    },
    "मराठी (Marathi)": {
        "title": "🤖 फिनसाथी सहाय्यक",
        "subtitle": "पैसे आणि बँकिंगविषयी सोपे प्रश्न विचारा.",
        "question": "तुमचा प्रश्न लिहा",
        "button": "उत्तर मिळवा",
        "home": "🏠 मुख्यपृष्ठावर परत जा",
        "empty": "कृपया आधी तुमचा प्रश्न लिहा.",
        "fallback": "या प्रश्नाचे उत्तर सापडले नाही. बँकिंग, बचत, UPI, बजेट किंवा फसवणुकीपासून सुरक्षिततेबद्दल विचारा.",
        "bank": "बँक खाते तुमचे पैसे सुरक्षित ठेवण्यास मदत करते. तुम्ही बँक किंवा ATM मधून पैसे जमा आणि काढू शकता.",
        "save": "नियमित बचत करा, बचतीचे ध्येय ठरवा आणि आपत्कालीन परिस्थितीसाठी काही पैसे बाजूला ठेवा.",
        "upi": "UPI द्वारे डिजिटल पद्धतीने पैसे पाठवता येतात. तुमचा UPI PIN कोणालाही सांगू नका. पेमेंट मंजूर करताना PIN टाका.",
        "fraud": "तुमचा OTP, ATM PIN, UPI PIN किंवा पासवर्ड कोणालाही सांगू नका. संशयास्पद लिंक उघडू नका. भारतात सायबर आर्थिक फसवणुकीची तक्रार करण्यासाठी 1930 वर कॉल करा किंवा cybercrime.gov.in ला भेट द्या.",
        "budget": "बजेटमध्ये तुमचे उत्पन्न आणि खर्च नोंदवले जातात. आधी उत्पन्न, नंतर आवश्यक खर्च, बचत आणि इतर खर्च लिहा.",
        "safe": "तुमचा खरा खाते क्रमांक, पासवर्ड, OTP, UPI PIN किंवा खाजगी बँकिंग माहिती येथे लिहू नका."
    }
}

t = TEXT.get(language, TEXT["English"])

st.title(t["title"])
st.write(t["subtitle"])
st.info(t["safe"])

question = st.text_input(t["question"])

if st.button(t["button"], use_container_width=True):
    q = question.lower().strip()

    if not q:
        st.warning(t["empty"])
    elif any(word in q for word in [
        "fraud", "scam", "otp", "pin", "cheat", "ವಂಚನೆ", "ಮೋಸ",
        "धोखाधड़ी", "फ्रॉड", "फसवणूक", "फसवणुकी"
    ]):
        st.warning(t["fraud"])
    elif any(word in q for word in [
        "upi", "payment", "pay", "ಯುಪಿಐ", "ಪಾವತಿ",
        "यूपीआई", "भुगतान", "पेमेंट", "पेमेंट", "पैसे भेज",
        "पैसे पाठव", "देयक"
    ]):
        st.info(t["upi"])
    elif any(word in q for word in [
        "save", "saving", "ಉಳಿತಾಯ", "बचत", "बचत", "बचत कशी"
    ]):
        st.success(t["save"])
    elif any(word in q for word in [
        "budget", "expense", "spend", "बजट", "खर्च",
        "बಜೆಟ್", "ಖರ್ಚು", "अंदाजपत्रक"
    ]):
        st.info(t["budget"])
    elif any(word in q for word in [
        "bank", "account", "atm", "ಬ್ಯಾಂಕ್", "ಖಾತೆ",
        "बैंक", "खाता", "बँक", "खाते"
    ]):
        st.info(t["bank"])
    else:
        st.info(t["fallback"])

if st.button(t["home"], use_container_width=True):
    st.switch_page("app.py")
