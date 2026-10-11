
import streamlit as st
from sarvamai import SarvamAI

# FinSaathi language support:
# English + 22 scheduled Indian languages

LANGUAGE_CODES = {
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


def translate_text(text, target_language="English"):
    """Translate English text into the selected language."""

    if not isinstance(text, str) or not text.strip():
        return text

    if target_language == "English":
        return text

    target_code = LANGUAGE_CODES.get(target_language)

    if not target_code:
        return text

    try:
        api_key = st.secrets["SARVAM_API_KEY"]

        client = SarvamAI(
            api_subscription_key=api_key
        )

        # The service accepts up to 2,000 characters
        # per translation request.
        if len(text) > 2000:
            return text

        response = client.text.translate(
            input=text,
            source_language_code="en-IN",
            target_language_code=target_code,
            model="sarvam-translate:v1",
        )

        return response.translated_text

    except Exception as error:
        print("FinSaathi translation error:", error)
        return text


def get_selected_language():
    """Return the language selected on the home page."""

    return st.session_state.get(
        "selected_language", "English"
    )


def tr(text):
    """Translate text using the currently selected language."""

    return translate_text(text, get_selected_language())
