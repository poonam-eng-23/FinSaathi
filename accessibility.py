
import streamlit as st


def apply_accessibility():
    if "accessibility_mode" not in st.session_state:
        st.session_state["accessibility_mode"] = False

    st.sidebar.toggle(
        "♿ Accessibility Mode",
        key="accessibility_mode",
        help="Make text larger and controls easier to use."
    )

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
                border: 2px solid #333333 !important;
            }

            .stApp button:focus-visible,
            .stApp input:focus-visible,
            .stApp textarea:focus-visible {
                outline: 3px solid #005fcc !important;
                outline-offset: 3px !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
