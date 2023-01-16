    
from fastapi import status
from configuration.fastapi.fast_api_configuration import clean_architecture

from usecases.balon_usecase import BalonUseCases as useCase
from usecases.balon_usecase import Session, get_session, Depends, List
from usecases.balon_usecase import complete_schema, patch_schema

from configuration.end_points.products import SEARCH_ALL_OBJECTS, SEARCH_SPECIFIC_OBJECT, ADD_NEW_OBJECT, ADD_NEW_OBJECT_LIST
from configuration.end_points.products import BASE_PATH, UPDATE_OBJECT, PATCH_OBJECT, REMOVE_OBJECT

class BalonService:
    
    # retorna UNA LISTA DE OBJETOS con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso TODOS LOS CAMPOS
    @clean_architecture.get(BASE_PATH + "/", response_model=List[complete_schema], name=SEARCH_ALL_OBJECTS)
    def get_object_list(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
        return useCase().get_object_list(session=session, offset=offset, limit=limit)

    # retorna UN OBJETO con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso todos los campos EXCEPTO EL CAMPO ID
    @clean_architecture.get(BASE_PATH + "/<built-in function id>",response_model=patch_schema, name=SEARCH_SPECIFIC_OBJECT, tags=['products'])
    def get_object(id:int, session: Session = Depends(get_session)):
        return useCase().get_object(id=id, session=session)

    @clean_architecture.post(BASE_PATH + "/", name=ADD_NEW_OBJECT, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object(entity:complete_schema, session: Session = Depends(get_session)):
        return useCase().add_object(entity=entity, session=session)

    @clean_architecture.post(BASE_PATH + "/all", name=ADD_NEW_OBJECT_LIST, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object_list(entity:List[complete_schema], session: Session = Depends(get_session)):
        return useCase().add_object_list(entity=entity, session=session)
    
    @clean_architecture.put(BASE_PATH + "/<built-in function id>", name=UPDATE_OBJECT, tags=['products'])
    def update_object(id:int, entity:complete_schema, session: Session = Depends(get_session)):
        return useCase().update_object(id=id, entity=entity, session=session)

    @clean_architecture.patch(BASE_PATH + "/<built-in function id>", name=PATCH_OBJECT, tags=['products'])
    def patch_object(id:int, entity:patch_schema, session: Session = Depends(get_session)):
        return useCase().patch_object(id=id, entity=entity, session=session)
    
    # status_code=status.HTTP_204_NO_CONTENT, genera excepcion porque retorna mensaje
    @clean_architecture.delete(BASE_PATH + "/<built-in function id>", status_code=status.HTTP_204_NO_CONTENT, name=REMOVE_OBJECT, tags=['products'])
    def delete_object(id:int, session: Session = Depends(get_session)):
        return useCase().delete_object(id=id, session=session)
    