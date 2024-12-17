from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import *
from app.db import get_db  # DBga bog'lanish uchun dependecy

company_router = APIRouter()

# Company yaratish
@company_router.post("/", response_model=dict)
async def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = await crud.create_company(db=db, company=company)  # Asinxron funksiyani await bilan chaqirish
    return {"success": True}


# # Company o'qish
# @router.get("/companies/{company_id}", response_model=schemas.CompanyRead)
# def read_company(company_id: int, db: Session = Depends(get_db)):
#     db_company = crud.get_company(db=db, company_id=company_id)
#     if db_company is None:
#         raise HTTPException(status_code=404, detail="Company not found")
#     return db_company
#
# # Company yangilash
# @router.put("/companies/{company_id}", response_model=schemas.CompanyRead)
# def update_company(company_id: int, company: schemas.CompanyUpdate, db: Session = Depends(get_db)):
#     db_company = crud.update_company(db=db, company_id=company_id, company=company)
#     if db_company is None:
#         raise HTTPException(status_code=404, detail="Company not found")
#     return db_company
