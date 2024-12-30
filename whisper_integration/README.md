# Whisper-tiny Integration for AI Explorer

## Model Overview
OpenAI's Whisper-tiny is a lightweight speech recognition model optimized for efficiency:
- Parameters: 39M
- Task: Speech-to-Text
- Languages: Multilingual support
- Hardware: CPU-compatible (no GPU required)
- Memory Usage: <1GB RAM

## Installation

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

### Setup Steps
```bash
# Clone repository
git clone https://github.com/omegalabsinc/omega-awesome-a2a.git
cd omega-awesome-a2a

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
Running the Integration
Start the Backend API
bash
Copy
uvicorn api:app --reload --host 0.0.0.0 --port 8000
Launch the UI
bash
Copy
streamlit run whisper_integration/ui/streamlit_app.py
API Endpoints
GET /info
Returns model information and capabilities

json
Copy
{
    "name": "Whisper-tiny",
    "version": "1.0",
    "type": "speech_recognition",
    "description": "Lightweight speech recognition model",
    "parameters": "39M",
    "input_format": [".wav", ".mp3", ".m4a"],
    "output_format": "text",
    "provider": "OpenAI",
    "license": "MIT"
}
POST /transcribe
Transcribes audio files to text

Input: Audio file (wav, mp3, m4a)
Output: JSON with transcribed text
Performance Benchmarks
Model Load Time: 69.57 seconds (CPU)
CUDA Support: Optional
Memory Footprint: ~800MB
Average Transcription Speed: ~2x realtime
Testing
bash
Copy
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/test_model.py
pytest tests/test_integration.py
Project Structure
unknown
Copy
whisper_integration/
├── api.py                 # FastAPI backend
├── model_handler.py       # Whisper model wrapper
├── benchmark.py          # Performance testing
├── ui/
│   └── streamlit_app.py  # Frontend interface
└── tests/
    ├── test_model.py     # Model tests
    └── test_integration.py # API tests
Contributing
Fork the repository
Create feature branch
Commit changes
Push to branch
Create Pull Request
Troubleshooting
Model Loading Slow: Normal for first load, model is cached after
Audio Not Playing: Check file format compatibility
Memory Issues: Reduce audio file size or clear cache
License
MIT License - See LICENSE file for details