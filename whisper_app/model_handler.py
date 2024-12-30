import whisper
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WhisperHandler:
    def __init__(self, model_size="tiny"):
        logger.info(f"Initializing Whisper model with size: {model_size}")
        self.model = whisper.load_model(model_size)
        
    def transcribe(self, audio_path):
        """
        Transcribe audio file to text
        Args:
            audio_path (str): Path to audio file
        Returns:
            str: Transcribed text
        """
        try:
            audio_path = Path(audio_path)
            if not audio_path.exists():
                raise FileNotFoundError(f"Audio file not found: {audio_path}")
                
            logger.info(f"Transcribing audio file: {audio_path}")
            result = self.model.transcribe(str(audio_path))
            return result["text"].strip()
            
        except Exception as e:
            logger.error(f"Error during transcription: {str(e)}")
            raise

    def get_model_info(self):
        """Return basic model information"""
        return {
            "model_type": "Whisper-tiny",
            "parameters": "39M",
            "languages": "multilingual",
            "description": "Lightweight speech recognition model"
        }
