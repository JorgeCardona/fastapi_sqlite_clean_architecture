from typing import List
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from configuration.fastapi.fast_api_configuration import clean_architecture
from configuration.database.db_config import get_session
from domain.entities.schemas.schema_product import ProductComplete as complete_schema
from domain.entities.schemas.schema_product import ProductPatch as patch_schema
from usescases.usecase_product import ProductUseCases as useCase

# https://github.com/JorgeCardona/AI/blob/master/URL%20Challenge/BACK%20FastAPI/database/models/Entity.py
# https://github.com/JorgeCardona/AI/blob/master/URL%20Challenge/BACK%20FastAPI/database/schemas/all_schemas.py
# https://github.com/JorgeCardona/AI/blob/master/URL%20Challenge/BACK%20FastAPI/main.py
# https://github.com/JorgeCardona/AI/blob/master/URL%20Challenge/BACK%20FastAPI/database/crud/services.py

class ProductServices:
        
    @clean_architecture.get("/")
    def Product_List(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
        return useCase().getObjectList(session=session, offset=offset, limit=limit)

    @clean_architecture.get("/{id}")
    def Product(id:int, session: Session = Depends(get_session)):
        return useCase().getObject(id=id, session=session)

    @clean_architecture.post("/", status_code=status.HTTP_201_CREATED)
    def Single_Product(entity:complete_schema, session: Session = Depends(get_session)):
        return useCase().addObject(entity=entity, session=session)

    @clean_architecture.post("/all", status_code=status.HTTP_201_CREATED)
    def Insert_Multiples_Product(entity:List[complete_schema], session: Session = Depends(get_session)):
        return useCase().addObjectList(entity=entity, session=session)
    
    @clean_architecture.put("/{id}")
    def Complete_Product(id:int, entity:complete_schema, session: Session = Depends(get_session)):
        return useCase().updateObject(id=id, entity=entity, session=session)

    @clean_architecture.patch("/{id}")
    def Partial_Product(id:int, entity:patch_schema, session: Session = Depends(get_session)):
        return useCase().patchObject(id=id, entity=entity, session=session)
    
    # status_code=status.HTTP_204_NO_CONTENT, genera excepcion porque retorna mensaje
    @clean_architecture.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
    def Remove_Product(id:int, session: Session = Depends(get_session)):
        return useCase().deleteObject(id=id, session=session)