from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .company import Company
    from .user import User


class CompanyRelationMixin:
    _company_id_nullable: bool = False
    _company_id_unique: bool = False
    _company_back_populates: str | None = None

    @declared_attr
    def company_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("company.id"),
            unique=cls._company_id_unique,
            nullable=cls._company_id_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["Company"]:
        return relationship(
            "Company",
            back_populates=cls._company_back_populates,
        )



class UserRelationMixin:
    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("user.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship(
            "User",
            back_populates=cls._user_back_populates,
        )