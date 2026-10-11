import streamlit as st

LANGUAGE_CODES = {
    "English": "en-IN",
    "हिन्दी — Hindi": "hi-IN",
    "ಕನ್ನಡ — Kannada": "kn-IN",
    "मराठी — Marathi": "mr-IN",
    "বাংলা — Bengali": "bn-IN",
    "ગુજરાતી — Gujarati": "gu-IN",
    "தமிழ் — Tamil": "ta-IN",
    "తెలుగు — Telugu": "te-IN",
    "മലയാളം — Malayalam": "ml-IN",
    "ਪੰਜਾਬੀ — Punjabi": "pa-IN",
    "اردو — Urdu": "ur-IN",
    "ଓଡ଼ିଆ — Odia": "od-IN",
    "অসমীয়া — Assamese": "as-IN",
    "कोंकणी — Konkani": "kok-IN",
    "नेपाली — Nepali": "ne-IN",
    "संस्कृतम् — Sanskrit": "sa-IN",
    "मैथिली — Maithili": "mai-IN",
    "डोगरी — Dogri": "doi-IN",
    "बड़ो — Bodo": "brx-IN",
    "کٲشُر — Kashmiri": "ks-IN",
    "মৈতৈলোন্ — Manipuri": "mni-IN",
    "ᱥᱟᱱᱛᱟᱲᱤ — Santali": "sat-IN",
    "سنڌي — Sindhi": "sd-IN",
}


def get_selected_language():
    return st.session_state.get("selected_language", "English")


def translate_text(text, target_language="English"):
    if not isinstance(text, str) or not text.strip():
        return text

    # Translation is temporarily disabled while the SDK issue is fixed.
    return text


def tr(text):
    return translate_text(text, get_selected_language())
