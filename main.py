from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "FastAPI is running"}

@app.get("/events")
def read_events():
    return {"status": "ok", "message": "responding the events"}