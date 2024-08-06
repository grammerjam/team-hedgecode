from typing import List

from schemas.entertainment import EntertainmentMedia, EntertainmentCollection

async def add_entertainment_media(entertainment_media: EntertainmentMedia, db) -> EntertainmentMedia:
    # Create new entertainment_media
    new_entertainment_media = await db.entertainment.insert_one(
        entertainment_media.model_dump(by_alias=True, exclude=["id"])
    )

    # if inserted_id to validate creation 
    if new_entertainment_media.inserted_id:
        # Fetch the inserted document, will return the ObjectId
        created_media = await db.entertainment.find_one({"_id": new_entertainment_media.inserted_id})
        # Populate EntertainmentMedia model with the created_media
        media_instance = EntertainmentMedia(**created_media)
        return media_instance
    else:
        raise ValueError('Failed to create new entertainment media')

async def get_all_movies(db) -> EntertainmentCollection:
    movie_list = []
    cursor = db.entertainment.find({"category": "Movie"})
    for document in await cursor.to_list(length=100):
        movie_list.append(EntertainmentMedia(**document))
    return movie_list


        
