from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from app.models.item import Item, ItemCreate
from app.services import item_service

router = APIRouter(
    prefix="/api/items",
    tags=["items"],
    responses={404: {"description": "Item not found"}},
)

@router.get("/", response_model=List[Item], status_code=status.HTTP_200_OK)
async def read_items():
    """
    Get all items
    """
    return item_service.get_items()

@router.get("/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def read_item(item_id: str, q: Optional[str] = None):
    """
    Get a specific item by ID
    """
    item = item_service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if q:
        item = {**item, "q": q}
    return item

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item_id: str, item: ItemCreate):
    """
    Create a new item
    """
    existing_item = item_service.get_item(item_id)
    if existing_item:
        raise HTTPException(
            status_code=400,
            detail=f"Item with ID {item_id} already exists"
        )
    
    return item_service.create_item(item_id, item.dict())

@router.put("/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def update_item(item_id: str, item: ItemCreate):
    """
    Update an existing item
    """
    updated_item = item_service.update_item(item_id, item.dict())
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return updated_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str):
    """
    Delete an item
    """
    deleted = item_service.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found") 