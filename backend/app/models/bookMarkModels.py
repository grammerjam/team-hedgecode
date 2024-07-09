from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import List, Dict

# Define the Bookmark Pydantic model
class Bookmark(BaseModel):
    user_id: str
    media_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    position: int

    # Validator to ensure position is non-negative
    @validator('position')
    def validate_position(cls, value):
        if value < 0:
            raise ValueError('position must be non-negative')
        return value

# In-memory store for bookmarks
bookmark_store: Dict[str, List[Bookmark]] = {}

# Function to add a bookmark
def add_bookmark(bookmark_data: Bookmark):
    if bookmark_data.user_id not in bookmark_store:
        bookmark_store[bookmark_data.user_id] = []
    bookmark_store[bookmark_data.user_id].append(bookmark_data)
    return "Bookmark added successfully."

# Function to retrieve bookmarks for a user
def get_bookmarks(user_id: str) -> List[Bookmark]:
    return bookmark_store.get(user_id, [])

# Function to delete a bookmark
def delete_bookmark(user_id: str, media_id: str):
    if user_id in bookmark_store:
        bookmark_store[user_id] = [
            bookmark for bookmark in bookmark_store[user_id] 
            if bookmark.media_id != media_id
        ]
        return "Bookmark deleted successfully."
    return "Bookmark not found."

