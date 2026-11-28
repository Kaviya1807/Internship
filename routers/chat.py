from fastapi import APIRouter
from schemas import ChatRequest

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    message = request.message.lower().strip()

    if "hello" in message:
        reply = "Hello! How are you?"

    elif "hi" in message:
        reply = "Hi! Welcome!"

    elif "python" in message:
        reply = "Python is a programming language."

    elif "bye" in message:
        reply = "Goodbye!"

    else:
        reply = "Sorry, I don't understand."

    return {
        "user_message": request.message,
        "reply": reply
    }