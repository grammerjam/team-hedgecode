from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: str = Field(..., description="Unique identifier for the user")
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., min_length=3, max_length=50, description="User's chosen username")
    password_hash: str = Field(..., description="Hashed password")
    full_name: Optional[str] = Field(None, description="User's full name")
    is_active: bool = Field(default=True, description="Whether the user account is active")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of account creation")
    last_login: Optional[datetime] = Field(None, description="Timestamp of last login")
    watch_history: List[str] = Field(default_factory=list, description="List of IDs of watched content")
    bookmark: List[str] = Field(default_factory=list, description="List of IDs of content in bookmarks")

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "user123",
                "email": "user@example.com",
                "username": "netflixfan",
                "password_hash": "hashed_password_here",
                "full_name": "John Doe",
                "is_active": True,
                "created_at": "2023-01-01T00:00:00",
                "last_login": "2023-07-16T12:30:00",
                "watch_history": ["movie123", "series456"],
                "bookmark": ["movie789", "series101"]
            }
        }