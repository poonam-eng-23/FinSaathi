
import streamlit as st
import requests

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

    response = requests.post(
        "https://api.sarvam.ai/translate",
        headers={
            "api-subscription-key": api_key,
            "Content-Type": "application/json",
        },
        json={
            "input": text[:2000],
            "source_language_code": "en-IN",
            "target_language_code": target_code,
            "model": "sarvam-translate:v1",
        },
        timeout=30,
    )

    if not response.ok:
        try:
            details = response.json().get("error", {})
            message = details.get("message", response.text)
            code = details.get("code", "unknown_error")
        except (ValueError, AttributeError):
            message = response.text
            code = "unknown_error"

        raise RuntimeError(
            f"HTTP {response.status_code} | {code} | {message}"
        )

    return response.json()["translated_text"]


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
        return translated if translated else text

    except Exception as e:
        error = str(e)[:500]

        if st.session_state.get("_last_translation_error") != error:
            st.session_state["_last_translation_error"] = error
            st.error(f"Translation failed: {error}")

        return text
