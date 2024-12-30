import streamlit as st
from pathlib import Path
import tempfile
import os
from ..model_handler import WhisperHandler

st.title("Whisper Speech Recognition")

@st.cache_resource
def load_model():
    return WhisperHandler()

model = load_model()

# Display model info
model_info = model.get_model_info()
st.sidebar.header("Model Information")
for key, value in model_info.items():
    st.sidebar.text(f"{key}: {value}")

# File uploader
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

if audio_file is not None:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(audio_file.name).suffix) as tmp_file:
        tmp_file.write(audio_file.getvalue())
        tmp_file_path = tmp_file.name

    try:
        with st.spinner("Transcribing..."):
            transcription = model.transcribe(tmp_file_path)
        st.success("Transcription Complete!")
        st.text_area("Transcription", transcription, height=200)
    except Exception as e:
        st.error(f"Error during transcription: {str(e)}")
    finally:
        # Cleanup
        os.unlink(tmp_file_path)
