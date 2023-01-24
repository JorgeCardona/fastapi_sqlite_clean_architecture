from fastapi import status
from configuration.rest.rest_api_configuration import clean_architecture

from usecases.usecase_products import ProductsUseCases as use_case
from usecases.usecase_products import Session, get_session, Depends, List
from usecases.usecase_products import get_schema, post_schema, put_schema, patch_schema

from configuration.end_points.products import SEARCH_ALL_OBJECTS, SEARCH_SPECIFIC_OBJECT, ADD_NEW_OBJECT, ADD_NEW_OBJECT_LIST
from configuration.end_points.products import BASE_PATH, UPDATE_OBJECT, PATCH_OBJECT, REMOVE_OBJECT

class ProductsServices:
            
    # retorna UNA LISTA DE OBJETOS con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso TODOS LOS CAMPOS
    @clean_architecture.get(BASE_PATH + "/", name=SEARCH_ALL_OBJECTS)
    def get_object_list(session: Session = Depends(get_session), offset: int = 0, limit: int = 100, page_number : int = 1, page_size : int = 10):
        """
        DESCRIPTION \\
        this service allows to RECOVERY A LIST of records from database
        """
        data = use_case().get_object_list(session=session, offset=offset, limit=limit)

        
        response = use_case().get_response_format(data, offset=offset, limit=limit, page_number=page_number, page_size=page_size)

        return response


    # retorna UN OBJETO con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso todos los campos EXCEPTO EL CAMPO ID
    @clean_architecture.get(BASE_PATH + "/{id}", name=SEARCH_SPECIFIC_OBJECT, tags=['products'], 
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
        
        data = use_case().get_object(id=id, session=session)

        response = use_case().get_response_format(data=data)
        return response
    
    @clean_architecture.post(BASE_PATH + "/", name=ADD_NEW_OBJECT, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object(entity:post_schema, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to CREATE a new the record of database
        """
        data = use_case().add_object(entity=entity, session=session)

        response = use_case().get_response_format(data=data)
        return response
    
    @clean_architecture.post(BASE_PATH + "/all", name=ADD_NEW_OBJECT_LIST, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object_list(entity:List[post_schema], session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to CREATE a LIST of new the record of database
        """
        data = use_case().add_object_list(entity=entity, session=session)

        response = use_case().get_response_format(data=data)
        return response
        
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
    @clean_architecture.delete(BASE_PATH + "/{id}",  name=REMOVE_OBJECT, tags=['products'])
    def delete_object(id:int, session: Session = Depends(get_session)):
        """
        DESCRIPTION \\
        this service allows to REMOVE the record of database
        """
        data = use_case().delete_object(id=id, session=session)
        print('dddddddddddddddddddddddddddd', data)

        response = use_case().get_response_format(data=data)
        
        print('responseeeeeeeeeee',response)
        
        from fastapi.responses import JSONResponse
        object_={}
        #response = JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=object_) if object_ else JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=object_)
        return response