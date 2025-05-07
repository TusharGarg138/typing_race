import streamlit as st
import random
import time

# List of sample texts
text_samples = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and versatile programming language.",
    "Typing fast and accurately takes practice and focus.",
    "JavaScript adds interactivity to your websites.",
    "Frontend development is fun with HTML, CSS, and JS."
]

st.title("Typing Race Game 🏁")

# Session state initialization
if 'text_to_type' not in st.session_state:
    st.session_state.text_to_type = random.choice(text_samples)
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'finished' not in st.session_state:
    st.session_state.finished = False

# Start button
if st.button("Start New Test"):
    st.session_state.text_to_type = random.choice(text_samples)
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.session_state.typed_text = ""

# Show the text to type
st.markdown("### Type this:")
st.write(st.session_state.text_to_type)

# User input box
typed = st.text_input("Start typing here:", value=st.session_state.get("typed_text", ""), disabled=st.session_state.finished)

# Store the typed text
st.session_state.typed_text = typed

# Check for completion
if not st.session_state.finished and typed.strip() == st.session_state.text_to_type.strip():
    end_time = time.time()
    elapsed = end_time - st.session_state.start_time
    word_count = len(st.session_state.text_to_type.split())
    wpm = (word_count / elapsed) * 60
    st.success(f"✅ Finished in {elapsed:.2f} seconds! Your speed: {wpm:.2f} WPM")
    st.session_state.finished = True
