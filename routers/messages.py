from fastapi import APIRouter, HTTPException
from models.message import Message
from typing import List

router = APIRouter()

# Временное хранилище для сообщений
messages_db = []


@router.post("/send/", response_model=Message)
async def send_message(message: Message):
    messages_db.append(message)
    return message


@router.get("/messages/{email}", response_model=List[Message])
async def get_messages(email: str):
    user_messages = [msg for msg in messages_db if msg.receiver == email]
    if not user_messages:
        raise HTTPException(status_code=404, detail="Messages not found")
    return user_messages