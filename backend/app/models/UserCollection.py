from pydantic import BaseModel, List
from UserModel import User
class UserCollection(BaseModel):
    students: List[User]