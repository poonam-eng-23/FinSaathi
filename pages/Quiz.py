
import random
import streamlit as st

st.set_page_config(page_title="FinSaathi Quiz", page_icon="📝")

language = st.session_state.get("language_code", "English")

# Each question: ID, question, options, correct option index, explanation
BANK = {
    "English": [
        ("q1", "Should you share your OTP with a caller?", ["Yes", "No", "Only with strangers", "Only at night"], 1, "Never share an OTP with anyone."),
        ("q2", "What is a bank account mainly used for?", ["Storing money safely", "Repairing phones", "Buying internet data only", "Making passwords"], 0, "A bank account helps you deposit, store and withdraw money."),
        ("q3", "When should you enter your UPI PIN?", ["To receive money", "To claim a prize", "To authorise a payment", "To check a message"], 2, "A UPI PIN is used to authorise a payment, not to receive money."),
        ("q4", "What should you do with a suspicious bank link?", ["Open it quickly", "Forward it", "Enter your PIN", "Avoid it and verify with the bank"], 3, "Avoid suspicious links and verify through official bank channels."),
        ("q5", "What does a budget help you track?", ["Income and expenses", "Only phone calls", "Only passwords", "Only birthdays"], 0, "A budget helps track income and spending."),
        ("q6", "Why should you save money regularly?", ["To spend more immediately", "To prepare for future needs", "To share your PIN", "To avoid keeping records"], 1, "Regular saving helps prepare for planned and unexpected expenses."),
        ("q7", "What should you do if you suspect online financial fraud in India?", ["Ignore it", "Delete all evidence", "Report it promptly through official channels", "Share your OTP"], 2, "You can call 1930 or visit cybercrime.gov.in to report cyber financial fraud."),
        ("q8", "Which is a safer password practice?", ["Use your name only", "Share it with friends", "Use the same simple password everywhere", "Use a strong, unique password"], 3, "Strong, unique passwords help protect your accounts."),
        ("q9", "What is an ATM used for?", ["Withdrawing cash and other banking services", "Creating social media posts", "Charging a phone", "Sending an email"], 0, "ATMs provide cash withdrawal and other banking services."),
        ("q10", "What is an emergency fund for?", ["Daily entertainment only", "Unexpected expenses", "Sharing account details", "Online games"], 1, "An emergency fund helps cover unexpected costs."),
        ("q11", "What should you do before taking a loan?", ["Borrow without checking", "Ignore repayment terms", "Understand interest and repayment conditions", "Share your PIN"], 2, "Understand the interest, fees and repayment schedule before borrowing."),
        ("q12", "Which detail should remain private?", ["A bank's public address", "A published bank phone number", "A public branch location", "Your banking OTP"], 3, "Keep OTPs and other authentication details private.")
    ],

    "ಕನ್ನಡ (Kannada)": [
        ("q1", "ಫೋನ್ ಮಾಡುವ ವ್ಯಕ್ತಿಯೊಂದಿಗೆ OTP ಹಂಚಿಕೊಳ್ಳಬೇಕೇ?", ["ಹೌದು", "ಇಲ್ಲ", "ಅಪರಿಚಿತರೊಂದಿಗೆ ಮಾತ್ರ", "ರಾತ್ರಿ ಮಾತ್ರ"], 1, "ನಿಮ್ಮ OTP ಅನ್ನು ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ."),
        ("q2", "ಬ್ಯಾಂಕ್ ಖಾತೆಯ ಮುಖ್ಯ ಉದ್ದೇಶವೇನು?", ["ಹಣವನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಇಡುವುದು", "ಫೋನ್ ದುರಸ್ತಿ", "ಇಂಟರ್ನೆಟ್ ಖರೀದಿ ಮಾತ್ರ", "ಪಾಸ್‌ವರ್ಡ್ ರಚಿಸುವುದು"], 0, "ಬ್ಯಾಂಕ್ ಖಾತೆಯಲ್ಲಿ ಹಣ ಜಮಾ ಮಾಡಬಹುದು, ಇಡಬಹುದು ಮತ್ತು ತೆಗೆಯಬಹುದು."),
        ("q3", "UPI PIN ಅನ್ನು ಯಾವಾಗ ನಮೂದಿಸಬೇಕು?", ["ಹಣ ಸ್ವೀಕರಿಸಲು", "ಬಹುಮಾನ ಪಡೆಯಲು", "ಪಾವತಿಯನ್ನು ಅನುಮೋದಿಸಲು", "ಸಂದೇಶ ನೋಡಲು"], 2, "UPI PIN ಪಾವತಿಯನ್ನು ಅನುಮೋದಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ; ಹಣ ಸ್ವೀಕರಿಸಲು ಅಲ್ಲ."),
        ("q4", "ಅನುಮಾನಾಸ್ಪದ ಬ್ಯಾಂಕ್ ಲಿಂಕ್ ಬಂದರೆ ಏನು ಮಾಡಬೇಕು?", ["ತಕ್ಷಣ ತೆರೆಯಬೇಕು", "ಮುಂದೆ ಕಳುಹಿಸಬೇಕು", "PIN ನಮೂದಿಸಬೇಕು", "ತೆರೆಯದೆ ಬ್ಯಾಂಕ್ ಮೂಲಕ ಪರಿಶೀಲಿಸಬೇಕು"], 3, "ಅನುಮಾನಾಸ್ಪದ ಲಿಂಕ್ ತೆರೆಯಬೇಡಿ; ಅಧಿಕೃತ ಬ್ಯಾಂಕ್ ಮೂಲಕ ಪರಿಶೀಲಿಸಿ."),
        ("q5", "ಬಜೆಟ್ ಯಾವುದನ್ನು ಗಮನಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ?", ["ಆದಾಯ ಮತ್ತು ಖರ್ಚು", "ಫೋನ್ ಕರೆಗಳು ಮಾತ್ರ", "ಪಾಸ್‌ವರ್ಡ್‌ಗಳು ಮಾತ್ರ", "ಜನ್ಮದಿನಗಳು ಮಾತ್ರ"], 0, "ಬಜೆಟ್ ಆದಾಯ ಮತ್ತು ಖರ್ಚನ್ನು ದಾಖಲಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ."),
        ("q6", "ನಿಯಮಿತವಾಗಿ ಹಣ ಉಳಿಸುವುದು ಏಕೆ ಮುಖ್ಯ?", ["ತಕ್ಷಣ ಹೆಚ್ಚು ಖರ್ಚು ಮಾಡಲು", "ಭವಿಷ್ಯದ ಅಗತ್ಯಗಳಿಗೆ ಸಿದ್ಧರಾಗಲು", "PIN ಹಂಚಿಕೊಳ್ಳಲು", "ದಾಖಲೆ ತಪ್ಪಿಸಲು"], 1, "ನಿಯಮಿತ ಉಳಿತಾಯವು ಭವಿಷ್ಯದ ಮತ್ತು ಅನಿರೀಕ್ಷಿತ ಖರ್ಚುಗಳಿಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ."),
        ("q7", "ಭಾರತದಲ್ಲಿ ಆನ್‌ಲೈನ್ ಹಣಕಾಸು ವಂಚನೆ ಅನುಮಾನವಾದರೆ ಏನು ಮಾಡಬೇಕು?", ["ನಿರ್ಲಕ್ಷಿಸಬೇಕು", "ಎಲ್ಲ ಸಾಕ್ಷ್ಯ ಅಳಿಸಬೇಕು", "ಅಧಿಕೃತ ಮಾರ್ಗದಲ್ಲಿ ತಕ್ಷಣ ವರದಿ ಮಾಡಬೇಕು", "OTP ಹಂಚಿಕೊಳ್ಳಬೇಕು"], 2, "ಸೈಬರ್ ಹಣಕಾಸು ವಂಚನೆಯನ್ನು 1930 ಗೆ ಕರೆ ಮಾಡಿ ಅಥವಾ cybercrime.gov.in ನಲ್ಲಿ ವರದಿ ಮಾಡಬಹುದು."),
        ("q8", "ಯಾವುದು ಸುರಕ್ಷಿತ ಪಾಸ್‌ವರ್ಡ್ ಅಭ್ಯಾಸ?", ["ಹೆಸರು ಮಾತ್ರ ಬಳಸುವುದು", "ಸ್ನೇಹಿತರೊಂದಿಗೆ ಹಂಚಿಕೊಳ್ಳುವುದು", "ಎಲ್ಲೆಡೆ ಒಂದೇ ಸರಳ ಪಾಸ್‌ವರ್ಡ್ ಬಳಸುವುದು", "ಬಲವಾದ ಪ್ರತ್ಯೇಕ ಪಾಸ್‌ವರ್ಡ್ ಬಳಸುವುದು"], 3, "ಬಲವಾದ ಮತ್ತು ಪ್ರತ್ಯೇಕ ಪಾಸ್‌ವರ್ಡ್‌ಗಳು ಖಾತೆಗಳನ್ನು ರಕ್ಷಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ."),
        ("q9", "ATM ಅನ್ನು ಯಾವುದಕ್ಕಾಗಿ ಬಳಸುತ್ತಾರೆ?", ["ಹಣ ತೆಗೆಯಲು ಮತ್ತು ಬ್ಯಾಂಕಿಂಗ್ ಸೇವೆಗಳಿಗೆ", "ಸಾಮಾಜಿಕ ಮಾಧ್ಯಮ ಪೋಸ್ಟ್ ಮಾಡಲು", "ಫೋನ್ ಚಾರ್ಜ್ ಮಾಡಲು", "ಇಮೇಲ್ ಕಳುಹಿಸಲು"], 0, "ATM ಮೂಲಕ ಹಣ ತೆಗೆಯಬಹುದು ಮತ್ತು ಇತರ ಬ್ಯಾಂಕಿಂಗ್ ಸೇವೆಗಳನ್ನು ಬಳಸಬಹುದು."),
        ("q10", "ತುರ್ತು ನಿಧಿ ಯಾವುದಕ್ಕಾಗಿ?", ["ಮನರಂಜನೆಗಾಗಿ ಮಾತ್ರ", "ಅನಿರೀಕ್ಷಿತ ಖರ್ಚುಗಳಿಗೆ", "ಖಾತೆ ವಿವರ ಹಂಚಿಕೊಳ್ಳಲು", "ಆನ್‌ಲೈನ್ ಆಟಗಳಿಗೆ"], 1, "ತುರ್ತು ನಿಧಿ ಅನಿರೀಕ್ಷಿತ ಖರ್ಚುಗಳನ್ನು ನಿಭಾಯಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ."),
        ("q11", "ಸಾಲ ಪಡೆಯುವ ಮೊದಲು ಏನು ಮಾಡಬೇಕು?", ["ಪರಿಶೀಲಿಸದೆ ಸಾಲ ಪಡೆಯಬೇಕು", "ಮರುಪಾವತಿ ನಿಯಮ ನಿರ್ಲಕ್ಷಿಸಬೇಕು", "ಬಡ್ಡಿ ಮತ್ತು ಮರುಪಾವತಿ ಷರತ್ತುಗಳನ್ನು ತಿಳಿಯಬೇಕು", "PIN ಹಂಚಿಕೊಳ್ಳಬೇಕು"], 2, "ಸಾಲದ ಮೊದಲು ಬಡ್ಡಿ, ಶುಲ್ಕ ಮತ್ತು ಮರುಪಾವತಿ ವೇಳಾಪಟ್ಟಿಯನ್ನು ತಿಳಿಯಿರಿ."),
        ("q12", "ಯಾವ ಮಾಹಿತಿಯನ್ನು ಖಾಸಗಿಯಾಗಿ ಇಡಬೇಕು?", ["ಬ್ಯಾಂಕಿನ ಸಾರ್ವಜನಿಕ ವಿಳಾಸ", "ಪ್ರಕಟಿತ ಬ್ಯಾಂಕ್ ಫೋನ್ ಸಂಖ್ಯೆ", "ಶಾಖೆಯ ಸಾರ್ವಜನಿಕ ಸ್ಥಳ", "ನಿಮ್ಮ ಬ್ಯಾಂಕಿಂಗ್ OTP"], 3, "OTP ಮತ್ತು ಇತರ ದೃಢೀಕರಣ ಮಾಹಿತಿಯನ್ನು ಖಾಸಗಿಯಾಗಿ ಇಡಿ.")
    ],

    "हिन्दी (Hindi)": [
        ("q1", "क्या फोन करने वाले व्यक्ति को OTP बताना चाहिए?", ["हाँ", "नहीं", "केवल अजनबियों को", "केवल रात में"], 1, "अपना OTP किसी के साथ साझा न करें।"),
        ("q2", "बैंक खाते का मुख्य उपयोग क्या है?", ["पैसे सुरक्षित रखना", "फोन ठीक करना", "केवल इंटरनेट खरीदना", "पासवर्ड बनाना"], 0, "बैंक खाते में पैसे जमा, सुरक्षित और निकाले जा सकते हैं।"),
        ("q3", "UPI PIN कब डालना चाहिए?", ["पैसे प्राप्त करने के लिए", "इनाम पाने के लिए", "भुगतान की मंजूरी देने के लिए", "संदेश देखने के लिए"], 2, "UPI PIN भुगतान मंजूर करने के लिए है, पैसे प्राप्त करने के लिए नहीं।"),
        ("q4", "संदिग्ध बैंक लिंक मिलने पर क्या करें?", ["तुरंत खोलें", "आगे भेजें", "PIN डालें", "न खोलें और बैंक से जांच करें"], 3, "संदिग्ध लिंक से बचें और बैंक के आधिकारिक माध्यम से जांच करें।"),
        ("q5", "बजट किसका हिसाब रखने में मदद करता है?", ["आय और खर्च", "केवल फोन कॉल", "केवल पासवर्ड", "केवल जन्मदिन"], 0, "बजट आय और खर्च का हिसाब रखने में मदद करता है।"),
        ("q6", "नियमित बचत क्यों जरूरी है?", ["तुरंत ज्यादा खर्च करने के लिए", "भविष्य की जरूरतों के लिए तैयार रहने के लिए", "PIN साझा करने के लिए", "रिकॉर्ड से बचने के लिए"], 1, "नियमित बचत भविष्य और अचानक आने वाले खर्चों में मदद करती है।"),
        ("q7", "भारत में ऑनलाइन वित्तीय धोखाधड़ी का संदेह हो तो क्या करें?", ["अनदेखा करें", "सभी सबूत मिटाएं", "आधिकारिक माध्यम से तुरंत रिपोर्ट करें", "OTP साझा करें"], 2, "साइबर वित्तीय धोखाधड़ी की शिकायत 1930 पर कॉल करके या cybercrime.gov.in पर की जा सकती है।"),
        ("q8", "पासवर्ड रखने का सुरक्षित तरीका कौन सा है?", ["केवल अपना नाम", "दोस्तों से साझा करना", "हर जगह एक ही आसान पासवर्ड", "मजबूत और अलग पासवर्ड"], 3, "मजबूत और अलग पासवर्ड खातों की सुरक्षा में मदद करते हैं।"),
        ("q9", "ATM का उपयोग किस लिए होता है?", ["नकद निकालने और बैंकिंग सेवाओं के लिए", "सोशल मीडिया पोस्ट के लिए", "फोन चार्ज करने के लिए", "ईमेल भेजने के लिए"], 0, "ATM से नकद निकाला जा सकता है और अन्य बैंकिंग सेवाएं मिल सकती हैं।"),
        ("q10", "आपातकालीन बचत किस काम आती है?", ["केवल मनोरंजन", "अचानक होने वाले खर्च", "खाते की जानकारी साझा करना", "ऑनलाइन गेम"], 1, "आपातकालीन बचत अचानक आने वाले खर्चों में मदद करती है।"),
        ("q11", "ऋण लेने से पहले क्या करना चाहिए?", ["बिना जांच ऋण लेना", "भुगतान की शर्तें अनदेखी करना", "ब्याज और भुगतान की शर्तें समझना", "PIN साझा करना"], 2, "ऋण लेने से पहले ब्याज, शुल्क और भुगतान की समय-सारणी समझें।"),
        ("q12", "कौन सी जानकारी निजी रखनी चाहिए?", ["बैंक का सार्वजनिक पता", "प्रकाशित बैंक फोन नंबर", "शाखा का सार्वजनिक स्थान", "आपका बैंकिंग OTP"], 3, "OTP और अन्य प्रमाणीकरण जानकारी निजी रखें।")
    ],

    "मराठी (Marathi)": [
        ("q1", "फोन करणाऱ्या व्यक्तीला OTP सांगावा का?", ["होय", "नाही", "फक्त अनोळखी व्यक्तींना", "फक्त रात्री"], 1, "तुमचा OTP कोणाशीही शेअर करू नका."),
        ("q2", "बँक खात्याचा मुख्य उपयोग काय आहे?", ["पैसे सुरक्षित ठेवणे", "फोन दुरुस्त करणे", "फक्त इंटरनेट खरेदी", "पासवर्ड तयार करणे"], 0, "बँक खात्यात पैसे जमा, सुरक्षित आणि काढता येतात."),
        ("q3", "UPI PIN कधी टाकावा?", ["पैसे मिळवण्यासाठी", "बक्षीस मिळवण्यासाठी", "पेमेंट मंजूर करण्यासाठी", "संदेश पाहण्यासाठी"], 2, "UPI PIN पेमेंट मंजूर करण्यासाठी असतो; पैसे मिळवण्यासाठी नाही."),
        ("q4", "संशयास्पद बँक लिंक मिळाल्यास काय करावे?", ["लगेच उघडावी", "पुढे पाठवावी", "PIN टाकावा", "उघडू नये आणि बँकेकडून खात्री करावी"], 3, "संशयास्पद लिंक टाळा आणि बँकेच्या अधिकृत माध्यमातून खात्री करा."),
        ("q5", "बजेट कशाचा हिशोब ठेवण्यास मदत करते?", ["उत्पन्न आणि खर्च", "फक्त फोन कॉल", "फक्त पासवर्ड", "फक्त वाढदिवस"], 0, "बजेटमुळे उत्पन्न आणि खर्चाचा हिशोब ठेवता येतो."),
        ("q6", "नियमित बचत का महत्त्वाची आहे?", ["लगेच जास्त खर्च करण्यासाठी", "भविष्यातील गरजांसाठी तयार राहण्यासाठी", "PIN शेअर करण्यासाठी", "नोंदी टाळण्यासाठी"], 1, "नियमित बचत भविष्यातील आणि अचानक येणाऱ्या खर्चांसाठी मदत करते."),
        ("q7", "भारतात ऑनलाइन आर्थिक फसवणुकीचा संशय असल्यास काय करावे?", ["दुर्लक्ष करावे", "सर्व पुरावे मिटवावेत", "अधिकृत माध्यमातून त्वरित तक्रार करावी", "OTP शेअर करावा"], 2, "सायबर आर्थिक फसवणुकीची तक्रार 1930 वर कॉल करून किंवा cybercrime.gov.in वर करता येते."),
        ("q8", "पासवर्ड ठेवण्याची सुरक्षित पद्धत कोणती?", ["फक्त स्वतःचे नाव", "मित्रांसोबत शेअर करणे", "सर्वत्र एकच सोपा पासवर्ड", "मजबूत आणि वेगळा पासवर्ड"], 3, "मजबूत आणि वेगळे पासवर्ड खात्यांचे संरक्षण करतात."),
        ("q9", "ATM कशासाठी वापरतात?", ["पैसे काढण्यासाठी आणि बँकिंग सेवांसाठी", "सोशल मीडिया पोस्टसाठी", "फोन चार्ज करण्यासाठी", "ईमेल पाठवण्यासाठी"], 0, "ATM मधून पैसे काढता येतात आणि इतर बँकिंग सेवा वापरता येतात."),
        ("q10", "आपत्कालीन निधी कशासाठी असतो?", ["फक्त मनोरंजनासाठी", "अचानक येणाऱ्या खर्चांसाठी", "खात्याची माहिती शेअर करण्यासाठी", "ऑनलाइन खेळांसाठी"], 1, "आपत्कालीन निधी अनपेक्षित खर्च भागवण्यास मदत करतो."),
        ("q11", "कर्ज घेण्यापूर्वी काय करावे?", ["तपासणी न करता कर्ज घ्यावे", "परतफेडीच्या अटींकडे दुर्लक्ष करावे", "व्याज आणि परतफेडीच्या अटी समजून घ्याव्यात", "PIN शेअर करावा"], 2, "कर्ज घेण्यापूर्वी व्याज, शुल्क आणि परतफेडीचे वेळापत्रक समजून घ्या."),
        ("q12", "कोणती माहिती गोपनीय ठेवावी?", ["बँकेचा सार्वजनिक पत्ता", "प्रकाशित बँक फोन नंबर", "शाखेचे सार्वजनिक ठिकाण", "तुमचा बँकिंग OTP"], 3, "OTP आणि इतर प्रमाणीकरण माहिती गोपनीय ठेवा.")
    ]
}

UI = {
    "English": {
        "title": "📝 Financial Literacy Quiz",
        "intro": "A new set of 5 questions is randomly selected from the question bank.",
        "submit": "Check My Answers", "choose": "Choose an answer",
        "unanswered": "Please answer all questions first.",
        "score": "Your score", "excellent": "Excellent work!",
        "good": "Good effort! Read the explanations and try again.",
        "retry": "🔄 New Questions", "home": "🏠 Back to Home"
    },
    "ಕನ್ನಡ (Kannada)": {
        "title": "📝 ಆರ್ಥಿಕ ಸಾಕ್ಷರತೆ ರಸಪ್ರಶ್ನೆ",
        "intro": "ಪ್ರಶ್ನೆಗಳ ಸಂಗ್ರಹದಿಂದ ಹೊಸ 5 ಪ್ರಶ್ನೆಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಲಾಗುತ್ತದೆ.",
        "submit": "ಉತ್ತರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ", "choose": "ಉತ್ತರವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "unanswered": "ದಯವಿಟ್ಟು ಎಲ್ಲಾ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿ.",
        "score": "ನಿಮ್ಮ ಅಂಕ", "excellent": "ಅತ್ಯುತ್ತಮ ಪ್ರಯತ್ನ!",
        "good": "ಚೆನ್ನಾಗಿದೆ! ವಿವರಣೆಗಳನ್ನು ಓದಿ ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ.",
        "retry": "🔄 ಹೊಸ ಪ್ರಶ್ನೆಗಳು", "home": "🏠 ಮುಖಪುಟಕ್ಕೆ ಹಿಂತಿರುಗಿ"
    },
    "हिन्दी (Hindi)": {
        "title": "📝 वित्तीय साक्षरता प्रश्नोत्तरी",
        "intro": "प्रश्नों के संग्रह से 5 नए सवाल चुने जाते हैं।",
        "submit": "मेरे उत्तर जांचें", "choose": "उत्तर चुनें",
        "unanswered": "कृपया पहले सभी सवालों के जवाब दें।",
        "score": "आपका स्कोर", "excellent": "बहुत अच्छा!",
        "good": "अच्छी कोशिश! जवाबों की व्याख्या पढ़ें और फिर प्रयास करें।",
        "retry": "🔄 नए सवाल", "home": "🏠 होम पर वापस जाएं"
    },
    "मराठी (Marathi)": {
        "title": "📝 आर्थिक साक्षरता प्रश्नमंजुषा",
        "intro": "प्रश्नसंचातून 5 नवीन प्रश्न यादृच्छिकपणे निवडले जातात.",
        "submit": "माझी उत्तरे तपासा", "choose": "उत्तर निवडा",
        "unanswered": "कृपया आधी सर्व प्रश्नांची उत्तरे द्या.",
        "score": "तुमचे गुण", "excellent": "उत्तम काम!",
        "good": "छान प्रयत्न! स्पष्टीकरणे वाचा आणि पुन्हा प्रयत्न करा.",
        "retry": "🔄 नवीन प्रश्न", "home": "🏠 मुख्यपृष्ठावर परत जा"
    }
}

t = UI.get(language, UI["English"])
bank = BANK.get(language, BANK["English"])

# Pick questions once per quiz round, so normal Streamlit reruns
# do not unexpectedly change questions or erase answers.
if st.session_state.get("quiz_language") != language:
    st.session_state["quiz_language"] = language
    st.session_state["quiz_round"] = 0
    st.session_state["quiz_submitted"] = False
    st.session_state["quiz_questions"] = random.sample(bank, 5)

if "quiz_questions" not in st.session_state:
    st.session_state["quiz_round"] = 0
    st.session_state["quiz_submitted"] = False
    st.session_state["quiz_questions"] = random.sample(bank, 5)

st.title(t["title"])
st.write(t["intro"])
st.divider()

questions = st.session_state["quiz_questions"]
answers = []

for i, (qid, question, options, correct, explanation) in enumerate(questions):
    st.subheader(f"{i + 1}. {question}")
    answer = st.radio(
        t["choose"],
        options,
        index=None,
        key=f"answer_{st.session_state['quiz_round']}_{qid}"
    )
    answers.append(answer)

st.divider()

if st.button(t["submit"], use_container_width=True):
    if any(answer is None for answer in answers):
        st.warning(t["unanswered"])
    else:
        score = sum(
            answer == options[correct]
            for answer, (_, _, options, correct, _) in zip(answers, questions)
        )
        st.session_state["quiz_score"] = score
        st.session_state["quiz_submitted"] = True

if st.session_state.get("quiz_submitted", False):
    score = st.session_state.get("quiz_score", 0)
    st.subheader(f"{t['score']}: {score}/5")

    if score >= 4:
        st.success(t["excellent"])
    else:
        st.info(t["good"])

    for i, (_, question, options, correct, explanation) in enumerate(questions):
        st.write(f"**{i + 1}. {question}**")
        st.write(f"✅ {options[correct]}")
        st.caption(explanation)

    if st.button(t["retry"], use_container_width=True):
        st.session_state["quiz_round"] += 1
        st.session_state["quiz_questions"] = random.sample(bank, 5)
        st.session_state["quiz_submitted"] = False
        st.session_state.pop("quiz_score", None)
        st.rerun()

if st.button(t["home"], use_container_width=True):
    st.session_state.pop("quiz_questions", None)
    st.session_state.pop("quiz_score", None)
    st.session_state["quiz_submitted"] = False
    st.switch_page("app.py")
