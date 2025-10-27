from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.transactions.schemas import STransactionAdd
from src.transactions.service import TransactionService
from src.database import get_session


transactions_router = APIRouter(
    prefix='/transactions',
    tags=['Transactions'],
)


#TODO доделать эндпоинты для транзакций