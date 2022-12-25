from typing import List
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from configuration.fastapi.fast_api_configuration import clean_architecture
from configuration.database.db_config import get_session
from domain.entities.schemas.schema_product import ProductComplete as complete_schema
from domain.entities.schemas.schema_product import ProductPatch as patch_schema
from usescases.usecase_product import ProductUseCases as useCase
from configuration.end_points.product import SEARCH_ALL_PRODUCTS, SEARCH_SPECIFIC_PRODUCT, ADD_NEW_PRODUCT, ADD_NEW_PRODUCT_LIST
from configuration.end_points.product import UPDATE_PRODUCT, PATCH_PRODUCT, REMOVE_PRODUCT
# https://github.com/JorgeCardona/AI/blob/master/URL%20Challenge/BACK%20FastAPI/database/models/Entity.py
# https://github.com/JorgeCardona/AI/blob/master/URL%20Challenge/BACK%20FastAPI/database/schemas/all_schemas.py
# https://github.com/JorgeCardona/AI/blob/master/URL%20Challenge/BACK%20FastAPI/main.py
# https://github.com/JorgeCardona/AI/blob/master/URL%20Challenge/BACK%20FastAPI/database/crud/services.py

class ProductServices:

    # retorna UNA LISTA DE OBJETOS con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso TODOS LOS CAMPOS
    @clean_architecture.get("/", response_model=List[complete_schema], name=SEARCH_ALL_PRODUCTS, tags=['products'])
    def get_object_list(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
        return useCase().get_object_list(session=session, offset=offset, limit=limit)

    # retorna UN OBJETO con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso todos los campos EXCEPTO EL CAMPO ID
    @clean_architecture.get("/{id}",response_model=patch_schema, name=SEARCH_SPECIFIC_PRODUCT, tags=['products'])
    def get_object(id:int, session: Session = Depends(get_session)):
        return useCase().get_object(id=id, session=session)

    @clean_architecture.post("/", name=ADD_NEW_PRODUCT, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object(entity:complete_schema, session: Session = Depends(get_session)):
        return useCase().add_object(entity=entity, session=session)

    @clean_architecture.post("/all", name=ADD_NEW_PRODUCT_LIST, status_code=status.HTTP_201_CREATED, tags=['items'])
    def add_object_list(entity:List[complete_schema], session: Session = Depends(get_session)):
        return useCase().add_object_list(entity=entity, session=session)
    
    @clean_architecture.put("/{id}", name=UPDATE_PRODUCT )
    def update_object(id:int, entity:complete_schema, session: Session = Depends(get_session)):
        return useCase().update_object(id=id, entity=entity, session=session)

    @clean_architecture.patch("/{id}", include_in_schema=False)
    def patch_object(id:int, entity:patch_schema, session: Session = Depends(get_session)):
        return useCase().patch_object(id=id, entity=entity, session=session)
    
    # status_code=status.HTTP_204_NO_CONTENT, genera excepcion porque retorna mensaje
    @clean_architecture.delete("/{id}", name=REMOVE_PRODUCT, status_code=status.HTTP_204_NO_CONTENT, tags=['items'])
    def delete_object(id:int, session: Session = Depends(get_session)):
        return useCase().delete_object(id=id, session=session)