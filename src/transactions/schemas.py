from datetime import datetime
from pydantic import BaseModel, Field


class STransactionAdd(BaseModel):
    amount: float
    description: str
    date: datetime
    date: datetime
    category_id: int
    created_at: datetime
    
           
class STransactionResponse(BaseModel):
    id: int
    amount: float = Field(ge=0)
    description: str
    date: datetime
    date: datetime
    category_id: int
    created_at: datetime
    updated_at: datetime | None = None
    
    model_config = {"from_attributes": True} 