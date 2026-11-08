from fastapi import APIRouter, HTTPException
from app.database import db
from app.models import Cake
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_cakes():
    cakes = []
    async for cake in db.cakes.find({"in_stock": True}):
        cake["_id"] = str(cake["_id"])
        cakes.append(cake)
    return cakes

@router.get("/{cake_id}")
async def get_cake(cake_id: str):
    if not ObjectId.is_valid(cake_id):
        raise HTTPException(status_code=400, detail="Invalid cake ID")
    cake = await db.cakes.find_one({"_id": ObjectId(cake_id)})
    if not cake:
        raise HTTPException(status_code=404, detail="Cake not found")
    cake["_id"] = str(cake["_id"])
    return cake

@router.post("/")
async def create_cake(cake: Cake):
    cake_dict = cake.dict(by_alias=True)
    result = await db.cakes.insert_one(cake_dict)
    return {"id": str(result.inserted_id), "message": "Cake created successfully"}

@router.delete("/{cake_id}")
async def delete_cake(cake_id: str):
    if not ObjectId.is_valid(cake_id):
        raise HTTPException(status_code=400, detail="Invalid cake ID")
    result = await db.cakes.delete_one({"_id": ObjectId(cake_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cake not found")
    return {"message": "Cake deleted successfully"}
