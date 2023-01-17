core = '# created by Jorge Cardona - https://github.com/JorgeCardona'

def core_template(name:str):
    content = f"""{core}
    """ 
    return content
 
def rest_template(name:str):
    
    application_name = name.lower()
    
    content = f"""{core}
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from configuration.cors.cors_configuration import CORSMiddleware, origins 
from configuration.swagger.swagger_configuration import SWAGGER_ROUTE, SWAGGER_REDOC_ROUTE

# INSTANCIA DE FASTAPI, PARA CONFIGURACION E INICIO DE LA APLICACION
{application_name} = FastAPI()
    """ 
    return content

def graphql_template(name:str):
    content = f"""{core}
    """ 
    return content
def swagger_template(name:str):
    content = f"""{core}
SWAGGER_ROUTE ='/docs'
SWAGGER_REDOC_ROUTE ='/redoc'
    """ 
    return content    

def cors_template(name:str):
    content = f"""{core}
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://localhost.jorgecardona.com",
    "http://localhost:3000",
    "http://localhost:8080",
]
    """ 
    return content
    
def utils_template(name:str):
    content = f"""{core}
    """ 
    return content


def environment_template(name:str):
    
    DB_DIALECT = '{DB_DIALECT}'
    DB_USER = '{DB_USER}'
    DB_PASSWORD = '{DB_PASSWORD}'
    DB_HOST = '{DB_HOST}'
    DB_PORT = '{DB_PORT}'
    DB_NAME = '{DB_NAME}'
    connect_args= "{'check_same_thread': False}"
    
    content = f"""{core}
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Environment:
    
    # es usada por la funcion get_sessioncon la variable de instancia self.Base
    Base =  declarative_base()
         
    def __init__(self) -> None:
        
        # eliminar la siguiente linea, es solo para definir que esta en ambiente de prueba
        os.environ.setdefault('ENVIRONMENT', 'local')
        
        # environment variables
        self.environment       = os.getenv('ENVIRONMENT', None)
        
        # obtains the database url for connection               
        self.data_base_url     = self.get_database_url()
        
        # since the function returns nothing then you don't need parentheses when assigning the variable to a function
        self.get_sessiones = self.get_session
        
        # get the database connection object       
        self.engine = self.get_engine()
        self.session_local = sessionmaker(bind=self.engine, expire_on_commit=False)

    def get_engine(self):
            
        #Creates database engine
        engine = create_engine(
            self.complete_data_base_url,
            connect_args={connect_args},
            echo =True,
            pool_recycle=3600
        )
        
        return engine
    
    def get_session(self):
        
        # esta relacionado con la variable definida al inicio de la clase
        self.Base.metadata.create_all(self.engine)
        
        session = self.session_local()
        try:
            yield session
        finally:
            session.close()
            
    # para graphql        
    def get_connection(self):
        
        return self.engine.connect()
        
        
    def get_database_url(self):
        
        # if does not exist environment defined, use the local environment database connection
        if self.environment:
            self.database_dialect  = 'sqlite'
            self.database_host     = 'configuration/database/sqlite_local'
            self.database_name     = 'clean_architecture.db'
                        
            self.complete_data_base_url = "{DB_DIALECT}:///{DB_HOST}/{DB_NAME}" \\
                                          .format(DB_DIALECT=self.database_dialect, DB_HOST=self.database_host, DB_NAME=self.database_name)                                          
        else:
            self.database_dialect       = os.environ["DB_DIALECT"]
            self.database_user          = os.environ["DB_USER"]
            self.database_password      = os.environ["DB_PASSWORD"]
            self.database_host          = os.environ["DB_HOST"]
            self.database_port          = os.environ["DB_PORT"]
            self.database_database_name = os.environ["DB_NAME"]
            self.complete_data_base_url = "{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" \\
                                           .format(DB_DIALECT=self.database_dialect, DB_USER=self.database_user, \\
                                                   DB_PASSWORD=self.database_password, DB_HOST=self.database_host, \\
                                                   DB_PORT=self.database_port, DB_NAME=self.database_name)       
        return self.complete_data_base_url
    """  
    return content

def database_template(name:str):
    content = f"""{core}
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configuration.environment.environment_configuration import Environment

instance = Environment()
get_session = instance.get_session
"""
    return content

def log_template(name:str):
    content = f"""{core}
import logging as log_api
import os

root_path = str(os.getcwd()).replace('\\\\','/')
LOG_FILE_NAME  = 'logging.log'
LOG_FOLDER = root_path + '/log'
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
    content = f"""{core}
BASE_PATH = '/{end_point}'
TAG = '{name_base}'
SEARCH_ALL_OBJECTS = 'Get {name_base} List'
SEARCH_SPECIFIC_OBJECT = 'Get {name_base}'
ADD_NEW_OBJECT = 'Add New {name_base}'
ADD_NEW_OBJECT_LIST = 'Add New {name_base} List'
REMOVE_OBJECT = 'Delete {name_base}'
UPDATE_OBJECT = 'Update {name_base}'
PATCH_OBJECT = 'Update {name_base} Partially'
"""  
    return content
 
def models_template(name:str):
    
    class_name = name.capitalize()
    table_name = name.lower() + 's'
    
    content = f"""{core}
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

def schemas_template(name:str):

    class_name =  name.capitalize()
    class_name_base = class_name + 'Create'
    
    content = f"""{core}
from pydantic import BaseModel
from typing import Optional
        
class {class_name_base}(BaseModel):
    name:str
    price:int
    categorie:str
    
    class Config:
        orm_mode = True
        
class {class_name}Read({class_name_base}):
    id:int      

class {class_name}Update({class_name_base}):
    pass
          
class {class_name}Patch(BaseModel):
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
    content = f"""{core}
from abc import ABC, abstractmethod

class {complete_class_name}(ABC):
    pass
    """ 
    return content
    
def repositories_template(name:str, complement='Repository'):
    
    class_name = name.capitalize()
    schema_name = name.lower()
    complete_class_name = class_name + complement
    
    content = f"""{core}
from abc import ABC, abstractmethod
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from configuration.database.database_configuration import get_session
from domain.entities.{schema_name}_entity.{schema_name}_model import {class_name} as model
from domain.entities.{schema_name}_entity.{schema_name}_schema import {class_name}Create as post_schema
from domain.entities.{schema_name}_entity.{schema_name}_schema import {class_name}Read as get_schema
from domain.entities.{schema_name}_entity.{schema_name}_schema import {class_name}Update as put_schema
from domain.entities.{schema_name}_entity.{schema_name}_schema import {class_name}Patch as patch_schema


class {complete_class_name}(ABC):

    @abstractmethod
    def get_object_list(self, session:Session = Depends(get_session), offset: int = 0, limit: int = 100):
        pass

    @abstractmethod
    def get_object(self, id:int, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def add_object(self, entity:post_schema, session:Session = Depends(get_session)):
        pass
 
    @abstractmethod
    def add_object_list(self, entity:List[post_schema], session:Session = Depends(get_session)):
         pass
    
    @abstractmethod
    def __update_rows__(self, id:int, entity:object, session:Session = Depends(get_session)):    
        pass
       
    @abstractmethod
    def update_object(self, id:int, entity:put_schema, session:Session = Depends(get_session)):
        pass

    @abstractmethod
    def patch_object(self, id:int, entity:patch_schema, session:Session = Depends(get_session)):
        pass
    
    @abstractmethod
    def delete_object(self, id:int, session:Session = Depends(get_session)):
        pass
"""
    return content

def usecases_template(name:str, complement='UseCase'):
    
    class_name = name.capitalize()
    schema_name = name.lower()
    complete_class_name = class_name + complement
    content = f"""{core}
from fastapi import HTTPException, status

from domain.interfaces.repositories.{schema_name}_repository import {class_name}Repository as repository
from domain.interfaces.repositories.{schema_name}_repository import Session, get_session, Depends, List
from domain.interfaces.repositories.{schema_name}_repository import model, get_schema, post_schema, put_schema, patch_schema
from configuration.log.log_configuration import log_api

class {complete_class_name}s(repository):
     
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
            
    def add_object(self, entity:post_schema, session:Session = Depends(get_session)):

        object_data = entity.dict(exclude_unset=True)
        object_ = model(**object_data)

        session.add(object_)
        session.commit()
        session.refresh(object_)
        return object_

    def add_object_list(self, entity:List[post_schema], session:Session = Depends(get_session)):

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
        
    def update_object(self, id:int, entity:put_schema, session:Session = Depends(get_session)):

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
        
 
def services_template(name:str, complement='Service'):
    
    class_name = name.capitalize()
    schema_name = name.lower()
    tag = 'TAG'
    complete_class_name = class_name + complement
    content = f"""{core}   
from fastapi import status
from configuration.rest.rest_configuration import clean_architecture

from usecases.{schema_name}_usecase import {class_name}UseCases as use_case
from usecases.{schema_name}_usecase import Session, get_session, Depends, List
from usecases.{schema_name}_usecase import get_schema, post_schema, put_schema, patch_schema

from configuration.end_points.{schema_name}_end_points_configuration import SEARCH_ALL_OBJECTS, SEARCH_SPECIFIC_OBJECT, ADD_NEW_OBJECT, ADD_NEW_OBJECT_LIST
from configuration.end_points.{schema_name}_end_points_configuration import BASE_PATH, UPDATE_OBJECT, PATCH_OBJECT, REMOVE_OBJECT, TAG

class {complete_class_name}:
    
    # retorna UNA LISTA DE OBJETOS con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso TODOS LOS CAMPOS
    @clean_architecture.get(BASE_PATH + "/", response_model=List[get_schema], name=SEARCH_ALL_OBJECTS)
    def get_object_list(session: Session = Depends(get_session), offset: int = 0, limit: int = 100):
        return use_case().get_object_list(session=session, offset=offset, limit=limit)

    # retorna UN OBJETO con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso todos los campos EXCEPTO EL CAMPO ID
    @clean_architecture.get(BASE_PATH + "/{id}",response_model=get_schema, name=SEARCH_SPECIFIC_OBJECT, tags=[{tag}] )
    def get_object(id:int, session: Session = Depends(get_session)):
        return use_case().get_object(id=id, session=session)

    @clean_architecture.post(BASE_PATH + "/", name=ADD_NEW_OBJECT, status_code=status.HTTP_201_CREATED, tags=[{tag}])
    def add_object(entity:post_schema, session: Session = Depends(get_session)):
        return use_case().add_object(entity=entity, session=session)

    @clean_architecture.post(BASE_PATH + "/all", name=ADD_NEW_OBJECT_LIST, status_code=status.HTTP_201_CREATED, tags=[{tag}])
    def add_object_list(entity:List[post_schema], session: Session = Depends(get_session)):
        return use_case().add_object_list(entity=entity, session=session)
    
    @clean_architecture.put(BASE_PATH + "/{id}", name=UPDATE_OBJECT, tags=[{tag}])
    def update_object(id:int, entity:put_schema, session: Session = Depends(get_session)):
        return use_case().update_object(id=id, entity=entity, session=session)

    @clean_architecture.patch(BASE_PATH + "/{id}", name=PATCH_OBJECT, tags=[{tag}])
    def patch_object(id:int, entity:patch_schema, session: Session = Depends(get_session)):
        return use_case().patch_object(id=id, entity=entity, session=session)
    
    # status_code=status.HTTP_204_NO_CONTENT, genera excepcion porque retorna mensaje
    @clean_architecture.delete(BASE_PATH + "/{id}", status_code=status.HTTP_204_NO_CONTENT, name=REMOVE_OBJECT, tags=[{tag}])
    def delete_object(id:int, session: Session = Depends(get_session)):
        return use_case().delete_object(id=id, session=session)
    """
    return content
          
def create_file(file, template):
    
    with open(file,'w') as escribir:
        escribir.write(template)
    #print(template)
    
template = models_template(name='REST')
template = schemas_template(name='REST')
template = repositories_template(name='REST')
template = usecases_template(name='REST')
template = services_template(name='REST')

#create_file(template)