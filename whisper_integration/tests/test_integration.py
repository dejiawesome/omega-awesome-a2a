# tests/test_integration.py
import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_info_endpoint():
    response = client.get("/info")
    assert response.status_code == 200
    assert "name" in response.json()
    assert response.json()["name"] == "Whisper-tiny"

def test_transcribe_endpoint():
    # Create a sample audio file for testing
    audio_path = "tests/test_files/sample.wav"
    with open(audio_path, "rb") as f:
        response = client.post(
            "/transcribe",
            files={"file": ("sample.wav", f, "audio/wav")}
        )
    assert response.status_code == 200
    assert "text" in response.json()
