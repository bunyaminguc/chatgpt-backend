from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv  # .env dosyasını yüklemek için

# .env dosyasını yükle
load_dotenv()

app = FastAPI()

# OpenAI API anahtarını ortam değişkeninden al
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=OPENAI_API_KEY)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
