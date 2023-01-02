from fastapi import status
from configuration.fastapi.fast_api_configuration import clean_architecture

from usecases.usecase_users import UsersUseCases as useCase
from usecases.usecase_users import Session, get_session, Depends, List
from usecases.usecase_users import complete_schema, patch_schema

from configuration.end_points.users import BASE_PATH, UPDATE_OBJECT, PATCH_OBJECT, REMOVE_OBJECT
from configuration.end_points.users import SEARCH_ALL_OBJECTS, SEARCH_SPECIFIC_OBJECT, ADD_NEW_OBJECT, ADD_NEW_OBJECT_LIST

class UsersServices:

    # retorna UNA LISTA DE OBJETOS con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso TODOS LOS CAMPOS
    @clean_architecture.get(BASE_PATH + "/", response_model=List[complete_schema], name=SEARCH_ALL_OBJECTS)
    def get_object_list(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
        """
        DESCRIPTION \\
        this service allows to RECOVERY A LIST of records from database
        """
        return useCase().get_object_list(session=session, offset=offset, limit=limit)

    # retorna UN OBJETO con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso todos los campos EXCEPTO EL CAMPO ID
    @clean_architecture.get(BASE_PATH + "/{id}",response_model=patch_schema, name=SEARCH_SPECIFIC_OBJECT, tags=['users'])
    def get_object(id:int, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to RECOVERY specific the record from database
        """
        return useCase().get_object(id=id, session=session)

    @clean_architecture.post(BASE_PATH + "/", name=ADD_NEW_OBJECT, status_code=status.HTTP_201_CREATED, tags=['users'])
    def add_object(entity:complete_schema, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to CREATE a new the record of database
        """
        return useCase().add_object(entity=entity, session=session)

    @clean_architecture.post(BASE_PATH + "/all", name=ADD_NEW_OBJECT_LIST, status_code=status.HTTP_201_CREATED, tags=['users'])
    def add_object_list(entity:List[complete_schema], session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to CREATE a LIST of new the record of database
        """
        return useCase().add_object_list(entity=entity, session=session)
    
    @clean_architecture.put(BASE_PATH + "/{id}", name=UPDATE_OBJECT, tags=['users'])
    def update_object(id:int, entity:complete_schema, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to UPDATE the record of database
        """
        return useCase().update_object(id=id, entity=entity, session=session)

    @clean_architecture.patch(BASE_PATH + "/{id}", name=PATCH_OBJECT, tags=['users'])
    def patch_object(id:int, entity:patch_schema, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to PATCH the record of database
        """
        return useCase().patch_object(id=id, entity=entity, session=session)
    
    # status_code=status.HTTP_204_NO_CONTENT, genera excepcion porque retorna mensaje
    @clean_architecture.delete(BASE_PATH + "/{id}", status_code=status.HTTP_204_NO_CONTENT, name=REMOVE_OBJECT, tags=['users'])
    def delete_object(id:int, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to REMOVE the record of database
        """
        return useCase().delete_object(id=id, session=session)