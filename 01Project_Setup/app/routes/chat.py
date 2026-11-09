from fastapi import APIRouter

router = APIRouter()


@router.get("/chat")
def get_chat():
    return {"message": "Chat route working"}


@router.post("/chat")
def create_chat():
    return {"message": "Chat created"}
