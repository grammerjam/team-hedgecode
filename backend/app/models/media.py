from pydantic import BaseModel, BeforeValidator, ConfigDict, Field
from typing import Annotated


# Custom PyObjectId to handle MongoDB's ObjectId, represents str for JSON serialization.
PyObjectId = Annotated[str, BeforeValidator(str)]

class Thumbnail(BaseModel):
    """
    Container for Thumbnail URLs.
    """
    small: str = Field(description="The URL to the small thumbnail")
    medium: str = Field(description="The URL to the medium thumbnail")
    large: str = Field(description="The URL to the large thumbnail")

class Media(BaseModel):
    """
    Container for Media.
    """
    id: PyObjectId = Field(..., default_factory=PyObjectId, description="Unique ID of the media", alias="_id")
    title: str = Field(..., description="Media title")
    thumbnail: Thumbnail = Field(description="The collection of thumbnails of the media")
    release_year: int = Field(..., description="The year media was released", gt=1800, lt=2100)
    category: str = Field(..., description="Media category: either Movie or TV Series")
    rating: str = Field(description="Media rating")
    url: str = Field(description="The URL to the media file")
    is_trending: bool = Field(False, description="Whether media is trending or not")

    model_config = ConfigDict(
        populate_by_name = True,
        json_schema_extra = {
            "example": {
                "id": "66988b6079f9be39362748b4",
                "title": "Beyond Earth",
                "thumbnail": {
                    "small": "./assets/thumbnails/beyond-earth/regular/small.jpg",
                    "medium": "./assets/thumbnails/beyond-earth/regular/medium.jpg",
                    "large": "./assets/thumbnails/beyond-earth/regular/large.jpg"
                },
                "release_year": 2019,
                "category": "Movie",
                "rating": "PG",
                "url": "http://example.com/media/beyond-earth",
                "is_trending": True
            }
        }
    )
