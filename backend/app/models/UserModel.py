from pydantic import BaseModel, Field, EmailStr, ConfigDict, SecretStr, PyObjectId, Optional, List


class User(BaseModel):
    
    # __tablename__ = "users"

    # # Columns
    # id = Column(Integer, primary_key = True)
    # first_name = Column(String)
    # last_name = Column(String)
    # email = Column(String)

    # _password_hash = Column(String, nullable=False)

    # # Foreign Keys

    # # Relationships
    # bookmarks = relationship("Bookmark", back_populates="user")

    id : Optional[PyObjectId] = Field(default=None, alias="_id")
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password_hash: SecretStr = Field(...)
    
    bookmarks: List[Bookmark] = Field(default_factory=list)
    
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
