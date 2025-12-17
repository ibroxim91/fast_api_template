from typing import Optional
from pydantic import BaseModel


__all__ = ["Token", "TokenData", "User", "UserResponse"]



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


# Схема данных для пользователя
class UserAuth(BaseModel):
    username: str
    password: str



class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str] = None
    role: str


    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str]
    role: Optional[str]



    class Config:
        # orm_mode = True
        from_attributes = True