import openai
from typing import List, Dict

# Встав сюди свій ключ (або використовуй os.getenv, якщо будеш з .env)
openai.api_key = "your-openai-key-here"

# Глобальна історія для однієї сесії (для кількох юзерів треба буде зберігати по id)
chat_history: List[Dict[str, str]] = [
    {"role": "system", "content": "Ти веселий помічник. Відповідай із гумором, але по темі."}
]

def ask_llm(user_input: str) -> str:
    chat_history.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # або gpt-4, якщо є доступ
        messages=chat_history,
        temperature=0.8,
        max_tokens=500,
    )

    assistant_reply = response.choices[0].message["content"]
    chat_history.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply
