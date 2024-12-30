import pytest
import os
from whisper_integration.model_handler import WhisperHandler

def test_model_initialization():
    handler = WhisperHandler()
    assert handler.model is not None
    assert handler.model_name == "tiny"

def test_model_info():
    handler = WhisperHandler()
    info = handler.get_model_info()
    assert isinstance(info, dict)
    assert "model_type" in info
    assert "parameters" in info
    assert info["model_type"] == "tiny"

@pytest.mark.slow  # Mark as slow test since it downloads test file
def test_transcription():
    # Create a simple test audio file or use a small sample
    # For now, we'll just test if the method exists
    handler = WhisperHandler()
    assert hasattr(handler, 'transcribe')
