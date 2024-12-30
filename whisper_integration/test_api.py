import requests
import os

def test_api():
    # Base URL
    base_url = "http://localhost:8000"
    
    # Test info endpoint
    print("Testing INFO endpoint...")
    info_response = requests.get(f"{base_url}/info")
    print(f"Status: {info_response.status_code}")
    print(f"Response: {info_response.json()}\n")
    
    # Test transcription endpoint with sample audio
    print("Testing TRANSCRIBE endpoint...")
    audio_path = "test_audio.wav"  # Make sure this file exists
    
    with open(audio_path, 'rb') as audio_file:
        files = {'file': ('test.wav', audio_file, 'audio/wav')}
        transcribe_response = requests.post(f"{base_url}/transcribe", files=files)
        print(f"Status: {transcribe_response.status_code}")
        print(f"Response: {transcribe_response.json()}")

if __name__ == "__main__":
    test_api()
