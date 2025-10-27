from sqlalchemy.ext.asyncio import AsyncSession

from src.transactions.schemas import STransactionResponse, STransactionAdd
from src.transactions.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self, session: AsyncSession):
        self.repository = TransactionRepository(session)
        
    async def get_transaction(self, transaction_id:int) -> STransactionResponse:
        tr = await self.repository.get_transaction(transaction_id)
        return STransactionResponse.model_validate(tr)
    
    async def get_category_by_name(self, category_name: str) -> STransactionResponse | None:
        tr = await self.repository.get_transaction_by_name(category_name)
        if tr:
            return STransactionResponse.model_validate(tr)
        return
        
    async def add_transaction(self, transaction_to_add: STransactionAdd) -> int: 
        tr = await self.repository.add_transaction(transaction_to_add)
        return STransactionResponse.model_validate(tr).id
    
    