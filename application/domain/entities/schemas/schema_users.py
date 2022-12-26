from pydantic import BaseModel
from typing import Optional

class UsersComplete(BaseModel):

    email:str
    hashed_password:str
    is_active:bool
    
    class Config:
        orm_mode = True
    #items = relationship("Product", back_populates="owner")
      
class UsersPatch(BaseModel):
    
    email:Optional[str]
    hashed_password:Optional[str]
    is_active:Optional[bool]
    
    class Config:
        orm_mode = True