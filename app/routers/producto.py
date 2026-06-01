from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    categoria: str
    precio: float

productos_db = [
    Producto(id=1, nombre="Producto 1", categoria="Categoría A", precio=100.0),
    Producto(id=2, nombre="Producto 2", categoria="Categoría B", precio=150.0),
]

@router.get("/productos", response_model=List[Producto])
async def get_productos():
    return productos_db

@router.post("/productos", response_model=Producto)
async def create_producto(producto: Producto):
    productos_db.append(producto)
    return producto

@router.get("/productos/{producto_id}", response_model=Producto)
async def get_producto(producto_id: int):
    for producto in productos_db:
        if producto.id == producto_id:
            return producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.put("/productos/{producto_id}", response_model=Producto)
async def update_producto(producto_id: int, updated_producto: Producto):
    for i, producto in enumerate(productos_db):
        if producto.id == producto_id:
            productos_db[i] = updated_producto
            return updated_producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.delete("/productos/{producto_id}")
async def delete_producto(producto_id: int):
    for i, producto in enumerate(productos_db):
        if producto.id == producto_id:
            del productos_db[i]
            return {"detail": "Producto deleted"}
    raise HTTPException(status_code=404, detail="Producto not found")
