
import streamlit as st

st.set_page_config(page_title="FinSaathi - UPI", page_icon="📱")

language = st.session_state.get("language_code", "English")

TEXT = {
    "English": {
        "title": "📱 UPI & Digital Payments",
        "intro": "Learn how to make digital payments safely.",
        "what": "What is UPI?",
        "what_info": "UPI allows you to transfer money between bank accounts using a supported payment app.",
        "send": "How to Send Money",
        "step1": "Open your trusted UPI payment app.",
        "step2": "Choose a recipient or scan their QR code.",
        "step3": "Check the recipient's name and amount carefully.",
        "step4": "Enter your UPI PIN only to authorise a payment you are making.",
        "safety": "Important Safety Rules",
        "tip1": "You do not need to enter your UPI PIN to receive money.",
        "tip2": "Never share your UPI PIN or OTP with anyone.",
        "tip3": "Do not approve unexpected collect requests.",
        "quiz": "Quick Safety Quiz",
        "question": "Someone says you must enter your UPI PIN to receive a payment. What should you do?",
        "a": "Enter the PIN immediately",
        "b": "Do not enter it; verify the request",
        "c": "Share your PIN with the caller",
        "check": "Check Answer",
        "correct": "Correct! A UPI PIN is not needed to receive money.",
        "wrong": "Not quite. Never enter your UPI PIN just to receive money."
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "📱 ಯುಪಿಐ ಮತ್ತು ಡಿಜಿಟಲ್ ಪಾವತಿಗಳು",
        "intro": "ಡಿಜಿಟಲ್ ಪಾವತಿಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಮಾಡುವುದನ್ನು ಕಲಿಯಿರಿ.",
        "what": "ಯುಪಿಐ ಎಂದರೇನು?",
        "what_info": "ಯುಪಿಐ ಮೂಲಕ ಬೆಂಬಲಿತ ಪಾವತಿ ಆ್ಯಪ್ ಬಳಸಿ ಒಂದು ಬ್ಯಾಂಕ್ ಖಾತೆಯಿಂದ ಮತ್ತೊಂದು ಖಾತೆಗೆ ಹಣ ಕಳುಹಿಸಬಹುದು.",
        "send": "ಹಣ ಕಳುಹಿಸುವ ವಿಧಾನ",
        "step1": "ನಂಬಿಕಸ್ಥ ಯುಪಿಐ ಪಾವತಿ ಆ್ಯಪ್ ತೆರೆಯಿರಿ.",
        "step2": "ಸ್ವೀಕರಿಸುವವರನ್ನು ಆಯ್ಕೆಮಾಡಿ ಅಥವಾ ಅವರ ಕ್ಯೂಆರ್ ಕೋಡ್ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ.",
        "step3": "ಸ್ವೀಕರಿಸುವವರ ಹೆಸರು ಮತ್ತು ಮೊತ್ತವನ್ನು ಎಚ್ಚರಿಕೆಯಿಂದ ಪರಿಶೀಲಿಸಿ.",
        "step4": "ನೀವು ಮಾಡುತ್ತಿರುವ ಪಾವತಿಯನ್ನು ದೃಢೀಕರಿಸಲು ಮಾತ್ರ ಯುಪಿಐ ಪಿನ್ ನಮೂದಿಸಿ.",
        "safety": "ಪ್ರಮುಖ ಸುರಕ್ಷತಾ ನಿಯಮಗಳು",
        "tip1": "ಹಣವನ್ನು ಸ್ವೀಕರಿಸಲು ಯುಪಿಐ ಪಿನ್ ನಮೂದಿಸುವ ಅಗತ್ಯವಿಲ್ಲ.",
        "tip2": "ನಿಮ್ಮ ಯುಪಿಐ ಪಿನ್ ಅಥವಾ ಒಟಿಪಿಯನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ.",
        "tip3": "ನಿರೀಕ್ಷಿಸದ ಹಣದ ಬೇಡಿಕೆಗಳನ್ನು ಪರಿಶೀಲಿಸದೆ ಅನುಮೋದಿಸಬೇಡಿ.",
        "quiz": "ಸಣ್ಣ ಸುರಕ್ಷತಾ ರಸಪ್ರಶ್ನೆ",
        "question": "ಹಣ ಪಡೆಯಲು ಯುಪಿಐ ಪಿನ್ ನಮೂದಿಸಬೇಕು ಎಂದು ಯಾರಾದರೂ ಹೇಳಿದರೆ ನೀವು ಏನು ಮಾಡಬೇಕು?",
        "a": "ತಕ್ಷಣ ಪಿನ್ ನಮೂದಿಸಬೇಕು",
        "b": "ಪಿನ್ ನಮೂದಿಸದೆ ವಿನಂತಿಯನ್ನು ಪರಿಶೀಲಿಸಬೇಕು",
        "c": "ಕರೆ ಮಾಡಿದವರಿಗೆ ಪಿನ್ ಹೇಳಬೇಕು",
        "check": "ಉತ್ತರ ಪರಿಶೀಲಿಸಿ",
        "correct": "ಸರಿಯಾಗಿದೆ! ಹಣ ಸ್ವೀಕರಿಸಲು ಯುಪಿಐ ಪಿನ್ ಅಗತ್ಯವಿಲ್ಲ.",
        "wrong": "ತಪ್ಪಾಗಿದೆ. ಹಣ ಸ್ವೀಕರಿಸಲು ಮಾತ್ರ ಯುಪಿಐ ಪಿನ್ ನಮೂದಿಸಬೇಡಿ."
    },
    "हिन्दी (Hindi)": {
        "title": "📱 यूपीआई और डिजिटल भुगतान",
        "intro": "डिजिटल भुगतान सुरक्षित रूप से करना सीखें।",
        "what": "यूपीआई क्या है?",
        "what_info": "यूपीआई के माध्यम से समर्थित भुगतान ऐप का उपयोग करके एक बैंक खाते से दूसरे खाते में पैसे भेज सकते हैं।",
        "send": "पैसे कैसे भेजें",
        "step1": "अपना भरोसेमंद यूपीआई ऐप खोलें।",
        "step2": "प्राप्तकर्ता चुनें या उसका क्यूआर कोड स्कैन करें।",
        "step3": "प्राप्तकर्ता का नाम और राशि ध्यान से जाँचें।",
        "step4": "केवल अपने द्वारा किए जा रहे भुगतान को अधिकृत करने के लिए यूपीआई पिन डालें।",
        "safety": "महत्वपूर्ण सुरक्षा नियम",
        "tip1": "पैसे प्राप्त करने के लिए यूपीआई पिन डालने की आवश्यकता नहीं होती।",
        "tip2": "अपना यूपीआई पिन या ओटीपी किसी से साझा न करें।",
        "tip3": "अनजान भुगतान अनुरोधों को जाँचे बिना स्वीकार न करें।",
        "quiz": "छोटी सुरक्षा प्रश्नोत्तरी",
        "question": "कोई कहता है कि पैसे प्राप्त करने के लिए यूपीआई पिन डालना होगा। आप क्या करेंगे?",
        "a": "तुरंत पिन डालेंगे",
        "b": "पिन नहीं डालेंगे और अनुरोध की जाँच करेंगे",
        "c": "कॉल करने वाले को पिन बताएँगे",
        "check": "उत्तर जाँचें",
        "correct": "सही! पैसे प्राप्त करने के लिए यूपीआई पिन की आवश्यकता नहीं है।",
        "wrong": "ध्यान दें: केवल पैसे प्राप्त करने के लिए यूपीआई पिन कभी न डालें।"
    },
    "मराठी (Marathi)": {
        "title": "📱 यूपीआय आणि डिजिटल पेमेंट",
        "intro": "डिजिटल पेमेंट सुरक्षितपणे कसे करावे ते शिका.",
        "what": "यूपीआय म्हणजे काय?",
        "what_info": "यूपीआयद्वारे समर्थित पेमेंट अॅप वापरून एका बँक खात्यातून दुसऱ्या खात्यात पैसे पाठवता येतात.",
        "send": "पैसे कसे पाठवायचे",
        "step1": "तुमचे विश्वासार्ह यूपीआय अॅप उघडा.",
        "step2": "पैसे घेणारी व्यक्ती निवडा किंवा तिचा क्यूआर कोड स्कॅन करा.",
        "step3": "प्राप्तकर्त्याचे नाव आणि रक्कम काळजीपूर्वक तपासा.",
        "step4": "तुम्ही करत असलेल्या पेमेंटला मान्यता देण्यासाठीच यूपीआय पिन टाका.",
        "safety": "महत्त्वाचे सुरक्षितता नियम",
        "tip1": "पैसे मिळवण्यासाठी यूपीआय पिन टाकण्याची गरज नसते.",
        "tip2": "तुमचा यूपीआय पिन किंवा ओटीपी कोणालाही सांगू नका.",
        "tip3": "अनोळखी पेमेंट विनंत्या तपासल्याशिवाय स्वीकारू नका.",
        "quiz": "छोटी सुरक्षितता प्रश्नमंजुषा",
        "question": "पैसे मिळवण्यासाठी यूपीआय पिन टाकावा लागेल असे कोणी सांगितले तर तुम्ही काय कराल?",
        "a": "लगेच पिन टाकाल",
        "b": "पिन न टाकता विनंती तपासाल",
        "c": "फोन करणाऱ्याला पिन सांगाल",
        "check": "उत्तर तपासा",
        "correct": "बरोबर! पैसे मिळवण्यासाठी यूपीआय पिनची गरज नसते.",
        "wrong": "लक्षात ठेवा: फक्त पैसे मिळवण्यासाठी यूपीआय पिन टाकू नका."
    }
}

T = TEXT.get(language, TEXT["English"])

st.title(T["title"])
st.write(T["intro"])

st.divider()

st.subheader(T["what"])
st.write(T["what_info"])

st.subheader(T["send"])
for key in ["step1", "step2", "step3", "step4"]:
    st.write("• " + T[key])

st.divider()

st.subheader(T["safety"])
st.warning(T["tip1"])
st.warning(T["tip2"])
st.info(T["tip3"])

st.divider()

st.subheader(T["quiz"])
st.write(T["question"])

answer = st.radio(
    " ",
    [T["a"], T["b"], T["c"]],
    key="upi_safety_quiz"
)

if st.button(T["check"]):
    if answer == T["b"]:
        st.success(T["correct"])
    else:
        st.error(T["wrong"])

if st.button("🏠 Home / ಮುಖಪುಟ / होम / मुख्यपृष्ठ"):
    st.switch_page("app.py")
