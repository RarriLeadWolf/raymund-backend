
from fastapi import FastAPI, UploadFile, File
import pandas as pd
import numpy as np

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    values = df.select_dtypes(include=[np.number])

    if values.empty:
        return {"error": "No numeric data"}

    std_dev = values.std().mean()
    mean_val = values.mean().mean()

    score = (std_dev / (mean_val + 1)) * 100
    score = max(0, min(100, score))

    status = "Normal"
    if score > 60:
        status = "Elevated"
    elif score > 30:
        status = "Watch"

    return {
        "threat_score": round(score, 2),
        "status": status
    }