# Whisper Integration for AI Explorer

## Overview
This integration adds OpenAI's Whisper-tiny model to the AI Explorer interface, providing lightweight speech recognition capabilities.

## Features
- Speech-to-text transcription
- Support for multiple audio formats (.wav, .mp3, .m4a)
- Real-time audio recording and processing
- RESTful API integration

## Requirements
- Python 3.8+
- CUDA-capable GPU (optional)
- 4GB RAM minimum

## Quick Start
```bash
# Clone the repository
git clone https://github.com/omegalabsinc/omega-awesome-a2a.git
cd omega-awesome-a2a

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn api:app --reload --host 0.0.0.0 --port 8000

# Start the UI (in a new terminal)
streamlit run whisper_integration/ui/streamlit_app.py
API Endpoints
GET /info - Model information
POST /transcribe - Audio transcription
unknown
Copy

2. Record demonstration video:
```markdown
## Demo Recording Checklist

1. Introduction (30s)
   - [ ] Project overview
   - [ ] Model capabilities

2. Setup Demo (1min)
   - [ ] Show repository structure
   - [ ] Demonstrate installation process

3. Original Model Usage (1min)
   - [ ] Show basic Whisper model usage
   - [ ] Demonstrate transcription

4. AI Explorer Integration (2min)
   - [ ] Show API endpoints
   - [ ] Demonstrate UI interface
   - [ ] Test file upload
   - [ ] Test live recording

5. Comparison (30s)
   - [ ] Side-by-side comparison
   - [ ] Show identical results
Create PR Checklist:
Code files:
api.py
model_handler.py
ui/streamlit_app.py
tests/test_integration.py
Documentation:
README.md
Setup instructions
API documentation
Demo materials:
Screen recording
Sample audio files
Benchmark results
Tests:
Unit tests
Integration tests
Benchmark reports