from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.categories.schemas import SCategoryAdd
from src.categories.service import CategoryService
from src.database import get_session


categories_router = APIRouter(
    prefix='/categories',
    tags=['Categories'],
    
)


@categories_router.post('')
async def add_category(category: SCategoryAdd, session: AsyncSession = Depends(get_session)):
    service = CategoryService(session)
    try:
        result = await service.add_category(category)
        return {'ok': True, 'id': result}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='category with that name already exists.')

    

@categories_router.get('/{category_id}')
async def get_category(category_id: int, session: AsyncSession = Depends(get_session)):
    service = CategoryService(session)
    try:
        result = await service.get_category(category_id)
        if not result:
            raise Exception('Category dont exist')
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
    return {'ok': True, 'data': result}