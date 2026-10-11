
import streamlit as st
from sarvamai import SarvamAI

LANGUAGE_CODES = {
    "English": "en-IN",
    "অসমীয়া": "as-IN",
    "বাংলা": "bn-IN",
    "बड़ो": "brx-IN",
    "डोगरी": "doi-IN",
    "ગુજરાતી": "gu-IN",
    "हिन्दी": "hi-IN",
    "ಕನ್ನಡ": "kn-IN",
    "کٲشُر": "ks-IN",
    "कोंकणी": "kok-IN",
    "मैथिली": "mai-IN",
    "മലയാളം": "ml-IN",
    "মৈতৈলোন্": "mni-IN",
    "मराठी": "mr-IN",
    "नेपाली": "ne-IN",
    "ଓଡ଼ିଆ": "od-IN",
    "ਪੰਜਾਬੀ": "pa-IN",
    "संस्कृत": "sa-IN",
    "ᱥᱟᱱᱛᱟᱲᱤ": "sat-IN",
    "سنڌي": "sd-IN",
    "தமிழ்": "ta-IN",
    "తెలుగు": "te-IN",
    "اردو": "ur-IN",
}

LANGUAGES = list(LANGUAGE_CODES.keys())


def get_selected_language():
    return st.session_state.get("language", "English")


@st.cache_data(show_spinner=False)
def _translate_text(text, target_code):
    api_key = st.secrets["SARVAM_API_KEY"]

    client = SarvamAI(
        api_subscription_key=api_key
    )

    response = client.text.translate(
        input=text[:2000],
        source_language_code="en-IN",
        target_language_code=target_code,
        model="sarvam-translate:v1",
    )

    return response.translated_text


def tr(text):
    if not isinstance(text, str):
        return text

    language = get_selected_language()

    if language == "English":
        return text

    target_code = LANGUAGE_CODES.get(language)

    if not target_code:
        return text

    try:
        translated = _translate_text(text, target_code)

        if translated:
            return translated

        return text

    except Exception as e:
        error_message = (
            f"{type(e).__name__}: {str(e)[:300]}"
        )

        if st.session_state.get(
            "_last_translation_error"
        ) != error_message:
            st.session_state[
                "_last_translation_error"
            ] = error_message

            st.error(
                "Translation failed. Please check this error: "
                + error_message
            )

        return text
