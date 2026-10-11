
import streamlit as st
import re

st.set_page_config(page_title="FinSaathi - Fraud Safety", page_icon="🛡️")

language = st.session_state.get("language_code", "English")

TEXT = {
    "English": {
        "title": "🛡️ Fraud Safety Centre",
        "intro": "Learn to recognise and avoid common financial scams.",
        "signs": "Warning Signs of Fraud",
        "tips": [
            "Someone asks for your OTP, UPI PIN or password.",
            "A message threatens to block your bank account immediately.",
            "An unknown link promises a prize or unexpected payment.",
            "A caller pressures you to act urgently."
        ],
        "checker": "🔎 Suspicious Message Checker",
        "prompt": "Paste a suspicious SMS or message here",
        "button": "Check Message",
        "empty": "Please enter a message first.",
        "warning": "⚠️ This message contains warning signs. Verify it through official channels.",
        "safe": "No common warning patterns were detected. This does not guarantee that the message is safe.",
        "reasons": "Possible warning signs detected:",
        "helpline": "If you suspect financial cyber fraud in India, call 1930 promptly and report it at the official cybercrime portal.",
        "rules": "Important Safety Rules",
        "rule1": "Never share your OTP, PIN or password.",
        "rule2": "Never install an unknown app at a caller's request.",
        "rule3": "Contact your bank using its official number."
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "🛡️ ವಂಚನೆ ಸುರಕ್ಷತಾ ಕೇಂದ್ರ",
        "intro": "ಸಾಮಾನ್ಯ ಆರ್ಥಿಕ ವಂಚನೆಗಳನ್ನು ಗುರುತಿಸಿ ತಪ್ಪಿಸಿಕೊಳ್ಳಲು ಕಲಿಯಿರಿ.",
        "signs": "ವಂಚನೆಯ ಎಚ್ಚರಿಕೆ ಸೂಚನೆಗಳು",
        "tips": [
            "ಯಾರಾದರೂ ನಿಮ್ಮ ಒಟಿಪಿ, ಯುಪಿಐ ಪಿನ್ ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್ ಕೇಳುತ್ತಾರೆ.",
            "ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಯನ್ನು ತಕ್ಷಣ ಮುಚ್ಚುವುದಾಗಿ ಸಂದೇಶ ಬೆದರಿಸುತ್ತದೆ.",
            "ಅಪರಿಚಿತ ಲಿಂಕ್ ಬಹುಮಾನ ಅಥವಾ ಅನಿರೀಕ್ಷಿತ ಹಣದ ಆಮಿಷ ನೀಡುತ್ತದೆ.",
            "ಕರೆ ಮಾಡುವವರು ತಕ್ಷಣ ಕ್ರಮ ಕೈಗೊಳ್ಳುವಂತೆ ಒತ್ತಡ ಹೇರುತ್ತಾರೆ."
        ],
        "checker": "🔎 ಅನುಮಾನಾಸ್ಪದ ಸಂದೇಶ ಪರಿಶೀಲನೆ",
        "prompt": "ಅನುಮಾನಾಸ್ಪದ ಸಂದೇಶವನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಿ",
        "button": "ಸಂದೇಶ ಪರಿಶೀಲಿಸಿ",
        "empty": "ದಯವಿಟ್ಟು ಮೊದಲು ಸಂದೇಶವನ್ನು ನಮೂದಿಸಿ.",
        "warning": "⚠️ ಈ ಸಂದೇಶದಲ್ಲಿ ಎಚ್ಚರಿಕೆಯ ಸೂಚನೆಗಳಿವೆ. ಅಧಿಕೃತ ಮಾರ್ಗದ ಮೂಲಕ ಪರಿಶೀಲಿಸಿ.",
        "safe": "ಸಾಮಾನ್ಯ ಎಚ್ಚರಿಕೆಯ ಸೂಚನೆಗಳು ಕಂಡುಬಂದಿಲ್ಲ. ಇದರಿಂದ ಸಂದೇಶ ಸುರಕ್ಷಿತವೆಂದು ಖಚಿತವಾಗುವುದಿಲ್ಲ.",
        "reasons": "ಕಂಡುಬಂದಿರುವ ಎಚ್ಚರಿಕೆಯ ಸೂಚನೆಗಳು:",
        "helpline": "ಭಾರತದಲ್ಲಿ ಆರ್ಥಿಕ ಸೈಬರ್ ವಂಚನೆ ಅನುಮಾನವಿದ್ದರೆ 1930ಕ್ಕೆ ತಕ್ಷಣ ಕರೆ ಮಾಡಿ ಮತ್ತು ಅಧಿಕೃತ ಸೈಬರ್ ಅಪರಾಧ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ವರದಿ ಮಾಡಿ.",
        "rules": "ಪ್ರಮುಖ ಸುರಕ್ಷತಾ ನಿಯಮಗಳು",
        "rule1": "ನಿಮ್ಮ ಒಟಿಪಿ, ಪಿನ್ ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ.",
        "rule2": "ಕರೆ ಮಾಡಿದವರು ಹೇಳಿದ ಕಾರಣಕ್ಕೆ ಅಪರಿಚಿತ ಆ್ಯಪ್ ಸ್ಥಾಪಿಸಬೇಡಿ.",
        "rule3": "ಬ್ಯಾಂಕಿನ ಅಧಿಕೃತ ಸಂಖ್ಯೆಯ ಮೂಲಕ ಸಂಪರ್ಕಿಸಿ."
    },
    "हिन्दी (Hindi)": {
        "title": "🛡️ धोखाधड़ी सुरक्षा केंद्र",
        "intro": "आम वित्तीय धोखाधड़ी को पहचानना और उससे बचना सीखें।",
        "signs": "धोखाधड़ी के चेतावनी संकेत",
        "tips": [
            "कोई आपका ओटीपी, यूपीआई पिन या पासवर्ड माँगता है।",
            "संदेश में तुरंत बैंक खाता बंद करने की धमकी दी जाती है।",
            "कोई अनजान लिंक इनाम या अचानक पैसे मिलने का लालच देता है।",
            "कॉल करने वाला तुरंत कार्रवाई करने का दबाव डालता है।"
        ],
        "checker": "🔎 संदिग्ध संदेश जाँचें",
        "prompt": "संदिग्ध संदेश यहाँ लिखें",
        "button": "संदेश जाँचें",
        "empty": "कृपया पहले संदेश लिखें।",
        "warning": "⚠️ इस संदेश में चेतावनी के संकेत हैं। आधिकारिक माध्यम से जाँच करें।",
        "safe": "कोई सामान्य चेतावनी संकेत नहीं मिला। इससे संदेश के सुरक्षित होने की गारंटी नहीं मिलती।",
        "reasons": "संभावित चेतावनी संकेत:",
        "helpline": "भारत में वित्तीय साइबर धोखाधड़ी का संदेह होने पर तुरंत 1930 पर कॉल करें और आधिकारिक साइबर अपराध पोर्टल पर शिकायत करें।",
        "rules": "महत्वपूर्ण सुरक्षा नियम",
        "rule1": "अपना ओटीपी, पिन या पासवर्ड किसी से साझा न करें।",
        "rule2": "कॉल करने वाले के कहने पर कोई अनजान ऐप इंस्टॉल न करें।",
        "rule3": "अपने बैंक के आधिकारिक नंबर पर संपर्क करें।"
    },
    "मराठी (Marathi)": {
        "title": "🛡️ फसवणूक सुरक्षा केंद्र",
        "intro": "सामान्य आर्थिक फसवणूक ओळखायला आणि टाळायला शिका.",
        "signs": "फसवणुकीची धोक्याची चिन्हे",
        "tips": [
            "कोणी तुमचा ओटीपी, यूपीआय पिन किंवा पासवर्ड मागतो.",
            "संदेशात तुमचे बँक खाते त्वरित बंद करण्याची धमकी दिली जाते.",
            "अनोळखी लिंक बक्षीस किंवा अनपेक्षित पैसे मिळण्याचे आमिष दाखवते.",
            "फोन करणारी व्यक्ती त्वरित कृती करण्यासाठी दबाव आणते."
        ],
        "checker": "🔎 संशयास्पद संदेश तपासा",
        "prompt": "संशयास्पद संदेश येथे लिहा",
        "button": "संदेश तपासा",
        "empty": "कृपया आधी संदेश लिहा.",
        "warning": "⚠️ या संदेशात धोक्याची चिन्हे आहेत. अधिकृत माध्यमातून तपासा.",
        "safe": "सामान्य धोक्याची चिन्हे आढळली नाहीत. याचा अर्थ संदेश सुरक्षित आहे याची खात्री नाही.",
        "reasons": "संभाव्य धोक्याची चिन्हे:",
        "helpline": "भारतात आर्थिक सायबर फसवणुकीचा संशय असल्यास त्वरित 1930 वर कॉल करा आणि अधिकृत सायबर गुन्हे पोर्टलवर तक्रार करा.",
        "rules": "महत्त्वाचे सुरक्षितता नियम",
        "rule1": "तुमचा ओटीपी, पिन किंवा पासवर्ड कोणालाही सांगू नका.",
        "rule2": "फोन करणाऱ्याच्या सांगण्यावरून अनोळखी अॅप स्थापित करू नका.",
        "rule3": "बँकेच्या अधिकृत क्रमांकावर संपर्क साधा."
    }
}

T = TEXT.get(language, TEXT["English"])

st.title(T["title"])
st.write(T["intro"])

st.divider()

st.subheader(T["signs"])
for tip in T["tips"]:
    st.warning(tip)

st.divider()

st.subheader(T["checker"])
message = st.text_area(T["prompt"])

if st.button(T["button"], use_container_width=True):
    if not message.strip():
        st.info(T["empty"])
    else:
        # Basic rule-based screening, not a trained AI model
        patterns = {
            "OTP/PIN/password request": r"\b(otp|pin|password|passcode)\b",
            "Urgent threat": r"\b(block(ed)?|suspend(ed)?|urgent|immediately|expire[ds]?)\b",
            "Prize or reward bait": r"\b(prize|winner|reward|lottery|claim|ಬ್ಲಾಕ್|ಬಹುಮಾನ|इनाम|बक्षीस)\b",
            "Suspicious link": r"(https?://|www\.)"
        }

        found = [
            reason for reason, pattern in patterns.items()
            if re.search(pattern, message, re.IGNORECASE)
        ]

        if found:
            st.error(T["warning"])
            st.write(T["reasons"])
            for reason in found:
                st.write("• " + reason)
        else:
            st.info(T["safe"])

st.divider()

st.subheader(T["rules"])
st.write("• " + T["rule1"])
st.write("• " + T["rule2"])
st.write("• " + T["rule3"])

st.info(T["helpline"])
st.caption(
    "Official reporting: https://cybercrime.gov.in/"
)

if st.button("🏠 Home / ಮುಖಪುಟ / होम / मुख्यपृष्ठ"):
    st.switch_page("app.py")
