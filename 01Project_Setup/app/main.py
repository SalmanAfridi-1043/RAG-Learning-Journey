from fastapi import FastAPI
from app.routes import chat
from app.core.config import APP_NAME, DEBUG

app = FastAPI(title=APP_NAME, debug=DEBUG)

app.include_router(chat.router)


@app.get("/")
def home():
    return {"message": "Welcome to RAG Practice API"}
