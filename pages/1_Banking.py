
import streamlit as st

st.set_page_config(page_title="FinSaathi - Banking", page_icon="🏦")

# Read the language selected on the home page
language = st.session_state.get("language_code", "English")

TEXT = {
    "English": {
        "title": "🏦 Basic Banking",
        "intro": "Learn the basics of banking.",
        "account": "What is a bank account?",
        "account_info": "A bank account helps you deposit, save and withdraw money safely.",
        "savings": "Savings Account",
        "savings_info": "A savings account lets you keep money in a bank and may earn interest.",
        "atm": "ATM",
        "atm_info": "An ATM allows you to withdraw cash and perform certain banking services.",
        "passbook": "Passbook",
        "passbook_info": "A passbook records deposits, withdrawals and your account balance.",
        "safety": "Banking Safety Tips",
        "tip1": "Never share your ATM PIN, OTP or password.",
        "tip2": "Use official bank websites and apps.",
        "tip3": "Report unknown transactions to your bank immediately."
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "🏦 ಮೂಲ ಬ್ಯಾಂಕಿಂಗ್",
        "intro": "ಬ್ಯಾಂಕಿಂಗ್‌ನ ಮೂಲಭೂತ ವಿಷಯಗಳನ್ನು ತಿಳಿಯಿರಿ.",
        "account": "ಬ್ಯಾಂಕ್ ಖಾತೆ ಎಂದರೇನು?",
        "account_info": "ಬ್ಯಾಂಕ್ ಖಾತೆಯ ಮೂಲಕ ನೀವು ಹಣವನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಜಮಾ ಮಾಡಬಹುದು, ಉಳಿಸಬಹುದು ಮತ್ತು ಹಿಂಪಡೆಯಬಹುದು.",
        "savings": "ಉಳಿತಾಯ ಖಾತೆ",
        "savings_info": "ಉಳಿತಾಯ ಖಾತೆಯಲ್ಲಿ ಹಣವನ್ನು ಇಡಬಹುದು ಮತ್ತು ಅದಕ್ಕೆ ಬಡ್ಡಿ ದೊರೆಯಬಹುದು.",
        "atm": "ಎಟಿಎಂ",
        "atm_info": "ಎಟಿಎಂ ಮೂಲಕ ಹಣವನ್ನು ಹಿಂಪಡೆಯಬಹುದು ಮತ್ತು ಕೆಲವು ಬ್ಯಾಂಕಿಂಗ್ ಸೇವೆಗಳನ್ನು ಬಳಸಬಹುದು.",
        "passbook": "ಪಾಸ್‌ಬುಕ್",
        "passbook_info": "ಪಾಸ್‌ಬುಕ್‌ನಲ್ಲಿ ಹಣದ ಜಮಾ, ಹಿಂಪಡೆಯುವಿಕೆ ಮತ್ತು ಖಾತೆಯ ಬಾಕಿ ವಿವರಗಳು ದಾಖಲಾಗುತ್ತವೆ.",
        "safety": "ಬ್ಯಾಂಕಿಂಗ್ ಸುರಕ್ಷತಾ ಸಲಹೆಗಳು",
        "tip1": "ನಿಮ್ಮ ಎಟಿಎಂ ಪಿನ್, ಒಟಿಪಿ ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್ ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ.",
        "tip2": "ಬ್ಯಾಂಕಿನ ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಮತ್ತು ಆ್ಯಪ್‌ಗಳನ್ನು ಮಾತ್ರ ಬಳಸಿ.",
        "tip3": "ಅಪರಿಚಿತ ವಹಿವಾಟು ಕಂಡುಬಂದರೆ ತಕ್ಷಣ ಬ್ಯಾಂಕಿಗೆ ತಿಳಿಸಿ."
    },
    "हिन्दी (Hindi)": {
        "title": "🏦 बुनियादी बैंकिंग",
        "intro": "बैंकिंग की बुनियादी बातें सीखें।",
        "account": "बैंक खाता क्या है?",
        "account_info": "बैंक खाते से आप सुरक्षित रूप से पैसे जमा कर सकते हैं, बचा सकते हैं और निकाल सकते हैं।",
        "savings": "बचत खाता",
        "savings_info": "बचत खाते में पैसे रखे जा सकते हैं और उस पर ब्याज मिल सकता है।",
        "atm": "एटीएम",
        "atm_info": "एटीएम से नकद पैसे निकाले जा सकते हैं और कुछ बैंकिंग सेवाएँ ली जा सकती हैं।",
        "passbook": "पासबुक",
        "passbook_info": "पासबुक में जमा, निकासी और खाते की शेष राशि दर्ज होती है।",
        "safety": "बैंकिंग सुरक्षा सुझाव",
        "tip1": "अपना एटीएम पिन, ओटीपी या पासवर्ड किसी से साझा न करें।",
        "tip2": "केवल बैंक की आधिकारिक वेबसाइट और ऐप का उपयोग करें।",
        "tip3": "अज्ञात लेन-देन दिखने पर तुरंत बैंक को सूचित करें।"
    },
    "मराठी (Marathi)": {
        "title": "🏦 मूलभूत बँकिंग",
        "intro": "बँकिंगच्या मूलभूत गोष्टी शिका.",
        "account": "बँक खाते म्हणजे काय?",
        "account_info": "बँक खात्याद्वारे तुम्ही पैसे सुरक्षितपणे जमा करू शकता, बचत करू शकता आणि काढू शकता.",
        "savings": "बचत खाते",
        "savings_info": "बचत खात्यात पैसे ठेवता येतात आणि त्यावर व्याज मिळू शकते.",
        "atm": "एटीएम",
        "atm_info": "एटीएममधून रोख पैसे काढता येतात आणि काही बँकिंग सेवा वापरता येतात.",
        "passbook": "पासबुक",
        "passbook_info": "पासबुकमध्ये जमा, पैसे काढणे आणि खात्यातील शिल्लक नोंदवली जाते.",
        "safety": "बँकिंग सुरक्षिततेच्या सूचना",
        "tip1": "तुमचा एटीएम पिन, ओटीपी किंवा पासवर्ड कोणालाही सांगू नका.",
        "tip2": "फक्त बँकेची अधिकृत वेबसाइट आणि अॅप वापरा.",
        "tip3": "अनोळखी व्यवहार दिसल्यास त्वरित बँकेला कळवा."
    }
}

T = TEXT.get(language, TEXT["English"])

st.title(T["title"])
st.write(T["intro"])

st.divider()

st.subheader(T["account"])
st.write(T["account_info"])

st.subheader(T["savings"])
st.write(T["savings_info"])

st.subheader(T["atm"])
st.write(T["atm_info"])

st.subheader(T["passbook"])
st.write(T["passbook_info"])

st.divider()

st.subheader(T["safety"])
st.warning(T["tip1"])
st.info(T["tip2"])
st.info(T["tip3"])

if st.button("🏠 Home / ಮುಖಪುಟ / होम / मुख्यपृष्ठ"):
    st.switch_page("app.py")
