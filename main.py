from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_home():
    return {"Hello": "World"}

@app.post("/media")
async def get_medialib():
    return {"medialib": "medialib"}

