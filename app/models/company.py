from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Company(Base):
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
