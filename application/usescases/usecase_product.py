from typing import List
from fastapi import Depends
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from domain.interfaces.repositories.repository_product import ProductRepository as repository

from domain.entities.models.model_product import Product as model
from domain.entities.schemas.schema_product import ProductComplete as complete_schema
from domain.entities.schemas.schema_product import ProductPatch as patch_schema
from configuration.database.db_config import get_session
from configuration.log.logging import log_api

class ProductUseCases(repository):
     
    def get_object_list(self, session:Session = Depends(get_session), offset: int = 0, limit: int = 100):
       
        object_ = session.query(model).offset(offset).limit(limit).all()
        return object_
    
    def get_object(self, id:int, session:Session = Depends(get_session)):
        
        object_ = session.query(model).get(id)
        
        if object_:
            return object_ 
        else:
            message = "Resource not found"
            log_api.warning(message)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message
            )
            
    def add_object(self, entity:complete_schema, session:Session = Depends(get_session)):
        
        """_summary_
        entity.dict(exclude_unset=True) -> convierte la entidad en un diccionario
        model(**object_data) -> crea la instancia del objeto usando el diccionario con los 2 asteriscos previos, **object_data
        
        Returns:
            _type_: _description_
        """
        object_data = entity.dict(exclude_unset=True)
        object_ = model(**object_data)
        
        session.add(object_)
        session.commit()
        session.refresh(object_)
        return object_

    def add_object_list(self, entity:List[complete_schema], session:Session = Depends(get_session)):
        
        """_summary_
        entity.dict(exclude_unset=True) -> convierte la entidad en un diccionario
        model(**object_data) -> crea la instancia del objeto usando el diccionario con los 2 asteriscos previos, **object_data
        
        Returns:
            _type_: _description_
        """
        list_objects_ = []
        
        for entity_object in entity:
            object_data = entity_object.dict(exclude_unset=True)
            object_ = model(**object_data)
            list_objects_.append(object_)
        
        session.add_all(list_objects_)
        session.commit()
        session.refresh(object_)
        return list_objects_
    
    def __update_rows__(self, id:int, entity:object, session:Session = Depends(get_session)):
        """_summary_
        esta implementacion funciona tanto para UPDATE y PATCH dado que con el for declarado
        se garantiza que se actualicen solo los vlores enviados
        Args:
            id (int): _description_
            entity (complete_model): _description_
            session (Session, optional): _description_. Defaults to Depends(get_session).

        object_data = convierte el objeto ENTITY de entrada en un DICCIONARIO
        setattr =  ACTUALIZA los campos del OBJECT_ de la consulta a la base de datos con los valores de OBJECT_DATA
        Raises:
            HTTPException: _description_

        Returns:
            _type_: _description_
        """
        
        object_ = self.get_object(id=id, session=session)
        object_data = entity.dict(exclude_unset=True)
            
        for key, value in object_data.items():
            setattr(object_, key, value)
        session.add(object_)
        session.commit()
        session.refresh(object_)
        return object_
        
    def update_object(self, id:int, entity:complete_schema, session:Session = Depends(get_session)):

        return self.__update_rows__(id=id, entity=entity, session=session)
            
    def patch_object(self, id:int, entity:patch_schema, session:Session = Depends(get_session)):

        return self.__update_rows__(id=id, entity=entity, session=session)

    def delete_object(self, id:int, session:Session = Depends(get_session)):
        object_ = self.get_object(id=id, session=session)

        session.delete(object_)
        session.commit()
        session.close()
        #return 'object_ was deleted...'