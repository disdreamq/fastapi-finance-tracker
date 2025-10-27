from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.categories.models import Category
from src.categories.schemas import SCategoryAdd


class AbstractRepository(ABC):
    @abstractmethod
    async def add_category():
        raise NotImplementedError
    
    
class CategoryRepository(AbstractRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_category(self, category_id: int) -> Category:
        stmt = select(Category).filter(Category.id == category_id)
        result = await self.session.execute(stmt)
        return result.scalar_one()
    
    async def get_category_by_name(self, category_name: str) -> Category | None:
        stmt = select(Category).filter(Category.name == category_name)
        try:
            result = await self.session.execute(stmt)
            return result.scalar_one()
        except Exception:
            return  
    
    async def add_category(self, category: SCategoryAdd) -> Category:
        category_to_add = Category(name = category.name, type = category.type, created_at = category.created_at)
        self.session.add(category_to_add)
        await self.session.flush()
        await self.session.commit()
        return category_to_add

    async def delete_category(self, category_id: int) -> bool:
        category_to_delete = await self.get_category(category_id)
        if category_to_delete:
            await self.session.delete(category_to_delete)
            await self.session.commit()
            return True
        return False
    
    async def update_category(self, category_id:int, name: str | None, type: str | None ) -> bool:
        category_to_update = await self.get_category(category_id)
        if category_to_update:
            if not name and not type:
                return False
            if name:
                category_to_update.name = name
            if type: 
                category_to_update.type = type
            await self.session.commit()
            return True
        return False