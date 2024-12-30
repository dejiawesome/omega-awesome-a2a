from typing import Dict, Any
import whisper
import logging
from pathlib import Path
import tempfile
import os

logger = logging.getLogger(__name__)

class WhisperExplorerIntegration:
    """AI Explorer Integration for Whisper Model"""
    
    def __init__(self):
        self.model = None
        self.model_name = "tiny"
        self.supported_types = [".wav", ".mp3", ".m4a"]
        
    def initialize(self) -> Dict[str, Any]:
        """Initialize the model and return configuration"""
        try:
            self.model = whisper.load_model(self.model_name)
            return {
                "status": "success",
                "model_name": self.model_name,
                "supported_formats": self.supported_types,
                "max_duration": "30 minutes",
                "languages": "multilingual"
            }
        except Exception as e:
            logger.error(f"Model initialization failed: {str(e)}")
            return {"status": "error", "message": str(e)}

    def predict(self, audio_data: bytes, file_extension: str) -> Dict[str, Any]:
        """Process audio and return transcription"""
        if not self.model:
            return {"status": "error", "message": "Model not initialized"}
            
        if file_extension not in self.supported_types:
            return {
                "status": "error", 
                "message": f"Unsupported file type. Supported: {self.supported_types}"
            }
            
        try:
            # Save temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
                tmp_file.write(audio_data)
                tmp_path = tmp_file.name
            
            # Transcribe
            result = self.model.transcribe(tmp_path)
            
            # Cleanup
            os.unlink(tmp_path)
            
            return {
                "status": "success",
                "text": result["text"],
                "language": result.get("language", "unknown"),
                "segments": result.get("segments", [])
            }
            
        except Exception as e:
            logger.error(f"Transcription failed: {str(e)}")
            return {"status": "error", "message": str(e)}

    def get_info(self) -> Dict[str, Any]:
        """Return model information"""
        return {
            "name": "Whisper-tiny",
            "version": "1.0",
            "type": "speech_recognition",
            "description": "Lightweight speech recognition model",
            "parameters": "39M",
            "input_format": self.supported_types,
            "output_format": "text",
            "provider": "OpenAI",
            "license": "MIT"
        }
