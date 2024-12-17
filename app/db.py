from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .config import settings
from contextlib import asynccontextmanager

# Asinxron engine yaratish
DATABASE_URL = settings.db.url
engine = create_async_engine(DATABASE_URL, echo=settings.db.echo, future=True)

# Asinxron session uchun sessionmaker
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)



# Asinxron db sessiyasini olish uchun yordamchi funksiya

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
