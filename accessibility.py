    # Read Aloud
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔊 Read Aloud")

    text_to_read = st.sidebar.text_area(
        "Enter text to hear",
        key="accessibility_read_text",
        placeholder="Type or paste text here..."
    )

    # Clear the previous reading whenever the text changes
    if (
        "last_read_text" not in st.session_state
        or st.session_state["last_read_text"] != text_to_read
    ):
        st.session_state["text_ready_to_read"] = ""
        st.session_state["last_read_text"] = text_to_read

    if st.sidebar.button("🔊 Read text aloud"):
        if text_to_read.strip():
            st.session_state["text_ready_to_read"] = text_to_read
        else:
            st.session_state["text_ready_to_read"] = ""
            st.sidebar.warning("Please enter text first.")

    # Display the player only for the currently submitted text
    if (
        text_to_read.strip()
        and st.session_state.get("text_ready_to_read") == text_to_read
    ):
        st.sidebar.caption("Your text is ready. Press Play to listen.")

        components.html(
            f"""
            <div style="font-family:Arial,sans-serif;padding:8px;">
                <button id="play" style="padding:10px;font-size:16px;">
                    ▶ Play
                </button>
                <button id="stop" style="padding:10px;font-size:16px;">
                    ■ Stop
                </button>
                <p id="status" aria-live="polite">Ready to play.</p>
            </div>
            <script>
            const textToRead = {json.dumps(text_to_read)};
            const status = document.getElementById("status");

            document.getElementById("play").onclick = () => {{
                if (!window.speechSynthesis) {{
                    status.textContent = "Speech is not supported.";
                    return;
                }}

                window.speechSynthesis.cancel();

                const utterance = new SpeechSynthesisUtterance(textToRead);
                utterance.lang = "en-IN";

                utterance.onstart = () => status.textContent = "Speaking...";
                utterance.onend = () => status.textContent = "Finished.";
                utterance.onerror = (event) =>
                    status.textContent = "Speech error: " + event.error;

                window.speechSynthesis.speak(utterance);
            }};

            document.getElementById("stop").onclick = () => {{
                if (window.speechSynthesis) window.speechSynthesis.cancel();
                status.textContent = "Speech stopped.";
            }};
            </script>
            """,
            height=115
        )
