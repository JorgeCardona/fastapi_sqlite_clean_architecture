from pydantic import BaseModel
from typing import Optional
    
# schemas siempre se definen clave:valor
class ProductAdd(BaseModel):
    name:str
    price:int
    categorie:str
    
    class Config:
        orm_mode = True
        
class ProductSearch(ProductAdd):
    id:int      

class ProductUpdate(ProductAdd):
    pass
          
class ProductPatch(BaseModel):
    name:Optional[str]
    categorie:Optional[str]
    price:Optional[int]
    
    class Config:
        orm_mode = True