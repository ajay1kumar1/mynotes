from fastapi import APIRouter, HTTPException
from ..database import db
from ..models import ContentCreate, ContentInDB
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_movies():
    movies = []
    async for movie in db.movies.find():
        movie["_id"] = str(movie["_id"])
        movies.append(movie)
    return movies

@router.get("/{movie_id}")
async def get_movie(movie_id: str):
    if not ObjectId.is_valid(movie_id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    movie = await db.movies.find_one({"_id": ObjectId(movie_id)})
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    movie["_id"] = str(movie["_id"])
    return movie
