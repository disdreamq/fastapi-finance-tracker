from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, Float, CheckConstraint, ForeignKey

from database import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[float] = mapped_column(Float, CheckConstraint('amount > 0'), nullable=False)
    description: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)