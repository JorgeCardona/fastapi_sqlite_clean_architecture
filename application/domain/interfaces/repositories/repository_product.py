from abc import ABC, abstractmethod
from fastapi import Depends
from sqlalchemy.orm import Session
from domain.entities.schemas.schema_product import ProductComplete as complete_schema
from domain.entities.schemas.schema_product import ProductPatch as patch_schema
from configuration.database.db_config import get_session

class ProductRepository(ABC):

    @abstractmethod
    def getObjectList(self, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def getObject(self, id:int, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def addObject(self, entity:complete_schema, session:Session = Depends(get_session)):
        pass
    
    @abstractmethod
    def updateObject(self, id:int, entity:complete_schema, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def patchObject(self, id:int, entity:patch_schema, session:Session = Depends(get_session)):
        pass
    
    @abstractmethod
    def deleteObject(self, id:int, session:Session = Depends(get_session)):
        pass