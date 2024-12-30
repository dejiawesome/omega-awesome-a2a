# Updated model_handler.py with caching
import torch
import whisper
import os
from pathlib import Path

class WhisperHandler:
    _model_cache = {}  # Class-level cache
    
    def __init__(self, model_name="tiny"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Check cache first
        if model_name not in self._model_cache:
            # Check if model is already downloaded
            cache_dir = os.path.expanduser("~/.cache/whisper")
            model_path = Path(cache_dir) / f"{model_name}.pt"
            
            if model_path.exists():
                print(f"Loading model from cache: {model_path}")
            else:
                print("Downloading model (first time only)")
                
            self._model_cache[model_name] = whisper.load_model(model_name)
            
        self.model = self._model_cache[model_name]
