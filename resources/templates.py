def rest_template(name:str):
    content = f"""
    """ 
    return content

def graphql_template(name:str):
    content = f"""
    """ 
    return content

def cors_template(name:str):
    content = f"""
    """ 
    return content
    
def utils_template(name:str):
    content = f"""
    """ 
    return content

def environment_template(name:str):
    content = f"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Environment:
    
    # es usada por la funcion get_sessioncon la variable de instancia self.Base
    Base =  declarative_base()
         
    def __init__(self, environment:str) -> None:
        self.engine = self.select_environment(environment)
        self.session_local = sessionmaker(bind=self.engine, expire_on_commit=False)
        # since the function returns nothing then you don't need parentheses when assigning the variable to a function
        self.get_sessiones = self.get_session
        
     
    def select_environment(self, environment:str) -> None:
        
        if environment == 'dev':
            return self.get_engine_dev()
            
        else:
            return self.get_engine()
    

    def create_engine(self, SQLALCHEMY_DATABASE_URL:str):

        #Creates database engine
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL,

            echo =True,
            pool_recycle=3600
        )
        
        return engine
               
    def get_engine_dev(self):
        
        #Define database values
        DATABASE_NAME = 'clean_architecture.db'
        DIRECTORY_SAVE_SQLITE_DATABASE = 'configuration/database/sqlite_test'
        SQLALCHEMY_DATABASE_URL = f"sqlite:///{'DIRECTORY_SAVE_SQLITE_DATABASE'}/{'DATABASE_NAME'}"

        return self.create_engine(SQLALCHEMY_DATABASE_URL)
"""  
    return content

def database_template(name:str):
    content = f"""
"""
    return content

def log_template(name:str):
    content = f"""
import logging as log_api
import os

ROOT_DIRECTORY = str(os.getcwd()).replace('\\','/')
LOG_FILE_NAME  = 'logging.log'
LOG_FOLDER = ROOT_DIRECTORY + '/log'
LOG_DIRECTORY = LOG_FOLDER  + '/' + LOG_FILE_NAME

format_log = '%(asctime)s | %(levelname)s | message = %(message)s | %(name)s | line %(lineno)d | package %(filename)s | %(funcName)s'
log_api.basicConfig(filename=LOG_DIRECTORY,
                    level=log_api.DEBUG,
                    format= format_log)
"""  
    return content

def end_points_template(name:str):
    
    end_point = name + 's'
    name_base = name.capitalize()
    content = f"""
BASE_PATH = '/{end_point}'
SEARCH_ALL_OBJECTS = 'Get {name_base} List'
SEARCH_SPECIFIC_OBJECT = 'Get {name_base}'
ADD_NEW_OBJECT = 'Add New {name_base}'
ADD_NEW_OBJECT_LIST = 'Add New {name_base} List'
REMOVE_OBJECT = 'Delete {name_base}'
UPDATE_OBJECT = 'Update {name_base}'
PATCH_OBJECT = 'Update {name_base} Partially'
"""  
    return content
 
def model_template(name:str):
    
    class_name = name.capitalize()
    table_name = name.lower() + 's'
    
    content = f"""
from sqlalchemy import Column, Integer, String
from configuration.environment.environment_configuration import Environment

class {class_name}(Environment.Base):
    __tablename__ = '{table_name}'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    categorie = Column(String(256))
    price = Column(Integer)
"""
    
    return content

def schema_template(name:str, complete='Complete', partial='Patch'):
    
    class_name = name.capitalize()
    class_name_complete =  class_name + complete
    class_name_partial  = class_name + partial
    
    content = f"""
from pydantic import BaseModel
from typing import Optional

class {class_name_complete}(BaseModel):
    id:int
    name:str
    price:int
    categorie:str
    
    class Config:
        orm_mode = True
        
class {class_name_partial}(BaseModel):
    name:Optional[str]
    categorie:Optional[str]
    price:Optional[int]
    
    class Config:
        orm_mode = True
""" 
    return content

def business_logic_template(name:str, complement='BusinessLogic'):
    
    class_name = name.capitalize()
    schema_name = name.lower()
    complete_class_name = class_name + complement
    content = f"""
from abc import ABC, abstractmethod

class {complete_class_name}(ABC):
    pass
    """ 
    return content
    
def repository_template(name:str, complement='Repository'):
    
    class_name = name.capitalize()
    schema_name = name.lower()
    complete_class_name = class_name + complement
    
    content = f"""
from abc import ABC, abstractmethod
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from configuration.database.db_configuration import get_session
from domain.entities.{schema_name}_entity.{schema_name}_model import {class_name} as model
from domain.entities.{schema_name}_entity.{schema_name}_schema import {class_name}Full as complete_schema
from domain.entities.{schema_name}_entity.{schema_name}_schema import {class_name}Patch as patch_schema


class {complete_class_name}(ABC):
    
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
"""
    return content

def usecase_template(name:str, complement='UseCase'):
    
    class_name = name.capitalize()
    schema_name = name.lower()
    complete_class_name = class_name + complement
    content = f"""
from fastapi import HTTPException, status

from domain.interfaces.repositories.{schema_name}_repository import {class_name}Repository as repository
from domain.interfaces.repositories.{schema_name}_repository import Session, get_session, Depends, List
from domain.interfaces.repositories.{schema_name}_repository import model, complete_schema, patch_schema
from configuration.log.logging import log_api

class {complete_class_name}(repository):
     
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
    """ 
    return content
        
 
def service_template(name:str, complement='Service'):
    
    class_name = name.capitalize()
    schema_name = name.lower()
    complete_class_name = class_name + complement
    content = f"""    
from fastapi import status
from configuration.fastapi.fast_api_configuration import clean_architecture

from usecases.{schema_name}_usecase import {class_name}UseCases as useCase
from usecases.{schema_name}_usecase import Session, get_session, Depends, List
from usecases.{schema_name}_usecase import complete_schema, patch_schema

from configuration.end_points.products import SEARCH_ALL_OBJECTS, SEARCH_SPECIFIC_OBJECT, ADD_NEW_OBJECT, ADD_NEW_OBJECT_LIST
from configuration.end_points.products import BASE_PATH, UPDATE_OBJECT, PATCH_OBJECT, REMOVE_OBJECT

class {complete_class_name}:
    
    # retorna UNA LISTA DE OBJETOS con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso TODOS LOS CAMPOS
    @clean_architecture.get(BASE_PATH + "/", response_model=List[complete_schema], name=SEARCH_ALL_OBJECTS)
    def get_object_list(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
        return useCase().get_object_list(session=session, offset=offset, limit=limit)

    # retorna UN OBJETO con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso todos los campos EXCEPTO EL CAMPO ID
    @clean_architecture.get(BASE_PATH + "/{id}",response_model=patch_schema, name=SEARCH_SPECIFIC_OBJECT, tags=['products'])
    def get_object(id:int, session: Session = Depends(get_session)):
        return useCase().get_object(id=id, session=session)

    @clean_architecture.post(BASE_PATH + "/", name=ADD_NEW_OBJECT, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object(entity:complete_schema, session: Session = Depends(get_session)):
        return useCase().add_object(entity=entity, session=session)

    @clean_architecture.post(BASE_PATH + "/all", name=ADD_NEW_OBJECT_LIST, status_code=status.HTTP_201_CREATED, tags=['products'])
    def add_object_list(entity:List[complete_schema], session: Session = Depends(get_session)):
        return useCase().add_object_list(entity=entity, session=session)
    
    @clean_architecture.put(BASE_PATH + "/{id}", name=UPDATE_OBJECT, tags=['products'])
    def update_object(id:int, entity:complete_schema, session: Session = Depends(get_session)):
        return useCase().update_object(id=id, entity=entity, session=session)

    @clean_architecture.patch(BASE_PATH + "/{id}", name=PATCH_OBJECT, tags=['products'])
    def patch_object(id:int, entity:patch_schema, session: Session = Depends(get_session)):
        return useCase().patch_object(id=id, entity=entity, session=session)
    
    # status_code=status.HTTP_204_NO_CONTENT, genera excepcion porque retorna mensaje
    @clean_architecture.delete(BASE_PATH + "/{id}", status_code=status.HTTP_204_NO_CONTENT, name=REMOVE_OBJECT, tags=['products'])
    def delete_object(id:int, session: Session = Depends(get_session)):
        return useCase().delete_object(id=id, session=session)
    """
    return content
          
def create_file(file, template):
    
    with open(file,'w') as escribir:
        escribir.write(template)
    #print(template)
    
template = model_template(name='REST')
template = schema_template(name='REST')
template = repository_template(name='REST')
template = usecase_template(name='REST')
template = service_template(name='REST')

#create_file(template)