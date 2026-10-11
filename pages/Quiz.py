
import streamlit as st

st.set_page_config(page_title="FinSaathi Quiz", page_icon="📝")

language = st.session_state.get("language_code", "English")

QUIZ = {
    "English": {
        "title": "📝 Financial Literacy Quiz",
        "intro": "Test your knowledge of banking, savings, UPI and fraud safety!",
        "questions": [
            ("Should you share your OTP with someone who calls you?",
             ["Yes", "No"], 1,
             "Never share your OTP with anyone."),
            ("What is the safest way to handle your savings?",
             ["Spend everything", "Save regularly", "Share your PIN"], 1,
             "Regular saving helps you prepare for future needs."),
            ("When should you enter your UPI PIN?",
             ["To receive money", "To claim a prize", "To authorise a payment"], 2,
             "You do not need a UPI PIN to receive money."),
            ("What should you do if you receive a suspicious bank link?",
             ["Click immediately", "Avoid it and verify with the bank", "Forward it"], 1,
             "Avoid suspicious links and verify messages through official bank channels."),
            ("What does a budget help you track?",
             ["Income and expenses", "Only phone calls", "Only passwords"], 0,
             "A budget helps you understand your income and spending.")
        ],
        "submit": "Check My Answers",
        "score": "Your score",
        "outof": "out of",
        "excellent": "Excellent work!",
        "good": "Good effort! Review the answers and try again.",
        "retry": "🔄 Try Again",
        "home": "🏠 Back to Home",
        "select": "Choose an answer",
        "unanswered": "Please answer every question before submitting."
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "📝 ಆರ್ಥಿಕ ಸಾಕ್ಷರತೆ ರಸಪ್ರಶ್ನೆ",
        "intro": "ಬ್ಯಾಂಕಿಂಗ್, ಉಳಿತಾಯ, UPI ಮತ್ತು ವಂಚನೆ ಸುರಕ್ಷತೆ ಕುರಿತು ನಿಮ್ಮ ಜ್ಞಾನವನ್ನು ಪರೀಕ್ಷಿಸಿ!",
        "questions": [
            ("ಫೋನ್ ಮಾಡುವ ವ್ಯಕ್ತಿಯೊಂದಿಗೆ OTP ಹಂಚಿಕೊಳ್ಳಬೇಕೇ?",
             ["ಹೌದು", "ಇಲ್ಲ"], 1,
             "ನಿಮ್ಮ OTP ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ."),
            ("ಉಳಿತಾಯ ಮಾಡಲು ಉತ್ತಮ ವಿಧಾನ ಯಾವುದು?",
             ["ಎಲ್ಲಾ ಹಣ ಖರ್ಚು ಮಾಡುವುದು", "ನಿಯಮಿತವಾಗಿ ಉಳಿತಾಯ ಮಾಡುವುದು", "PIN ಹಂಚಿಕೊಳ್ಳುವುದು"], 1,
             "ನಿಯಮಿತ ಉಳಿತಾಯವು ಭವಿಷ್ಯದ ಅಗತ್ಯಗಳಿಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ."),
            ("UPI PIN ಅನ್ನು ಯಾವಾಗ ನಮೂದಿಸಬೇಕು?",
             ["ಹಣ ಸ್ವೀಕರಿಸಲು", "ಬಹುಮಾನ ಪಡೆಯಲು", "ಪಾವತಿಯನ್ನು ಅನುಮೋದಿಸಲು"], 2,
             "ಹಣ ಸ್ವೀಕರಿಸಲು UPI PIN ಅಗತ್ಯವಿಲ್ಲ."),
            ("ಅನುಮಾನಾಸ್ಪದ ಬ್ಯಾಂಕ್ ಲಿಂಕ್ ಬಂದರೆ ಏನು ಮಾಡಬೇಕು?",
             ["ತಕ್ಷಣ ತೆರೆಯಬೇಕು", "ತೆರೆಯದೆ ಬ್ಯಾಂಕ್ ಮೂಲಕ ಪರಿಶೀಲಿಸಬೇಕು", "ಇತರರಿಗೆ ಕಳುಹಿಸಬೇಕು"], 1,
             "ಅನುಮಾನಾಸ್ಪದ ಲಿಂಕ್‌ಗಳನ್ನು ತೆರೆಯಬೇಡಿ; ಅಧಿಕೃತ ಬ್ಯಾಂಕ್ ಮೂಲಕ ಪರಿಶೀಲಿಸಿ."),
            ("ಬಜೆಟ್ ಯಾವುದನ್ನು ಗಮನಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ?",
             ["ಆದಾಯ ಮತ್ತು ಖರ್ಚು", "ಫೋನ್ ಕರೆಗಳು ಮಾತ್ರ", "ಪಾಸ್‌ವರ್ಡ್‌ಗಳು ಮಾತ್ರ"], 0,
             "ಬಜೆಟ್ ನಿಮ್ಮ ಆದಾಯ ಮತ್ತು ಖರ್ಚನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.")
        ],
        "submit": "ಉತ್ತರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ",
        "score": "ನಿಮ್ಮ ಅಂಕ",
        "outof": "ರಲ್ಲಿ",
        "excellent": "ಅತ್ಯುತ್ತಮ ಪ್ರಯತ್ನ!",
        "good": "ಚೆನ್ನಾಗಿದೆ! ಉತ್ತರಗಳನ್ನು ಓದಿ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
        "retry": "🔄 ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ",
        "home": "🏠 ಮುಖಪುಟಕ್ಕೆ ಹಿಂತಿರುಗಿ",
        "select": "ಉತ್ತರವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "unanswered": "ಸಲ್ಲಿಸುವ ಮೊದಲು ಎಲ್ಲಾ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿ."
    },
    "हिन्दी (Hindi)": {
        "title": "📝 वित्तीय साक्षरता प्रश्नोत्तरी",
        "intro": "बैंकिंग, बचत, UPI और धोखाधड़ी से सुरक्षा का अपना ज्ञान जांचें!",
        "questions": [
            ("क्या फोन करने वाले व्यक्ति को अपना OTP बताना चाहिए?",
             ["हाँ", "नहीं"], 1,
             "अपना OTP किसी के साथ साझा न करें।"),
            ("बचत करने का अच्छा तरीका क्या है?",
             ["सारे पैसे खर्च करना", "नियमित बचत करना", "PIN साझा करना"], 1,
             "नियमित बचत भविष्य की जरूरतों में मदद करती है।"),
            ("UPI PIN कब डालना चाहिए?",
             ["पैसे प्राप्त करने के लिए", "इनाम पाने के लिए", "भुगतान की मंजूरी देने के लिए"], 2,
             "पैसे प्राप्त करने के लिए UPI PIN की जरूरत नहीं होती।"),
            ("संदिग्ध बैंक लिंक मिलने पर क्या करना चाहिए?",
             ["तुरंत खोलना", "न खोलना और बैंक से जांच करना", "आगे भेजना"], 1,
             "संदिग्ध लिंक न खोलें और बैंक के आधिकारिक माध्यम से जांच करें।"),
            ("बजट किसका हिसाब रखने में मदद करता है?",
             ["आय और खर्च", "केवल फोन कॉल", "केवल पासवर्ड"], 0,
             "बजट आपकी आय और खर्च समझने में मदद करता है।")
        ],
        "submit": "मेरे उत्तर जांचें",
        "score": "आपका स्कोर",
        "outof": "में से",
        "excellent": "बहुत अच्छा!",
        "good": "अच्छी कोशिश! उत्तरों को पढ़ें और फिर प्रयास करें।",
        "retry": "🔄 फिर से प्रयास करें",
        "home": "🏠 होम पर वापस जाएं",
        "select": "उत्तर चुनें",
        "unanswered": "जमा करने से पहले सभी सवालों के जवाब दें।"
    },
    "मराठी (Marathi)": {
        "title": "📝 आर्थिक साक्षरता प्रश्नमंजुषा",
        "intro": "बँकिंग, बचत, UPI आणि फसवणुकीपासून सुरक्षिततेचे ज्ञान तपासा!",
        "questions": [
            ("फोन करणाऱ्या व्यक्तीला OTP सांगावा का?",
             ["होय", "नाही"], 1,
             "तुमचा OTP कोणाशीही शेअर करू नका."),
            ("बचत करण्याची चांगली पद्धत कोणती?",
             ["सर्व पैसे खर्च करणे", "नियमित बचत करणे", "PIN शेअर करणे"], 1,
             "नियमित बचत भविष्यातील गरजांसाठी मदत करते."),
            ("UPI PIN कधी टाकावा?",
             ["पैसे मिळवण्यासाठी", "बक्षीस मिळवण्यासाठी", "पेमेंट मंजूर करण्यासाठी"], 2,
             "पैसे मिळवण्यासाठी UPI PIN ची गरज नसते."),
            ("संशयास्पद बँक लिंक मिळाल्यास काय करावे?",
             ["लगेच उघडावी", "उघडू नये आणि बँकेकडून खात्री करावी", "पुढे पाठवावी"], 1,
             "संशयास्पद लिंक उघडू नका. बँकेच्या अधिकृत माध्यमातून खात्री करा."),
            ("बजेट कशाचा हिशोब ठेवण्यास मदत करते?",
             ["उत्पन्न आणि खर्च", "फक्त फोन कॉल", "फक्त पासवर्ड"], 0,
             "बजेटमुळे तुमचे उत्पन्न आणि खर्च समजण्यास मदत होते.")
        ],
        "submit": "माझी उत्तरे तपासा",
        "score": "तुमचे गुण",
        "outof": "पैकी",
        "excellent": "उत्तम काम!",
        "good": "छान प्रयत्न! उत्तरे वाचा आणि पुन्हा प्रयत्न करा.",
        "retry": "🔄 पुन्हा प्रयत्न करा",
        "home": "🏠 मुख्यपृष्ठावर परत जा",
        "select": "उत्तर निवडा",
        "unanswered": "सबमिट करण्यापूर्वी सर्व प्रश्नांची उत्तरे द्या."
    }
}

t = QUIZ.get(language, QUIZ["English"])

st.title(t["title"])
st.write(t["intro"])
st.divider()

answers = []

for i, (question, options, correct, explanation) in enumerate(t["questions"]):
    st.subheader(f"{i + 1}. {question}")
    answer = st.radio(
        t["select"],
        options,
        key=f"quiz_{language}_{i}",
        index=None
    )
    answers.append(answer)

st.divider()

if st.button(t["submit"], use_container_width=True):
    if any(answer is None for answer in answers):
        st.warning(t["unanswered"])
    else:
        score = sum(
            1 for answer, (_, options, correct, _) in
            zip(answers, t["questions"])
            if answer == options[correct]
        )

        st.session_state["quiz_score"] = score
        st.session_state["quiz_submitted"] = True

if st.session_state.get("quiz_submitted", False):
    score = st.session_state.get("quiz_score", 0)
    st.subheader(f'{t["score"]}: {score} {t["outof"]} 5')

    if score >= 4:
        st.success(t["excellent"])
    else:
        st.info(t["good"])

    for i, (question, options, correct, explanation) in enumerate(t["questions"]):
        st.write(f"**{i + 1}. {question}**")
        st.write(f'✅ {options[correct]}')
        st.caption(explanation)

    if st.button(t["retry"], use_container_width=True):
        st.session_state["quiz_submitted"] = False
        st.session_state["quiz_score"] = 0
        for i in range(len(t["questions"])):
            st.session_state.pop(f"quiz_{language}_{i}", None)
        st.rerun()

if st.button(t["home"], use_container_width=True):
    st.switch_page("app.py")
