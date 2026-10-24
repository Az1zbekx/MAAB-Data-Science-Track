from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()


class EchoRequest(BaseModel):
    data: Any


@app.get("/")
def root():
    return {
        "message": "FastAPI Fundamentals API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/echo")
def echo(request: EchoRequest):
    return request