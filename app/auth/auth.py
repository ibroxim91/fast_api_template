from app.db import AsyncSessionLocal
from app.models.user import User as UserModel
from sqlalchemy import select
from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")




async def get_user_by_username(username: str):
    """Get user by username"""
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(UserModel).where(UserModel.username == username))
        return result.scalar_one_or_none()
    

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password"""
    return pwd_context.verify(plain_password, hashed_password)    


async def authenticate_user(username: str, password: str):
    """Authenticate user"""
    user = await get_user_by_username(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user