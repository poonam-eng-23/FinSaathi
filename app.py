
# FinSaathi: 22 Indian languages + English

LANGUAGES = {
    "English": "en-IN",
    "অসমীয়া — Assamese": "as-IN",
    "বাংলা — Bengali": "bn-IN",
    "बड़ो — Bodo": "brx-IN",
    "डोगरी — Dogri": "doi-IN",
    "ગુજરાતી — Gujarati": "gu-IN",
    "हिन्दी — Hindi": "hi-IN",
    "ಕನ್ನಡ — Kannada": "kn-IN",
    "کٲشُر — Kashmiri": "ks-IN",
    "कोंकणी — Konkani": "kok-IN",
    "मैथिली — Maithili": "mai-IN",
    "മലയാളം — Malayalam": "ml-IN",
    "মৈতৈলোন্ — Manipuri": "mni-IN",
    "मराठी — Marathi": "mr-IN",
    "नेपाली — Nepali": "ne-IN",
    "ଓଡ଼ିଆ — Odia": "od-IN",
    "ਪੰਜਾਬੀ — Punjabi": "pa-IN",
    "संस्कृतम् — Sanskrit": "sa-IN",
    "ᱥᱟᱱᱛᱟᱲᱤ — Santali": "sat-IN",
    "سنڌي — Sindhi": "sd-IN",
    "தமிழ் — Tamil": "ta-IN",
    "తెలుగు — Telugu": "te-IN",
    "اردو — Urdu": "ur-IN",
}

selected_language = st.selectbox(
    "🌐 Choose your language / ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
    list(LANGUAGES.keys()),
    key="finsaathi_language"
)

st.session_state["language_name"] = selected_language
st.session_state["language_code"] = LANGUAGES[selected_language]
