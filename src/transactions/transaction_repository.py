from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.transactions.models import Transaction
from src.transactions.schemas import STransactionAdd


class AbstractRepository(ABC):
    @abstractmethod
    async def add_transaction():
        raise NotImplementedError
    
    
class TransactionRepository(AbstractRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_transaction(self, tr_id: int) -> Transaction:
        stmt = select(Transaction).filter(Transaction.id == tr_id)
        result = await self.session.execute(stmt)
        return result.scalar_one()
    
    async def get_transaction_by_name(self, tr_name: str) -> Transaction | None:
        stmt = select(Transaction).filter(Transaction.name == tr_name)
        try:
            result = await self.session.execute(stmt)
            return result.scalar_one()
        except Exception:
            return  
    
    async def add_transaction(self, transaction: STransactionAdd) -> Transaction:
        transaction_to_add = Transaction(
            amount = transaction.amount, 
            description = transaction.description if transaction.description else '', 
            date = transaction.date, 
            category_id = transaction.category_id,
            created_at = transaction.created_at,
        )
        self.session.add(transaction_to_add)
        await self.session.flush()
        await self.session.commit()
        return transaction_to_add

    async def delete_transaction(self, transaction_id: int) -> bool:
        transaction_to_delete = await self.get_transaction(transaction_id)
        if transaction_to_delete:
            await self.session.delete(transaction_to_delete)
            await self.session.commit()
            return True
        return False
    
