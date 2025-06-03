import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chat import ask_llm

app = FastAPI()

# Дозволяємо звернення з фронту
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    text: str


@app.post("/chat")
def chat_endpoint(message: Message):
    reply = ask_llm(message.text)
    return {"reply": reply}


uvicorn.run(app,host='0.0.0.0',port=8000)
