import torch
import time
import json
import platform
import psutil
import whisper
from pathlib import Path

def get_system_info():
    return {
        "os": platform.system(),
        "python_version": platform.python_version(),
        "cpu": platform.processor(),
        "ram": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
        "cuda_available": torch.cuda.is_available(),
        "torch_version": torch.__version__
    }

def benchmark_model():
    results = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "system_info": get_system_info(),
        "model_benchmarks": {}
    }
    
    # Model loading benchmark
    print("Testing model loading times...")
    start_time = time.time()
    model = whisper.load_model("tiny")
    load_time = time.time() - start_time
    
    results["model_benchmarks"]["load_time"] = load_time
    results["model_benchmarks"]["model_size"] = "tiny"
    results["model_benchmarks"]["parameters"] = "39M"
    
    # Save results
    with open("benchmark_results.json", "w") as f:
        json.dump(results, f, indent=4)
    
    return results

if __name__ == "__main__":
    print("Starting Whisper Model Benchmark Suite...")
    results = benchmark_model()
    
    print("\n📊 Benchmark Results:")
    print(f"Model Load Time: {results['model_benchmarks']['load_time']:.2f}s")
    print(f"System: {results['system_info']['os']}")
    print(f"CUDA Available: {results['system_info']['cuda_available']}")
    print(f"RAM: {results['system_info']['ram']}")
    print("\nFull results saved to benchmark_results.json")
