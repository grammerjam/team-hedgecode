from typing import List

from schemas.entertainment import EntertainmentMedia, EntertainmentCollection

"""
This function works by taking in an enterainment_media structured like the example in the EntertainmentMedia model.

What happens is we the media object we're trying to insert, and we dump the model (basically taking the schema and dumping it), however we exclude ID.

From the insertion, we're provided and inserted_id, we test for existence of the inserted ID, and then we look for it in the collection to return that document.

Before returning the document, since this function says we'll be returning an EntertainmentMedia, so we copy the values from our retrieved document and make it an EntertainmentMedia to return.


"""
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

"""
This function works by looking for Entertainment that have the categories of "Movie".

We then receive a cursor object from Motor, which we need to assign a length, 100 has been used as a starting point.

From there, we just append each document to the movie list and return the movie list.

"""
async def get_all_movies(db) -> EntertainmentCollection:
    movie_list = []
    cursor = db.entertainment.find({"category": "Movie"})
    for document in await cursor.to_list(length=100):
        movie_list.append(EntertainmentMedia(**document))
    return movie_list


        
