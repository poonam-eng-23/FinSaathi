
import streamlit as st
import streamlit.components.v1 as components


def apply_accessibility():
    st.sidebar.markdown("---")
    st.sidebar.subheader("♿ Accessibility Settings")

    # Larger Text
    larger_text = st.sidebar.checkbox(
        "🔎 Larger Text",
        key="accessibility_larger_text"
    )

    # High Contrast Mode
    high_contrast = st.sidebar.checkbox(
        "🎨 High Contrast Mode",
        key="accessibility_high_contrast"
    )

    # Apply accessibility styles
    if larger_text:
        st.markdown(
            """
            <style>
            html, body, [class*="st-"] {
                font-size: 20px !important;
            }
            p, label, li {
                font-size: 20px !important;
                line-height: 1.6 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    if high_contrast:
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #000000 !important;
                color: #FFFFFF !important;
            }
            [data-testid="stSidebar"] {
                background-color: #000000 !important;
            }
            p, label, h1, h2, h3, h4, span, li {
                color: #FFFFFF !important;
            }
            input, textarea, select {
                background-color: #FFFFFF !important;
                color: #000000 !important;
            }
            button {
                border: 2px solid #FFFFFF !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Read Aloud
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔊 Read Aloud")

    components.html(
        """
        <div style="font-family:Arial,sans-serif;padding:8px;">
            <textarea id="readText"
                placeholder="Type or paste text here..."
                style="width:100%;height:100px;font-size:16px;
                box-sizing:border-box;"></textarea>

            <div style="margin-top:8px;">
                <button id="play"
                    style="padding:10px;font-size:16px;">
                    ▶ Play
                </button>
                <button id="stop"
                    style="padding:10px;font-size:16px;">
                    ■ Stop
                </button>
            </div>

            <p id="status" aria-live="polite">Ready to play.</p>
        </div>

        <script>
        const textBox = document.getElementById("readText");
        const status = document.getElementById("status");

        function stopSpeech() {
            if ("speechSynthesis" in window) {
                window.speechSynthesis.cancel();
            }
        }

        textBox.addEventListener("input", () => {
            stopSpeech();
            status.textContent = textBox.value.trim()
                ? "Text changed. Press Play to listen."
                : "Text cleared. Nothing to read.";
        });

        document.getElementById("play").onclick = () => {
            const text = textBox.value.trim();

            stopSpeech();

            if (!text) {
                status.textContent = "Please enter text first.";
                return;
            }

            if (!("speechSynthesis" in window)) {
                status.textContent = "Speech is not supported by this browser.";
                return;
            }

            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = "en-IN";

            utterance.onstart = () => {
                status.textContent = "Speaking...";
            };

            utterance.onend = () => {
                status.textContent = "Finished.";
            };

            utterance.onerror = () => {
                status.textContent = "Speech stopped or unavailable.";
            };

            window.speechSynthesis.speak(utterance);
        };

        document.getElementById("stop").onclick = () => {
            stopSpeech();
            status.textContent = "Speech stopped.";
        };
        </script>
        """,
        height=240
    )

    # Voice Input
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎤 Voice Input")

    if hasattr(st, "audio_input"):
        audio_value = st.sidebar.audio_input(
            "Record your question",
            key="accessibility_voice_input"
        )

        if audio_value is not None:
            st.sidebar.info(
                "Recording received. Automatic speech-to-text "
                "requires a speech recognition service."
            )
    else:
        st.sidebar.caption(
            "Voice recording is not supported in this Streamlit version."
        )
