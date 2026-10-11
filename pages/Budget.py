
import streamlit as st

st.set_page_config(page_title="FinSaathi - Budget", page_icon="📊")

language = st.session_state.get("language_code", "English")

TEXT = {
    "English": {
        "title": "📊 Monthly Budget Planner",
        "intro": "Plan your monthly income and expenses.",
        "income": "Monthly income (₹)",
        "food": "Food and groceries (₹)",
        "education": "Education (₹)",
        "transport": "Transport (₹)",
        "bills": "Bills and other expenses (₹)",
        "savings": "Savings planned (₹)",
        "total": "Total expenses and planned savings",
        "remaining": "Money left",
        "over": "Your expenses and savings exceed your income. Review your budget.",
        "balanced": "Your budget is balanced. Keep tracking your spending.",
        "left": "You have money left. Consider saving some of it.",
        "tips": "Budget Tips",
        "tip1": "Spend on needs before wants.",
        "tip2": "Record your expenses regularly.",
        "tip3": "Save an amount you can comfortably afford."
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "📊 ಮಾಸಿಕ ಬಜೆಟ್ ಯೋಜನೆ",
        "intro": "ನಿಮ್ಮ ಮಾಸಿಕ ಆದಾಯ ಮತ್ತು ಖರ್ಚುಗಳನ್ನು ಯೋಜಿಸಿ.",
        "income": "ಮಾಸಿಕ ಆದಾಯ (₹)",
        "food": "ಆಹಾರ ಮತ್ತು ದಿನಸಿ (₹)",
        "education": "ಶಿಕ್ಷಣ (₹)",
        "transport": "ಸಾರಿಗೆ (₹)",
        "bills": "ಬಿಲ್‌ಗಳು ಮತ್ತು ಇತರ ಖರ್ಚುಗಳು (₹)",
        "savings": "ಯೋಜಿತ ಉಳಿತಾಯ (₹)",
        "total": "ಒಟ್ಟು ಖರ್ಚು ಮತ್ತು ಯೋಜಿತ ಉಳಿತಾಯ",
        "remaining": "ಉಳಿದ ಹಣ",
        "over": "ನಿಮ್ಮ ಖರ್ಚು ಮತ್ತು ಉಳಿತಾಯದ ಮೊತ್ತ ಆದಾಯಕ್ಕಿಂತ ಹೆಚ್ಚಾಗಿದೆ. ಬಜೆಟ್ ಪರಿಶೀಲಿಸಿ.",
        "balanced": "ನಿಮ್ಮ ಬಜೆಟ್ ಸಮತೋಲನದಲ್ಲಿದೆ. ಖರ್ಚುಗಳನ್ನು ಗಮನಿಸುತ್ತಿರಿ.",
        "left": "ನಿಮ್ಮ ಬಳಿ ಹಣ ಉಳಿದಿದೆ. ಅದರಲ್ಲಿ ಸ್ವಲ್ಪ ಉಳಿಸಲು ಪ್ರಯತ್ನಿಸಿ.",
        "tips": "ಬಜೆಟ್ ಸಲಹೆಗಳು",
        "tip1": "ಬಯಕೆಗಳಿಗಿಂತ ಅಗತ್ಯಗಳಿಗೆ ಮೊದಲು ಖರ್ಚು ಮಾಡಿ.",
        "tip2": "ನಿಮ್ಮ ಖರ್ಚುಗಳನ್ನು ನಿಯಮಿತವಾಗಿ ದಾಖಲಿಸಿ.",
        "tip3": "ನಿಮಗೆ ಸಾಧ್ಯವಾದಷ್ಟು ಹಣವನ್ನು ಉಳಿಸಿ."
    },
    "हिन्दी (Hindi)": {
        "title": "📊 मासिक बजट योजना",
        "intro": "अपनी मासिक आय और खर्चों की योजना बनाएँ।",
        "income": "मासिक आय (₹)",
        "food": "भोजन और किराना (₹)",
        "education": "शिक्षा (₹)",
        "transport": "यातायात (₹)",
        "bills": "बिल और अन्य खर्च (₹)",
        "savings": "नियोजित बचत (₹)",
        "total": "कुल खर्च और नियोजित बचत",
        "remaining": "बची हुई राशि",
        "over": "आपके खर्च और बचत आपकी आय से अधिक हैं। बजट की समीक्षा करें।",
        "balanced": "आपका बजट संतुलित है। खर्चों पर नज़र रखें।",
        "left": "आपके पास पैसे बचे हैं। उनमें से कुछ बचाने पर विचार करें।",
        "tips": "बजट सुझाव",
        "tip1": "इच्छाओं से पहले ज़रूरतों पर खर्च करें।",
        "tip2": "अपने खर्च नियमित रूप से लिखें।",
        "tip3": "अपनी क्षमता के अनुसार बचत करें।"
    },
    "मराठी (Marathi)": {
        "title": "📊 मासिक बजेट नियोजन",
        "intro": "तुमच्या मासिक उत्पन्नाचे आणि खर्चाचे नियोजन करा.",
        "income": "मासिक उत्पन्न (₹)",
        "food": "अन्न आणि किराणा (₹)",
        "education": "शिक्षण (₹)",
        "transport": "प्रवास (₹)",
        "bills": "बिले आणि इतर खर्च (₹)",
        "savings": "नियोजित बचत (₹)",
        "total": "एकूण खर्च आणि नियोजित बचत",
        "remaining": "शिल्लक रक्कम",
        "over": "तुमचा खर्च आणि बचत उत्पन्नापेक्षा जास्त आहे. बजेट तपासा.",
        "balanced": "तुमचे बजेट संतुलित आहे. खर्चावर लक्ष ठेवा.",
        "left": "तुमच्याकडे पैसे शिल्लक आहेत. त्यातील काही बचत करा.",
        "tips": "बजेटविषयक सूचना",
        "tip1": "इच्छांपेक्षा गरजांना आधी प्राधान्य द्या.",
        "tip2": "तुमचे खर्च नियमितपणे लिहून ठेवा.",
        "tip3": "तुमच्या क्षमतेनुसार बचत करा."
    }
}

T = TEXT.get(language, TEXT["English"])

st.title(T["title"])
st.write(T["intro"])

income = st.number_input(T["income"], min_value=0.0, step=500.0)
food = st.number_input(T["food"], min_value=0.0, step=100.0)
education = st.number_input(T["education"], min_value=0.0, step=100.0)
transport = st.number_input(T["transport"], min_value=0.0, step=100.0)
bills = st.number_input(T["bills"], min_value=0.0, step=100.0)
savings = st.number_input(T["savings"], min_value=0.0, step=100.0)

total = food + education + transport + bills + savings
remaining = income - total

st.divider()
st.metric(T["total"], f"₹{total:,.2f}")
st.metric(T["remaining"], f"₹{remaining:,.2f}")

if remaining < 0:
    st.error(T["over"])
elif remaining == 0:
    st.info(T["balanced"])
else:
    st.success(T["left"])

st.divider()
st.subheader(T["tips"])
st.write("• " + T["tip1"])
st.write("• " + T["tip2"])
st.write("• " + T["tip3"])

if st.button("🏠 Home / ಮುಖಪುಟ / होम / मुख्यपृष्ठ"):
    st.switch_page("app.py")
