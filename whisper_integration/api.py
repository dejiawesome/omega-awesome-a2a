from fastapi import FastAPI, UploadFile, File
from .integration import WhisperExplorerIntegration
import uvicorn

app = FastAPI()
model = WhisperExplorerIntegration()

@app.on_event("startup")
async def startup_event():
    model.initialize()

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    contents = await file.read()
    file_ext = os.path.splitext(file.filename)[1].lower()
    result = model.predict(contents, file_ext)
    return result

@app.get("/info")
async def get_model_info():
    return model.get_info()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
