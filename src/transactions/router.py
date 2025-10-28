from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.transactions.schemas import STransactionAdd
from src.transactions.service import TransactionService
from src.database import get_session


transactions_router = APIRouter(
    prefix='/transactions',
    tags=['Transactions'],
)


@transactions_router.post('')
async def add_transaction(transaction: STransactionAdd, session: AsyncSession = Depends(get_session)):
    service = TransactionService(session)
    try:
        result = await service.add_transaction(transaction)
        return {'ok': True, 'id': result}
    except Exception:
        raise HTTPException(status_code=400, detail='Не удалось добавить транзакцию')
    
    
@transactions_router.get('/{transaction_id}')
async def get_transaction(transaction_id: int, session: AsyncSession = Depends(get_session)):
    service = TransactionService(session)
    try:
        result = await service.get_transaction(transaction_id)
        if not result:
            raise Exception('Transaction does not exists.')
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return {'ok': True, 'data': result}