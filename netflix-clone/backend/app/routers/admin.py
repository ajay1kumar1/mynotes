from fastapi import APIRouter, HTTPException, Depends
from ..database import db
from ..models import ContentCreate, ContentInDB
from ..dependencies import get_current_admin
from bson import ObjectId

router = APIRouter(dependencies=[Depends(get_current_admin)])

@router.post("/movies")
async def create_movie(movie_in: ContentCreate):
    movie_dict = movie_in.dict()
    result = await db.movies.insert_one(movie_dict)
    return {"id": str(result.inserted_id), "message": "Movie added"}

@router.put("/movies/{movie_id}")
async def update_movie(movie_id: str, movie_in: ContentCreate):
    if not ObjectId.is_valid(movie_id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    movie_dict = movie_in.dict()
    result = await db.movies.update_one({"_id": ObjectId(movie_id)}, {"$set": movie_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie updated"}

@router.delete("/movies/{movie_id}")
async def delete_movie(movie_id: str):
    if not ObjectId.is_valid(movie_id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await db.movies.delete_one({"_id": ObjectId(movie_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted"}

@router.get("/users")
async def get_all_users():
    users = []
    async for user in db.users.find():
        user["_id"] = str(user["_id"])
        del user["hashed_password"]
        users.append(user)
    return users
