from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Proveedor(BaseModel):
    id: int
    nombre: str
    contacto: str

proveedores_db = [
    Proveedor(id=1, nombre="Proveedor 1", contacto="contacto1@example.com"),
    Proveedor(id=2, nombre="Proveedor 2", contacto="contacto2@example.com"),
]

@router.get("/proveedores", response_model=List[Proveedor])
async def get_proveedores():
    return proveedores_db

@router.post("/proveedores", response_model=Proveedor)
async def create_proveedor(proveedor: Proveedor):
    proveedores_db.append(proveedor)
    return proveedor

@router.get("/proveedores/{proveedor_id}", response_model=Proveedor)
async def get_proveedor(proveedor_id: int):
    for proveedor in proveedores_db:
        if proveedor.id == proveedor_id:
            return proveedor
    raise HTTPException(status_code=404, detail="Proveedor not found")

@router.put("/proveedores/{proveedor_id}", response_model=Proveedor)
async def update_proveedor(proveedor_id: int, updated_proveedor: Proveedor):
    for i, proveedor in enumerate(proveedores_db):
        if proveedor.id == proveedor_id:
            proveedores_db[i] = updated_proveedor
            return updated_proveedor
    raise HTTPException(status_code=404, detail="Proveedor not found")

@router.delete("/proveedores/{proveedor_id}")
async def delete_proveedor(proveedor_id: int):
    for i, proveedor in enumerate(proveedores_db):
        if proveedor.id == proveedor_id:
            del proveedores_db[i]
            return {"detail": "Proveedor deleted"}
    raise HTTPException(status_code=404, detail="Proveedor not found")
