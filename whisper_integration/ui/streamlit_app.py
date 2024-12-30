# whisper_integration/ui/streamlit_app.py
import streamlit as st
import requests
import io
from audio_recorder_streamlit import audio_recorder
import tempfile
import os

st.set_page_config(page_title="Whisper AI Explorer", layout="wide")

def main():
    st.title("🎤 Whisper Speech Recognition")
    
    # Sidebar with model info
    with st.sidebar:
        st.header("Model Information")
        info = requests.get("http://localhost:8000/info").json()
        st.json(info)
    
    # Main interface
    st.header("Speech to Text")
    
    # File upload option
    uploaded_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])
    
    # Live recording option
    st.write("Or record audio directly:")
    audio_bytes = audio_recorder()
    
    if uploaded_file:
        process_audio(uploaded_file)
    elif audio_bytes:
        process_recorded_audio(audio_bytes)

def process_audio(audio_file):
    with st.spinner("Transcribing..."):
        files = {"file": audio_file}
        response = requests.post("http://localhost:8000/transcribe", files=files)
        if response.status_code == 200:
            st.success("Transcription Complete!")
            st.text_area("Transcribed Text:", response.json()["text"], height=150)
        else:
            st.error(f"Error: {response.text}")

def process_recorded_audio(audio_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_bytes)
        tmp_file_path = tmp_file.name
    
    try:
        with open(tmp_file_path, "rb") as audio_file:
            process_audio(audio_file)
    finally:
        os.unlink(tmp_file_path)

if __name__ == "__main__":
    main()
