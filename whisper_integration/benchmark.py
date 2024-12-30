# Add to benchmark.py
def test_cached_load():
    # First load - should be slow
    start = time.time()
    handler1 = WhisperHandler()
    first_load = time.time() - start
    
    # Second load - should be fast
    start = time.time()
    handler2 = WhisperHandler()
    cached_load = time.time() - start
    
    return {
        "first_load": first_load,
        "cached_load": cached_load
    }
