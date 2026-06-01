from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str

class Categoria(BaseModel):
    id: int
    nombre: str

class Stock(BaseModel):
    id: int
    producto_id: int
    cantidad: int

class Proveedor(BaseModel):
    id: int
    nombre: str