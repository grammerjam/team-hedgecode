from pydantic import BaseModel, Field, BeforeValidator, ConfigDict
# from typing_extensions import Annotated, Optional
from typing import List, Optional, Annotated


class Thumbnail(BaseModel):
    """
    Container for the Thumbnail URLs.
    """
    model_config = ConfigDict(from_attributes=True)

    size: str = Field(description="The size of the thumbnail. Small, Medium, Large.")
    url: str = Field(description="The thumbnail URL.")
    category: str = Field(description="The category of the thumbnail. Regular or Trending?")


# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class EntertainmentMedia(BaseModel):
    """
    Container for the piece of Entertainment, name is prone to change.
    """
    # The primary key for the EntertainmentMedia, stored as a `str` on the instance.
    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    id: Optional[PyObjectId] = Field(alias='_id', default=None)

    # Basic fields
    title: str = Field(description="The entertainment medias title.")
    thumbnail: Thumbnail = Field(description="The collection of URLs this media holds, categorized by regular and trending.")
    year: int = Field(description="The year this entertainment piece was released.")
    category: str = Field(description="Whether the entertainment piece is a MOVIE or TELEVISION SERIES.")

    url: str = Field(description="The URL of the entertainment media.")
    rating: str = Field(description="The entertainments rating")
    isTrending: bool = Field(default= False,description="Whether the entertainment media is trending or not")
    regular_thumbnail: List[Thumbnail]
    trending_thumbnail: Optional[List[Thumbnail]] = None
    

    model_config = ConfigDict(
        populate_by_name = True,
        json_schema_extra = {
            "example": {
            "title": "Beyond Earth",
            "trending_thumbnail": {
                            "small": "./assets/thumbnails/beyond-earth/trending/small.jpg",
                            "large": "./assets/thumbnails/beyond-earth/trending/large.jpg"
                        },
            "regular_thumbnail": {
                            "small": "./assets/thumbnails/beyond-earth/regular/small.jpg",
                            "medium": "./assets/thumbnails/beyond-earth/regular/medium.jpg",
                            "large": "./assets/thumbnails/beyond-earth/regular/large.jpg"
            },
            "year": 2019,
            "category": "Movie",
            "rating": "PG",
            'isTrending' : True 
            }
        }
        )

        


class EntertainmentCollection(BaseModel):
    """
    A container holding a list of `EntertainmentMedia` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    movies: List[EntertainmentMedia]