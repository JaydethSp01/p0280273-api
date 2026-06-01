from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import productos, categorias, stock, proveedores
import os

app = FastAPI()

origins = os.environ.get("CORS_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(productos.router)
app.include_router(categorias.router)
app.include_router(stock.router)
app.include_router(proveedores.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}