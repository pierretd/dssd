from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    """Base class for Item models"""
    name: str
    price: float = Field(..., ge=0)
    description: Optional[str] = None

class ItemCreate(ItemBase):
    """Class for creating items"""
    pass

class Item(ItemBase):
    """Class for responses with items"""
    id: str

    class Config:
        schema_extra = {
            "example": {
                "id": "foo",
                "name": "Foo",
                "price": 50.2,
                "description": "An item called Foo"
            }
        } 