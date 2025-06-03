import os
from dotenv import load_dotenv
from typing import List, Dict
from openai import OpenAI
import httpx

load_dotenv()

transport = httpx.HTTPTransport(proxy=None)
http_client = httpx.Client(transport=transport)

# Кастомний httpx клієнт бо проблеми через статичне DNS на локалі
client = OpenAI(http_client=http_client)

chat_history: List[Dict[str, str]] = [
    {"role": "system", "content": "Ти веселий помічник. Відповідай з гумором, але не відходь від теми."}
]

def ask_llm(user_input: str) -> str:
    chat_history.append({"role": "user", "content": user_input})

    print("Using model: gpt-3.5-turbo")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=0.8,
        max_tokens=500,
    )

    assistant_reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply
