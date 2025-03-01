from fastapi import FastAPI
from src.operations.router import router as book_rt

app = FastAPI(title="Book API")

app.include_router(book_rt)


@app.get("/")
async def home():
    return {"Message": "Hello, World!", "Info": "Go to doc"}
