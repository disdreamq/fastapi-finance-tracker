from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

Mode = 'TEST'

SQLALCHEMY_DATABASE_URL_TEST = "sqlite+aiosqlite:///:memory:"
SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///FinanceTracker'

db_url = SQLALCHEMY_DATABASE_URL if Mode == 'PROD' else SQLALCHEMY_DATABASE_URL_TEST

Base = declarative_base()
_engine = create_async_engine(db_url)
AsyncSessionLocal = async_sessionmaker(_engine, expire_on_commit=False)


def start_engine():
    DB_URL = 'sqlite+aiosalite:///FinanceTracker'   
    global _engine 
    
    if not _engine:
        _engine = create_async_engine(DB_URL)
      
    
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session



async def create_tables():
    async with _engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
        
async def drop_tables():
    async with _engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)