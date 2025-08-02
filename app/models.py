from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int
    price: float

class ProductRead(ProductCreate):
    id: int

    class Config:
        orm_mode = True
