from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Company
from app.schemas import CompanyCreate, CompanyUpdate

__all__ = ["create_company", "get_company", "update_company"]

# Company qo'shish (Asinxron)
async def create_company(db: AsyncSession, company: CompanyCreate):
    db_company = Company(**company.dict())
    db.add(db_company)
    await db.commit()
    await db.refresh(db_company)
    return db_company

# Company o'qish (Asinxron)
async def get_company(db: AsyncSession, company_id: int):
    result = await db.execute(select(Company).filter(Company.id == company_id))
    db_company = result.scalars().first()
    return db_company


# Company yangilash (Asinxron)
async def update_company(db: AsyncSession, company_id: int, company: CompanyUpdate):
    result = await db.execute(select(Company).filter(Company.id == company_id))
    db_company = result.scalars().first()

    if db_company:
        for key, value in company.dict(exclude_unset=True).items():
            setattr(db_company, key, value)
        await db.commit()
        await db.refresh(db_company)

    return db_company
