from datetime import datetime, timezone
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Добро пожаловать в Time Server API"}


@app.get("/time")
def get_time():
    return {"utc_time": datetime.now(timezone.utc).isoformat()}


@app.get("/date")
def get_date():
    return {"utc_date": datetime.now(timezone.utc).date().isoformat()}