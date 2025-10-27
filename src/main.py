from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.categories.router import categories_router
from src.database import create_tables, drop_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await drop_tables()
   

app = FastAPI(lifespan=lifespan)

app.include_router(categories_router)
