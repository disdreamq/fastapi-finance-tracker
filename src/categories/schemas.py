from datetime import datetime
from pydantic import BaseModel


class SCategoryAdd(BaseModel):
    name: str
    type: str
    created_at: datetime
    
           
class SCategoryResponse(BaseModel):
    id: int
    name: str
    type: str
    created_at: datetime
    updated_at: datetime | None = None
    
    model_config = {"from_attributes": True} 