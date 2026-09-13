from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Phase 6B FastAPI acceptance"}
