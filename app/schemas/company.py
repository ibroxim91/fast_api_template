from pydantic import BaseModel, EmailStr
from typing import Optional

__all__ = ["CompanyCreate", "CompanyRead", "CompanyUpdate"]

class CompanyCreate(BaseModel):
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None



class CompanyRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None

    class Config:
        orm_mode = True



class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None
