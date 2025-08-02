from fastapi import FastAPI, HTTPException, Depends
from typing import List
from app.database import get_database, add_product, get_all_products
from app.models import ProductCreate, ProductRead

app = FastAPI()

@app.post("/products", response_model=ProductRead)
async def create_product(product: ProductCreate, db = Depends(get_database)):
    # This handler is pre-wired: call your async add_product logic here
    return await add_product(db, product)

@app.get("/products", response_model=List[ProductRead])
async def list_products(db = Depends(get_database)):
    # This handler is pre-wired: call your async get_all_products logic here
    return await get_all_products(db)
