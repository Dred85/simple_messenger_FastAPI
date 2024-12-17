from fastapi import APIRouter
from models.user import User

router = APIRouter()

# Временное хранилище для пользователей
users_db = []


@router.post("/register/", response_model=User)
async def register_user(user: User):
    users_db.append(user)
    return user