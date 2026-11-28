from fastapi import FastAPI
from routers import students, chat

app = FastAPI(title="Student and Chat API")

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(students.router)
app.include_router(chat.router)