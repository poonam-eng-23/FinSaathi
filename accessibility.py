
import io
import json
import streamlit as st
import streamlit.components.v1 as components


def apply_accessibility():
    # Remember settings while navigating between pages
    if "accessibility_mode" not in st.session_state:
        st.session_state["accessibility_mode"] = False

    if "high_contrast_mode" not in st.session_state:
        st.session_state["high_contrast_mode"] = False

    st.sidebar.markdown("---")
    st.sidebar.subheader("♿ Accessibility")

    st.sidebar.toggle(
        "Larger Text",
        key="accessibility_mode",
        help="Increase text size and spacing."
    )

    st.sidebar.toggle(
        "High Contrast Mode",
        key="high_contrast_mode",
        help="Use stronger text and background contrast."
    )

    # Larger text
    if st.session_state["accessibility_mode"]:
        st.markdown(
            """
            <style>
            .stApp p,
            .stApp li,
            .stApp label,
            .stApp .stMarkdown {
                font-size: 1.15rem !important;
                line-height: 1.7 !important;
            }

            .stApp button {
                min-height: 48px !important;
                font-size: 1.05rem !important;
                font-weight: 600 !important;
            }

            .stApp input,
            .stApp textarea {
                font-size: 1.1rem !important;
            }

            button:focus-visible,
            input:focus-visible,
            textarea:focus-visible {
                outline: 3px solid #005fcc !important;
                outline-offset: 3px !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # High contrast
    if st.session_state["high_contrast_mode"]:
        st.markdown(
            """
            <style>
            .stApp,
            [data-testid="stSidebar"] {
                background-color: #ffffff !important;
                color: #000000 !important;
            }

            .stApp p,
            .stApp li,
            .stApp label,
            .stApp h1,
            .stApp h2,
            .stApp h3,
            .stApp .stMarkdown,
            [data-testid="stSidebar"] p,
            [data-testid="stSidebar"] label {
                color: #000000 !important;
            }

            .stApp button,
            [data-testid="stSidebar"] button {
                background-color: #000000 !important;
                color: #ffffff !important;
                border: 2px solid #000000 !important;
            }

            .stApp input,
            .stApp textarea,
            .stApp select {
                background-color: #ffffff !important;
                color: #000000 !important;
                border: 2px solid #000000 !important;
            }

            a {
                color: #003399 !important;
                text-decoration: underline !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Read Aloud
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔊 Read Aloud")
    st.sidebar.caption(
        "Enter or paste the text you want to hear."
    )

    language = st.session_state.get("language", "English")

    speech_languages = {
        "English": "en-IN",
        "ಕನ್ನಡ": "kn-IN",
        "Kannada": "kn-IN",
        "हिन्दी": "hi-IN",
        "Hindi": "hi-IN",
        "मराठी": "mr-IN",
        "Marathi": "mr-IN",
    }

    speech_language = speech_languages.get(
        language, "en-IN"
    )

    text_to_read = st.sidebar.text_area(
        "Text to read",
        key="accessibility_read_text",
        placeholder="Enter instructions or a safety tip here."
    )

    if st.sidebar.button(
        "🔊 Open Read Aloud",
        key="open_read_aloud"
    ):
        if text_to_read.strip():
            safe_text = json.dumps(text_to_read).replace(
                "<", "\\u003c"
            )
            safe_language = json.dumps(speech_language)

            components.html(
                f"""
                <div style="font-family: sans-serif;
                            padding: 8px;">
                    <button id="speak"
                        style="font-size:18px;padding:12px;
                               min-height:48px;cursor:pointer;">
                        ▶ Read text aloud
                    </button>
                    <button id="stop"
                        style="font-size:18px;padding:12px;
                               min-height:48px;cursor:pointer;">
                        ■ Stop
                    </button>
                    <p id="status" aria-live="polite">
                        Press Read text aloud to listen.
                    </p>
                </div>
                <script>
                const message = {safe_text};
                const lang = {safe_language};

                document.getElementById("speak").onclick = () => {{
                    if (!("speechSynthesis" in window)) {{
                        document.getElementById("status").textContent =
                            "Speech playback is not supported by this browser.";
                        return;
                    }}

                    window.speechSynthesis.cancel();
                    const utterance =
                        new SpeechSynthesisUtterance(message);
                    utterance.lang = lang;

                    utterance.onerror = () => {{
                        document.getElementById("status").textContent =
                            "Could not play the speech. Try another browser.";
                    }};

                    window.speechSynthesis.speak(utterance);
                    document.getElementById("status").textContent =
                        "Playing speech...";
                }};

                document.getElementById("stop").onclick = () => {{
                    if ("speechSynthesis" in window) {{
                        window.speechSynthesis.cancel();
                    }}
                    document.getElementById("status").textContent =
                        "Speech stopped.";
                }};
                </script>
                """,
                height=150
            )
        else:
            st.sidebar.info(
                "Enter some text before using Read Aloud."
            )

    # Voice Input
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎤 Voice Input")
    st.sidebar.caption(
        "Record your question, then convert it to text."
    )

    audio = st.sidebar.audio_input(
        "Record your question",
        key="accessibility_voice_recording"
    )

    if audio is not None and st.sidebar.button(
        "Convert Speech to Text",
        key="convert_voice_question"
    ):
        try:
            import speech_recognition as sr

            recognizer = sr.Recognizer()

            with sr.AudioFile(io.BytesIO(audio.getvalue())) as source:
                recorded_audio = recognizer.record(source)

            recognized_text = recognizer.recognize_google(
                recorded_audio,
                language=speech_language
            )

            st.session_state["voice_question"] = recognized_text

        except ImportError:
            st.sidebar.error(
                "Voice input needs the SpeechRecognition package. "
                "Add it to requirements.txt."
            )
        except sr.UnknownValueError:
            st.sidebar.warning(
                "Speech was not clear enough. Please try recording again."
            )
        except sr.RequestError:
            st.sidebar.error(
                "Speech recognition is unavailable. Check your "
                "internet connection and try again."
            )
        except Exception as error:
            st.sidebar.error(
                f"Could not process the recording: {error}"
            )

    if st.session_state.get("voice_question"):
        st.sidebar.markdown("**Recognized question:**")
        st.sidebar.write(st.session_state["voice_question"])

        st.sidebar.button(
            "Clear voice question",
            key="clear_voice_question",
            on_click=lambda: st.session_state.pop(
                "voice_question", None
            )
        )
