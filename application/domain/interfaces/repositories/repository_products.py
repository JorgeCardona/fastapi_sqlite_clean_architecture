from abc import ABC, abstractmethod
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from configuration.database.db_config import get_session
from domain.entities.models.model_products  import Product as model
from domain.entities.schemas.schema_products import ProductSearch as get_schema
from domain.entities.schemas.schema_products import ProductAdd as post_schema
from domain.entities.schemas.schema_products import ProductUpdate as put_schema
from domain.entities.schemas.schema_products import ProductPatch as patch_schema

class ProductRepository(ABC):

    @abstractmethod
    def get_object_list(self, session:Session = Depends(get_session), offset: int = 0, limit: int = 100):
        pass

    @abstractmethod
    def get_object(self, id:int, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def add_object(self, entity:post_schema, session:Session = Depends(get_session)):
        pass
 
    @abstractmethod
    def add_object_list(self, entity:List[post_schema], session:Session = Depends(get_session)):
         pass
    
    @abstractmethod
    def __update_rows__(self, id:int, entity:object, session:Session = Depends(get_session)):    
        pass
       
    @abstractmethod
    def update_object(self, id:int, entity:put_schema, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def patch_object(self, id:int, entity:patch_schema, session:Session = Depends(get_session)):
        pass
    
    @abstractmethod
    def delete_object(self, id:int, session:Session = Depends(get_session)):
        pass