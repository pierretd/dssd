from typing import Dict, List, Optional

# In-memory database for demonstration purposes
items_db: Dict[str, dict] = {
    "foo": {"id": "foo", "name": "Foo", "price": 50.2, "description": "An item called Foo"},
    "bar": {"id": "bar", "name": "Bar", "price": 62, "description": "An item called Bar"}
}

def get_items() -> List[dict]:
    """Get all items"""
    return list(items_db.values())

def get_item(item_id: str) -> Optional[dict]:
    """Get a specific item by ID"""
    return items_db.get(item_id)

def create_item(item_id: str, item_data: dict) -> dict:
    """Create a new item"""
    new_item = {**item_data, "id": item_id}
    items_db[item_id] = new_item
    return new_item

def update_item(item_id: str, item_data: dict) -> Optional[dict]:
    """Update an existing item"""
    if item_id not in items_db:
        return None
    
    updated_item = {**items_db[item_id], **item_data}
    items_db[item_id] = updated_item
    return updated_item

def delete_item(item_id: str) -> bool:
    """Delete an item"""
    if item_id not in items_db:
        return False
    
    del items_db[item_id]
    return True 