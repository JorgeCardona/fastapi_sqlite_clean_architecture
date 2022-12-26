from abc import ABC, abstractmethod
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from configuration.database.db_config import get_session
from domain.entities.schemas.schema_users import UsersComplete as complete_schema
from domain.entities.schemas.schema_users import UsersPatch as patch_schema

class UsersRepository(ABC):

    @abstractmethod
    def get_object_list(self, session:Session = Depends(get_session), offset: int = 0, limit: int = 100):
        pass

    @abstractmethod
    def get_object(self, id:int, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def add_object(self, entity:complete_schema, session:Session = Depends(get_session)):
        pass
 
    @abstractmethod
    def add_object_list(self, entity:List[complete_schema], session:Session = Depends(get_session)):
         pass
    
    @abstractmethod
    def __update_rows__(self, id:int, entity:object, session:Session = Depends(get_session)):    
        pass
       
    @abstractmethod
    def update_object(self, id:int, entity:complete_schema, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def patch_object(self, id:int, entity:patch_schema, session:Session = Depends(get_session)):
        pass
    
    @abstractmethod
    def delete_object(self, id:int, session:Session = Depends(get_session)):
        pass