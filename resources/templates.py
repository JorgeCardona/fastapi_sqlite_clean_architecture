core = '# created by Jorge Cardona - https://github.com/JorgeCardona'
llave_abre = '{'
llave_cierra = '}'

def main_debug(name:str):
    content = f"""{core}
from configuration.rest.rest_configuration import run_application

# start this Script on debug Mode for debugging the application
if __name__ == "__main__":
    run_application()
    """ 
    return content
    
def core_template(name:str):
    content = f"""{core}
    """ 
    return content

def mix_template(name:str):
    
    application_name = name.lower()

    API_PORT = 5555
    API_HOST = 'localhost'
    
    content = f"""{core} 
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

# importacion de modulos con ruta RELATIVA completa del proyecto desde el inicio de cada carpeta para no tener que usar los puntos '...'
from configuration.graphql.graphql_configuration import GRAPHQL_ROUTE, GRAPHQL_ALIAS
from configuration.cors.cors_configuration import CORSMiddleware, origins 
from configuration.swagger.swagger_configuration import SWAGGER_ROUTE, SWAGGER_REDOC_ROUTE, SWAGGER_REDOC_ALIAS

# INSTANCIA DE FASTAPI, PARA CONFIGURACION E INICIO DE LA APLICACION
{application_name} = FastAPI()

def custom_openapi():
    if {application_name}.openapi_schema:
        return {application_name}.openapi_schema
        
    openapi_schema = get_openapi(
        title="Clean Architecture Api Documentation",
        version="1.0.1",
        terms_of_service="http://example.com/terms/",
        description="Documentation for my custom OpenAPI schema",
            contact={llave_abre}
        "name": "Jorge Cardona",
        "url": "https://github.com/JorgeCardona/portfolio",
        "email": "jorgecardona@utp.edu.co",
    {llave_cierra},
    license_info={llave_abre}
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    {llave_cierra},
    
        routes={application_name}.routes,
    )
    openapi_schema["info"]["x-logo"] = {llave_abre}
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    {llave_cierra}

    {application_name}.openapi_schema = openapi_schema

    return {application_name}.openapi_schema
    
# SWAGGER CONFIG
{application_name}.openapi = custom_openapi

# CORS CONFIG
{application_name}.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# METADATA CONFIG, agrupa los endpoints en el swagger y muestra su etiqueta y descripcion relacionada
tags_metadata = [
    {llave_abre}
        "name": "products",
        "description": "Operations with products. All operations and logic is also here.",
    {llave_cierra},
    {llave_abre}
        "name": "users",
        "description": "Manage Users. So _fancy_ they have their own docs.",
        "externalDocs": {llave_abre}
            "description": "Users external docs",
            "url": "https://jorgecardona.com/",
        {llave_cierra},
    {llave_cierra},
]

# adicionadas configuracion de rutas personalizadas para la documentacion de SWAGGER
{application_name}.docs_url = SWAGGER_ROUTE
{application_name}.redoc_url = SWAGGER_REDOC_ROUTE

# adicionados la informacion para mostrar en swagger
{application_name}.openapi_tags = tags_metadata

# REDIRECCIONAMIENTO DE PETICIONES A OTRAS URL
from starlette.responses import RedirectResponse

# funcion que ejecuta el redireccionamiento solicitado
def redirect_url_response(url):
    return RedirectResponse(url=url)

# redireccionamiento a la documentacion cuando se abre el path principal en el navegador
# include_in_schema=False, oculta el endpoint de la documentacion de swagger
@{application_name}.get("/", include_in_schema=False)
def swagger_url(url=SWAGGER_ROUTE):
    return redirect_url_response(url)

# redireccionamiento para redoc
@{application_name}.get(SWAGGER_REDOC_ALIAS, include_in_schema=False)
def swagger_redoc_url(url=SWAGGER_REDOC_ROUTE):
    return redirect_url_response(url)

# redireccionamiento a la consola graphql cuando se pone un alias
@{application_name}.get(GRAPHQL_ALIAS, include_in_schema=False)
def graphql_url(url=GRAPHQL_ROUTE):
    return redirect_url_response(url)
    
# definicion de parametros de configuracion para la API
API_PORT = {API_PORT}
API_HOST = '{API_HOST}'

# inicia la aplicacion importando el metodo run_application en el main.py o en el main_debug.py sin usar el comando
# uvicorn main:{application_name} --host {API_HOST} --reload --port {API_PORT}
def run_application():
    import uvicorn
    uvicorn.run(app='main:{application_name}', 
                host=API_HOST, 
                port=API_PORT,
                reload=True
                )        
    """ 
    return content

def rest_template(name:str):
    
    application_name = name.lower()
    
    content = f"""{core} 
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

# importacion de modulos con ruta RELATIVA completa del proyecto desde el inicio de cada carpeta para no tener que usar los puntos '...'
from configuration.graphql.graphql_configuration import GRAPHQL_ROUTE, GRAPHQL_ALIAS
from configuration.cors.cors_configuration import CORSMiddleware, origins 
from configuration.swagger.swagger_configuration import SWAGGER_ROUTE, SWAGGER_REDOC_ROUTE, SWAGGER_REDOC_ALIAS

# INSTANCIA DE FASTAPI, PARA CONFIGURACION E INICIO DE LA APLICACION
{application_name} = FastAPI()

def custom_openapi():
    if {application_name}.openapi_schema:
        return {application_name}.openapi_schema
        
    openapi_schema = get_openapi(
        title="Clean Architecture Api Documentation",
        version="1.0.1",
        terms_of_service="http://example.com/terms/",
        description="Documentation for my custom OpenAPI schema",
            contact={llave_abre}
        "name": "Jorge Cardona",
        "url": "https://github.com/JorgeCardona/portfolio",
        "email": "jorgecardona@utp.edu.co",
    {llave_cierra},
    license_info={llave_abre}
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    {llave_cierra},
    
        routes={application_name}.routes,
    )
    openapi_schema["info"]["x-logo"] = {llave_abre}
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    {llave_cierra}

    {application_name}.openapi_schema = openapi_schema

    return {application_name}.openapi_schema
    
# SWAGGER CONFIG
{application_name}.openapi = custom_openapi

# CORS CONFIG
{application_name}.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# METADATA CONFIG, agrupa los endpoints en el swagger y muestra su etiqueta y descripcion relacionada
tags_metadata = [
    {llave_abre}
        "name": "products",
        "description": "Operations with products. All operations and logic is also here.",
    {llave_cierra},
    {llave_abre}
        "name": "users",
        "description": "Manage Users. So _fancy_ they have their own docs.",
        "externalDocs": {llave_abre}
            "description": "Users external docs",
            "url": "https://jorgecardona.com/",
        {llave_cierra},
    {llave_cierra},
]

# adicionadas configuracion de rutas personalizadas para la documentacion de SWAGGER
{application_name}.docs_url = SWAGGER_ROUTE
{application_name}.redoc_url = SWAGGER_REDOC_ROUTE

# adicionados la informacion para mostrar en swagger
{application_name}.openapi_tags = tags_metadata

# REDIRECCIONAMIENTO DE PETICIONES A OTRAS URL
from starlette.responses import RedirectResponse

# funcion que ejecuta el redireccionamiento solicitado
def redirect_url_response(url):
    return RedirectResponse(url=url)

# redireccionamiento a la documentacion cuando se abre el path principal en el navegador
# include_in_schema=False, oculta el endpoint de la documentacion de swagger
@{application_name}.get("/", include_in_schema=False)
def swagger_url(url=SWAGGER_ROUTE):
    return redirect_url_response(url)

# redireccionamiento para redoc
@{application_name}.get(SWAGGER_REDOC_ALIAS, include_in_schema=False)
def swagger_redoc_url(url=SWAGGER_REDOC_ROUTE):
    return redirect_url_response(url)

# redireccionamiento a la consola graphql cuando se pone un alias
@{application_name}.get(GRAPHQL_ALIAS, include_in_schema=False)
def graphql_url(url=GRAPHQL_ROUTE):
    return redirect_url_response(url)
    
# definicion de parametros de configuracion para la API
API_PORT = 5555
API_HOST = 'localhost'

def run_application():
    import uvicorn
    uvicorn.run(app='main:{application_name}', 
                host=API_HOST, 
                port=API_PORT,
                reload=True
                )        
    """ 
    return content

def graphql_template(name:str):
    content = f"""{core}
GRAPHQL_ROUTE = '/graphql'
GRAPHQL_ALIAS = '/gql'
    """ 
    return content
def swagger_template(name:str):
    content = f"""{core}
SWAGGER_ROUTE ='/docs'
SWAGGER_REDOC_ROUTE ='/redoc'
SWAGGER_REDOC_ALIAS = '/rd'
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
    complete_class_name = class_name + complement
    
    content = f"""{core}
from abc import ABC, abstractmethod

class {complete_class_name}(ABC):

    @abstractmethod
    def get_response_format(self, data, offset: int = 0, limit: int = 100, page_number : int = 1, page_size : int = 10):
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
    
    id = '{id}'
    data = 'data'

    content = f"""{core}
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from domain.interfaces.repositories.{schema_name}_repository import {class_name}Repository as repository
from domain.interfaces.business_logic.{schema_name}_business_logic import {class_name}BusinessLogic as business_logic
from domain.interfaces.repositories.{schema_name}_repository import Session, get_session, Depends, List
from domain.interfaces.repositories.{schema_name}_repository import model, get_schema, post_schema, put_schema, patch_schema
from configuration.end_points.{schema_name}_end_points_configuration import BASE_PATH
from configuration.log.log_configuration import log_api

class {complete_class_name}s(repository, business_logic):

    def get_response_format(self, data, offset: int = 0, limit: int = 100, page_number : int = 1, page_size : int = 10):
        
        if type(data) == list:
            import math
            start = (page_number - 1) * page_size
            end = start + page_size
            total_data = len(data)
            total_pages = math.ceil(total_data / page_size)
            
            response_data = {llave_abre}
                
                'data':data[start:end],            
                'count':page_size,
                'total':len(data),
                'page': f'{llave_abre}page_number{llave_cierra} from {llave_abre}total_pages{llave_cierra}',
                'pagination':{llave_abre}
                            'previous':None,
                            'next':None
                            {llave_cierra}
            {llave_cierra}
                        
            if page_number > 1:
                response_data['pagination']['previous'] = f'{llave_abre}BASE_PATH{llave_cierra}/?offset={llave_abre}offset{llave_cierra}&limit={llave_abre}limit{llave_cierra}&page_number={llave_abre}page_number-1{llave_cierra}&page_size={llave_abre}page_size{llave_cierra}'
                
            if end < total_data:
                response_data['pagination']['next'] = f'{llave_abre}BASE_PATH{llave_cierra}/?offset={llave_abre}offset{llave_cierra}&limit={llave_abre}limit{llave_cierra}&page_number={llave_abre}page_number+1{llave_cierra}&page_size={llave_abre}page_size{llave_cierra}'
                 
        elif type(data) == dict:
            response_data = {llave_abre}data{llave_cierra} if 'error' not in data else data
            
        else:
            response_data = {llave_abre}'data':data{llave_cierra}
            
        return response_data 
             
    def get_object_list(self, session:Session = Depends(get_session), offset: int = 0, limit: int = 100):
           
        object_ = session.query(model).offset(offset).limit(limit).all()
        return object_
    

    def get_object(self, id:int, session:Session = Depends(get_session)):
        
        object_ = session.query(model).get(id)
        
        if object_:
            return object_ 
        else:
            message = f"Resource with id {id} not found"
            log_api.warning(message)
            
            response = {llave_abre}
                        'error': {llave_abre}
                            'code': status.HTTP_404_NOT_FOUND,
                            'message': message
                        {llave_cierra}
            {llave_cierra}
            
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=response)
                        
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

        if object_.__dict__.get('status_code') != 404:
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
             
        if isinstance(object_, model):

            session.delete(object_)
            session.commit()
            session.close()
            
            # delete sqlalchemy key
            object_.__dict__.pop('_sa_instance_state')
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=object_.__dict__)           
            
        else:
            return object_
    """ 
    return content
        
 
def services_template(name:str, complement='Service'):
    
    class_name = name.capitalize()
    schema_name = name.lower()
    tag = 'TAG'
    id = '{id}'
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
    def get_object_list(session: Session = Depends(get_session), offset: int = 0, limit: int = 100, page_number : int = 1, page_size : int = 10):
        data = use_case().get_object_list(session=session, offset=offset, limit=limit)
        response = use_case().get_response_format(data, offset=offset, limit=limit, page_number=page_number, page_size=page_size)
        return response

    # retorna UN OBJETO con los campos que tenga el ESQUEMA DEL RESPONSE MODEL en este caso todos los campos EXCEPTO EL CAMPO ID
    @clean_architecture.get(BASE_PATH + "/{id}",response_model=get_schema, name=SEARCH_SPECIFIC_OBJECT, tags=[{tag}] )
    def get_object(id:int, session: Session = Depends(get_session)):
        data = use_case().get_object(id=id, session=session)
        response = use_case().get_response_format(data=data)
        return response

    @clean_architecture.post(BASE_PATH + "/", name=ADD_NEW_OBJECT, status_code=status.HTTP_201_CREATED, tags=[{tag}])
    def add_object(entity:post_schema, session: Session = Depends(get_session)):
        data = use_case().add_object(entity=entity, session=session)
        response = use_case().get_response_format(data=data)
        return response

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
    @clean_architecture.delete(BASE_PATH + "/{id}", name=REMOVE_OBJECT, tags=[{tag}])
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