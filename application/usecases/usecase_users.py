from fastapi import HTTPException, status
from domain.interfaces.repositories.repository_users import UsersRepository as repository
from domain.interfaces.repositories.repository_users import Session, get_session, Depends, List
from domain.interfaces.repositories.repository_users import complete_schema, patch_schema
from domain.entities.models.model_users import User as model
from configuration.log.logging import log_api

class UsersUseCases(repository):
     
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
        object_data = entity.dict(exclude_unset=True)
        object_ = model(**object_data)
        
        session.add(object_)
        session.commit()
        session.refresh(object_)
        return object_

    def add_object_list(self, entity:List[complete_schema], session:Session = Depends(get_session)):        
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