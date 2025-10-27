from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base


_engine = create_async_engine('sqlite+aiosqlite:///FinanceTracker')
AsyncSessionLocal = async_sessionmaker(_engine, expire_on_commit=False)


def start_engine():
    DB_URL = 'sqlite+aiosalite:///FinanceTracker'   
    global _engine 
    
    if not _engine:
        _engine = create_async_engine(DB_URL)
      
    
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session


Base = declarative_base()

async def create_tables():
    async with _engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
        
async def drop_tables():
    async with _engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)