from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Raymund backend live"}

@app.get("/health")
def health():
    return {"status": "ok"}
