
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
                status.textContent =
                    "Speech is not supported by this browser.";
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
                status.textContent =
                    "Speech stopped or unavailable.";
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

    # Browser Voice Recognition
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎤 Voice Input")

    components.html(
        """
        <div style="font-family:Arial,sans-serif;padding:8px;
                    color:inherit;">
            <label for="voiceLanguage"
                   style="font-size:15px;font-weight:bold;">
                Choose your speaking language
            </label>

            <select id="voiceLanguage"
                    style="width:100%;padding:10px;
                           margin:8px 0;font-size:16px;">
                <option value="en-IN">English</option>
                <option value="kn-IN">ಕನ್ನಡ (Kannada)</option>
                <option value="hi-IN">हिन्दी (Hindi)</option>
                <option value="mr-IN">मराठी (Marathi)</option>
            </select>

            <button id="startVoice"
                    style="width:100%;padding:12px;
                           font-size:16px;cursor:pointer;">
                🎤 Start Speaking
            </button>

            <button id="stopVoice"
                    style="width:100%;padding:10px;
                           margin-top:8px;font-size:16px;
                           cursor:pointer;" disabled>
                ■ Stop Recording
            </button>

            <p id="voiceStatus" aria-live="polite">
                Choose a language and press Start Speaking.
            </p>

            <label for="recognizedText"
                   style="font-size:15px;font-weight:bold;">
                Recognized text
            </label>

            <textarea id="recognizedText"
                      placeholder="Your spoken words will appear here..."
                      style="width:100%;height:120px;
                             box-sizing:border-box;
                             padding:10px;font-size:16px;"
                      aria-live="polite"></textarea>

            <button id="copyVoice"
                    style="width:100%;padding:10px;
                           margin-top:8px;font-size:16px;">
                📋 Copy Recognized Text
            </button>

            <p style="font-size:13px;line-height:1.5;">
                After copying, paste the text into the question
                box on the AI Assistant page.
            </p>
        </div>

        <script>
        const startButton = document.getElementById("startVoice");
        const stopButton = document.getElementById("stopVoice");
        const languageSelect = document.getElementById("voiceLanguage");
        const recognizedText = document.getElementById("recognizedText");
        const voiceStatus = document.getElementById("voiceStatus");
        const copyButton = document.getElementById("copyVoice");

        const SpeechRecognition =
            window.SpeechRecognition ||
            window.webkitSpeechRecognition;

        let recognition = null;
        let finalText = "";
        let manuallyStopped = false;

        if (!SpeechRecognition) {
            startButton.disabled = true;
            voiceStatus.textContent =
                "Voice recognition is not supported here. " +
                "Try an updated version of Google Chrome.";
        }

        if (SpeechRecognition) {
            recognition = new SpeechRecognition();
            recognition.continuous = true;
            recognition.interimResults = true;

            recognition.onstart = () => {
                voiceStatus.textContent = "Listening... Speak now.";
                startButton.disabled = true;
                stopButton.disabled = false;
            };

            recognition.onresult = (event) => {
                let interimText = "";

                for (let i = event.resultIndex;
                     i < event.results.length; i++) {
                    const transcript = event.results[i][0].transcript;

                    if (event.results[i].isFinal) {
                        finalText += transcript + " ";
                    } else {
                        interimText += transcript;
                    }
                }

                recognizedText.value = finalText + interimText;
            };

            recognition.onerror = (event) => {
                voiceStatus.textContent =
                    "Recognition issue: " + event.error +
                    ". Check microphone permission and internet.";
            };

            recognition.onend = () => {
                startButton.disabled = false;
                stopButton.disabled = true;

                if (manuallyStopped) {
                    voiceStatus.textContent =
                        "Recording stopped. You can copy your text.";
                } else if (finalText.trim()) {
                    voiceStatus.textContent =
                        "Speech captured. Check the text below.";
                } else {
                    voiceStatus.textContent =
                        "No words captured. Please try again.";
                }
            };
        }

        startButton.onclick = () => {
            if (!recognition) return;

            finalText = "";
            recognizedText.value = "";
            manuallyStopped = false;
            recognition.lang = languageSelect.value;

            try {
                recognition.start();
            } catch (error) {
                voiceStatus.textContent =
                    "Please wait a moment and try again.";
            }
        };

        stopButton.onclick = () => {
            if (recognition) {
                manuallyStopped = true;
                recognition.stop();
            }
        };

        copyButton.onclick = async () => {
            const text = recognizedText.value.trim();

            if (!text) {
                voiceStatus.textContent =
                    "Speak first so there is text to copy.";
                return;
            }

            try {
                await navigator.clipboard.writeText(text);
                voiceStatus.textContent =
                    "Text copied. Paste it into your AI Assistant question box.";
            } catch (error) {
                recognizedText.focus();
                recognizedText.select();
                voiceStatus.textContent =
                    "Text selected. Press Ctrl+C to copy, then paste it into the AI Assistant.";
            }
        };
        </script>
        """,
        height=540
    )
