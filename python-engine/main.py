from fastapi import FastAPI
from engine import pericia_apice

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}
