from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_home():
    return {"Hello": "World"}