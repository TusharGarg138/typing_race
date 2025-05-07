import streamlit as st
import time
import random

# Set page title and layout
st.set_page_config(page_title="Typing Speed Test 💻", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background: radial-gradient(circle at top left, #f5e9ff, #e5d4ff);
        }
        .main-box {
            background-color: #ffffffcc;
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        .typing-box {
            border: 2px solid #b36bff;
            border-radius: 10px;
            padding: 1rem;
            background: #f9f1ff;
            margin-bottom: 1rem;
        }
        .stButton > button {
            background-color: #a44ee5;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            border: none;
            padding: 0.5rem 1.5rem;
            margin: 0.5rem 0.5rem 0 0;
        }
        .stButton > button:hover {
            background-color: #9334db;
        }
        .metric-label {
            font-size: 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title and container
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #5c0d9b;'>⌨️ Test Yo' Typing Speed 🌀</h2>", unsafe_allow_html=True)

# Sample texts
text_samples = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and versatile programming language.",
    "Typing fast and accurately takes practice and focus.",
    "JavaScript adds interactivity to your websites.",
    "Frontend development is fun with HTML, CSS, and JS."
]

# Session state setup
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'text_to_type' not in st.session_state:
    st.session_state.text_to_type = random.choice(text_samples)
if 'finished' not in st.session_state:
    st.session_state.finished = False

# Button handlers
def start_test():
    st.session_state.text_to_type = random.choice(text_samples)
    st.session_state.start_time = time.time()
    st.session_state.finished = False

def reset_test():
    st.session_state.start_time = None
    st.session_state.finished = False
    st.session_state.typing_area = ""

# Buttons
col1, col2 = st.columns(2)
with col1:
    st.button("🚀 Start", on_click=start_test)
with col2:
    st.button("🔁 Reset", on_click=reset_test)

# Typing area
if st.session_state.start_time:
    st.markdown('<div class="typing-box">', unsafe_allow_html=True)
    st.markdown(f"**Text to Type:**\n\n`{st.session_state.text_to_type}`")
    typed_text = st.text_area("Start typing here...", height=150, key="typing_area")
    st.markdown('</div>', unsafe_allow_html=True)

    elapsed_time = time.time() - st.session_state.start_time
    elapsed_time = max(elapsed_time, 1)

    if typed_text.strip() == st.session_state.text_to_type.strip():
        st.session_state.finished = True

    if st.session_state.finished:
        words = len(st.session_state.text_to_type.split())
        wpm = round((words / elapsed_time) * 60)
        accuracy = sum(1 for a, b in zip(typed_text, st.session_state.text_to_type) if a == b) / max(len(st.session_state.text_to_type), 1) * 100

        st.success("✅ Test Completed!")
        col1, col2, col3 = st.columns(3)
        col1.metric("⚡ Speed", f"{wpm} WPM")
        col2.metric("🎯 Accuracy", f"{accuracy:.2f}%")
        col3.metric("⏱️ Time", f"{elapsed_time:.2f} sec")

st.markdown('</div>', unsafe_allow_html=True)
