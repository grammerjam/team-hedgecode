from pydantic import BaseModel, Field, BeforeValidator, ConfigDict
# from typing_extensions import Annotated, Optional
from typing import List, Optional, Annotated


class TrendingThumbnails(BaseModel):
    """
    Container for the TRENDING thumbnail URLs.
    """
    model_config = ConfigDict(from_attributes=True)
    
    # Basic fields
    small: str = Field(description="The URL to the SMALL trending photo.")
    large: str = Field(description="The URL to the LARGE trending photo.")

class RegularThumbnails(BaseModel):
    """
    Container for the REGULAR thumbnail URLs.
    """
    model_config = ConfigDict(from_attributes=True)

    # Basic fields
    small: str = Field(description="The URL to the SMALL regular photo.")
    medium: str = Field(description="The URL to the MEDIUM regular photo.")
    large: str = Field(description="The URL to the LARGE regular photo.")


class Thumbnail(BaseModel):
    """
    Container for the Thumbnail URLs.
    """
    model_config = ConfigDict(from_attributes=True)

    # Declare the trending and regular as RegularThumbnails and TrendingThumbnails items
    regular: RegularThumbnails
    # can be empty
    trending: Optional[TrendingThumbnails] = None
    

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class EntertainmentPublicSettings(BaseModel):
    """
    Container for the relationships between the entertainment piece and it's trending attribute. One could put more here, but matching the data.json

    This is prone to change, so it's separated from the entertainment piece.
    """

    model_config = ConfigDict(from_attributes=True)

    # Basic fields
    isTrending: bool = Field(default= False,description="Whether the entertainment media is trending or not")


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

    public_entertainment_settings: EntertainmentPublicSettings = Field(description="Is the entertainment piece trending?")

    model_config = ConfigDict(
        populate_by_name = True,
        json_schema_extra = {
            "example": {
                "title": "Beyond Earth",
                "thumbnail": {
                    "trending": {
                                    "small": "./assets/thumbnails/beyond-earth/trending/small.jpg",
                                    "large": "./assets/thumbnails/beyond-earth/trending/large.jpg"
                                },
                    "regular": {
                                    "small": "./assets/thumbnails/beyond-earth/regular/small.jpg",
                                    "medium": "./assets/thumbnails/beyond-earth/regular/medium.jpg",
                                    "large": "./assets/thumbnails/beyond-earth/regular/large.jpg"
                                }
                },
               "year": 2019,
                "category": "Movie",
                "rating": "PG",
                "public_entertainment_settings": { 'isTrending' : True }
            }
        }
        )

        


class EntertainmentCollection(BaseModel):
    """
    A container holding a list of `EntertainmentMedia` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    movies: List[EntertainmentMedia]