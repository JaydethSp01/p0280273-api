from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class StockItem(BaseModel):
    producto_id: int
    cantidad: int

stock_db = [
    StockItem(producto_id=1, cantidad=50),
    StockItem(producto_id=2, cantidad=30),
]

@router.get("/stock", response_model=List[StockItem])
async def get_stock():
    return stock_db

@router.post("/stock", response_model=StockItem)
async def create_stock_item(stock_item: StockItem):
    stock_db.append(stock_item)
    return stock_item

@router.get("/stock/{producto_id}", response_model=StockItem)
async def get_stock_item(producto_id: int):
    for item in stock_db:
        if item.producto_id == producto_id:
            return item
    raise HTTPException(status_code=404, detail="Stock item not found")

@router.put("/stock/{producto_id}", response_model=StockItem)
async def update_stock_item(producto_id: int, updated_stock_item: StockItem):
    for i, item in enumerate(stock_db):
        if item.producto_id == producto_id:
            stock_db[i] = updated_stock_item
            return updated_stock_item
    raise HTTPException(status_code=404, detail="Stock item not found")

@router.delete("/stock/{producto_id}")
async def delete_stock_item(producto_id: int):
    for i, item in enumerate(stock_db):
        if item.producto_id == producto_id:
            del stock_db[i]
            return {"detail": "Stock item deleted"}
    raise HTTPException(status_code=404, detail="Stock item not found")
