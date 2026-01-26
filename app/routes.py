from fastapi import APIRouter 
from .models import Item

router = APIRouter() 

items = [] 

@router.post("/items") 
def create_item(item: Item): 
    items.append(item) 
    return {"status": "created", "item": item} 

@router.get("/items") 
def get_items(): 
    return items 

@router.put("/items/{index}") 
def update_item(index: int, item: Item): 
    items[index] = item 
    return {"status": "updated", "item": item} 

@router.delete("/items/{index}") 
def delete_item(index: int): 
    deleted_item = items.pop(index) 
    return {"status": "deleted", "item": deleted_item}