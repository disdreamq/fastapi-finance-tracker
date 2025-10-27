from sqlalchemy.ext.asyncio import AsyncSession

from src.categories.schemas import SCategoryAdd, SCategoryResponse
from src.categories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.repository = CategoryRepository(session)
        
    async def get_category(self, category_id:int) -> SCategoryResponse:
        category = await self.repository.get_category(category_id)
        return SCategoryResponse.model_validate(category)
    
    async def get_category_by_name(self, category_name: str) -> SCategoryResponse | None:
        category = await self.repository.get_category_by_name(category_name)
        if category:
            return SCategoryResponse.model_validate(category)
        return
        
    async def add_category(self, category_to_add: SCategoryAdd) -> int:
        res = await self.get_category_by_name(category_to_add.name)
        if res:
            raise
        category = await self.repository.add_category(category_to_add)
        return SCategoryResponse.model_validate(category).id
    
    