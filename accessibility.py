import io
import json
import streamlit as st
import streamlit.components.v1 as components


def apply_accessibility():
    st.session_state.setdefault("accessibility_mode", False)
    st.session_state.setdefault("high_contrast_mode", False)

    st.sidebar.markdown("---")
    st.sidebar.subheader("♿ Accessibility")

    st.sidebar.toggle("Larger Text", key="accessibility_mode")
    st.sidebar.toggle("High Contrast Mode", key="high_contrast_mode")

    if st.session_state["accessibility_mode"]:
        st.markdown(
            """
            <style>
            .stApp p, .stApp li, .stApp label,
            .stApp .stMarkdown {
                font-size: 1.15rem !important;
                line-height: 1.7 !important;
            }
            .stApp button {
                min-height: 48px !important;
                font-size: 1.05rem !important;
            }
            *:focus-visible {
                outline: 3px solid #005fcc !important;
                outline-offset: 3px !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    if st.session_state["high_contrast_mode"]:
        st.markdown(
            """
            <style>
            .stApp, [data-testid="stSidebar"] {
                background: #ffffff !important;
                color: #000000 !important;
            }
            .stApp p, .stApp li, .stApp label,
            .stApp h1, .stApp h2, .stApp h3,
            .stApp .stMarkdown,
            [data-testid="stSidebar"] p,
            [data-testid="stSidebar"] label {
                color: #000000 !important;
            }
            .stApp button, [data-testid="stSidebar"] button {
                background: #000000 !important;
                color: #ffffff !important;
                border: 2px solid #000000 !important;
            }
            .stApp input, .stApp textarea {
                background: #ffffff !important;
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

    text_to_read = st.sidebar.text_area(
        "Enter text to hear",
        key="accessibility_read_text",
        placeholder="Type or paste text here..."
    )

    if st.sidebar.button("🔊 Read text aloud"):
        if text_to_read.strip():
            st.session_state["text_ready_to_read"] = text_to_read
        else:
            st.sidebar.warning("Please enter some text first.")

    if st.session_state.get("text_ready_to_read"):
        speech_text = json.dumps(
            st.session_state["text_ready_to_read"]
        )

        components.html(
            f"""
            <div style="font-family:Arial,sans-serif;padding:8px;">
                <button id="play" style="padding:10px;font-size:16px;">
                    ▶ Play
                </button>
                <button id="stop" style="padding:10px;font-size:16px;">
                    ■ Stop
                </button>
                <p id="status" aria-live="polite">
                    Press Play to listen.
                </p>
            </div>

            <script>
            const textToRead = {speech_text};
            const status = document.getElementById("status");

            function speakText() {{
                if (!window.speechSynthesis ||
                    !window.SpeechSynthesisUtterance) {{
                    status.textContent =
                        "Speech is not supported. Try Microsoft Edge.";
                    return;
                }}

                const synth = window.speechSynthesis;
                synth.cancel();

                const voices = synth.getVoices();

                if (!voices.length) {{
                    status.textContent =
                        "No speech voices available. Check your browser's speech settings and reload the page.";
                    return;
                }}

                const utterance =
                    new SpeechSynthesisUtterance(textToRead);

                utterance.lang = "en-IN";

                const voice =
                    voices.find(v => v.lang === "en-IN") ||
                    voices.find(v => v.lang.startsWith("en-")) ||
                    voices.find(v => v.lang.startsWith("en"));

                if (voice) {{
                    utterance.voice = voice;
                }}

                utterance.onstart = () => {{
                    status.textContent = "Speaking...";
                }};

                utterance.onend = () => {{
                    status.textContent = "Finished reading.";
                }};

                utterance.onerror = (event) => {{
                    status.textContent =
                        "Speech error: " + event.error +
                        ". Try reloading the page or using Microsoft Edge.";
                }};

                synth.speak(utterance);
            }}

            document.getElementById("play").onclick = speakText;

            document.getElementById("stop").onclick = () => {{
                if (window.speechSynthesis) {{
                    window.speechSynthesis.cancel();
                }}
                status.textContent = "Speech stopped.";
            }};

            if (window.speechSynthesis) {{
                window.speechSynthesis.onvoiceschanged = () => {{}};
            }}
            </script>
            """,
            height=125
        )

    # Voice Input
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎤 Voice Input")

    audio = st.sidebar.audio_input("Record your question")

    if audio is not None and st.sidebar.button("Convert speech to text"):
        try:
            import speech_recognition as sr

            recognizer = sr.Recognizer()

            with sr.AudioFile(io.BytesIO(audio.getvalue())) as source:
                recorded_audio = recognizer.record(source)

            recognized_text = recognizer.recognize_google(
                recorded_audio,
                language="en-IN"
            )

            st.session_state["voice_question"] = recognized_text

        except ImportError:
            st.sidebar.error(
                "Install SpeechRecognition in requirements.txt."
            )
        except Exception:
            st.sidebar.error(
                "Could not recognize speech. Try again and check your internet connection."
            )

    if st.session_state.get("voice_question"):
        st.sidebar.write("Recognized question:")
        st.sidebar.write(st.session_state["voice_question"])

        if st.sidebar.button("Clear voice question"):
            st.session_state.pop("voice_question", None)
            st.rerun()
