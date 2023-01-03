from pydantic import BaseModel
from typing import Optional
    
# schemas siempre se definen clave:valor
class ProductFull(BaseModel):
    id:int
    name:str
    price:int
    categorie:str
    class Config:
        orm_mode = True
        
class ProductComplete(BaseModel):
    name:str
    price:int
    categorie:str
    class Config:
        orm_mode = True
    
class ProductPatch(BaseModel):
    name:Optional[str]
    categorie:Optional[str]
    price:Optional[int]
    class Config:
        orm_mode = True