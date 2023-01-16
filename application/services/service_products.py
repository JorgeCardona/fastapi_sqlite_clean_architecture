from fastapi import status
from configuration.rest.rest_api_configuration import clean_architecture

from usecases.usecase_products import ProductsUseCases as use_case
from usecases.usecase_products import Session, get_session, Depends, List
from usecases.usecase_products import get_schema, post_schema, put_schema, patch_schema

from configuration.end_points.products import SEARCH_ALL_OBJECTS, SEARCH_SPECIFIC_OBJECT, ADD_NEW_OBJECT, ADD_NEW_OBJECT_LIST
from configuration.end_points.products import BASE_PATH, UPDATE_OBJECT, PATCH_OBJECT, REMOVE_OBJECT

class ProductsServices:
    
    # retorna UNA LISTA DE OBJETOS con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso TODOS LOS CAMPOS
    @clean_architecture.get(BASE_PATH + "/", response_model=List[get_schema], name=SEARCH_ALL_OBJECTS)
    def get_object_list(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
        """
        DESCRIPTION \\
        this service allows to RECOVERY A LIST of records from database
        """
        return use_case().get_object_list(session=session, offset=offset, limit=limit)

    # retorna UN OBJETO con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso todos los campos EXCEPTO EL CAMPO ID
    @clean_architecture.get(BASE_PATH + "/{id}",response_model=get_schema, name=SEARCH_SPECIFIC_OBJECT, tags=['products'], 
    responses={
        404: {"model": get_schema, "description": "The item was not found"},
        200: {
            "description": "User requested by ID",
            "content": {
                "application/json": {
                    "example": {"id": "bar", "value": "The bar tenders"}
                }
            },
        },
    }
                            )
    def get_object(id:int, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to RECOVERY specific the record from database
        """
        return use_case().get_object(id=id, session=session)

    @clean_architecture.post(BASE_PATH + "/", name=ADD_NEW_OBJECT, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object(entity:post_schema, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to CREATE a new the record of database
        """
        return use_case().add_object(entity=entity, session=session)

    @clean_architecture.post(BASE_PATH + "/all", name=ADD_NEW_OBJECT_LIST, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object_list(entity:List[post_schema], session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to CREATE a LIST of new the record of database
        """
        return use_case().add_object_list(entity=entity, session=session)
    
    @clean_architecture.put(BASE_PATH + "/{id}", name=UPDATE_OBJECT, tags=['products'])
    def update_object(id:int, entity:put_schema, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to UPDATE the record of database
        """
        return use_case().update_object(id=id, entity=entity, session=session)

    @clean_architecture.patch(BASE_PATH + "/{id}", name=PATCH_OBJECT, tags=['products'])
    def patch_object(id:int, entity:patch_schema, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to PATCH the record of database
        """
        return use_case().patch_object(id=id, entity=entity, session=session)
    
    # status_code=status.HTTP_204_NO_CONTENT, genera excepcion porque retorna mensaje
    @clean_architecture.delete(BASE_PATH + "/{id}", status_code=status.HTTP_204_NO_CONTENT, name=REMOVE_OBJECT, tags=['products'])
    def delete_object(id:int, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to REMOVE the record of database
        """
        return use_case().delete_object(id=id, session=session)