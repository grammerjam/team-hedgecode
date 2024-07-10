from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from starlette.responses import RedirectResponse
from motor.motor_asyncio import AsyncIOMotorClient

from schemas import entertainment
from contextlib import asynccontextmanager
from database import *

import uvicorn

app = FastAPI(
    title = settings.APP_NAME,
    version = settings.VERSION
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Establish the database connection
    global db_client
    db_client = await settings.initiate_database()
    yield
    # Close the database connection
    if db_client:
        db_client.close()

app = FastAPI(lifespan=lifespan)

async def get_database():
    if db_client is None:
        raise RuntimeError("Database client not initialized")
    return db_client[settings.DB_NAME]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Redirect / -> Swagger-UI documentation
@app.get("/")
async def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")


@app.post("/entertainment/media/")
async def create_entertainment_media(entertainment_media: entertainment.EntertainmentMedia) -> EntertainmentMedia:
    db = await get_database()
    if db is not None:
        new_entertainment_media = await add_entertainment_media(entertainment_media, db)
    else:
        raise HTTPException(status_code=500, detail="Database connection failed")

    if new_entertainment_media:
       return new_entertainment_media
    else:
        raise HTTPException(status_code=500, detail="Failed to create item")

@app.get("/movies")
async def all_movies() -> EntertainmentCollection:
    db = await get_database()
    if db is not None:
        all_movies = await get_all_movies(db)
    else:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    if all_movies is not None:
        return EntertainmentCollection(movies=all_movies)
    else:
        raise HTTPException(status_code=404, detail="Failed to find movies")



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
