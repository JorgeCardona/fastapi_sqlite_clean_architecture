
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
        SQLALCHEMY_DATABASE_URL = f"sqlite:///DIRECTORY_SAVE_SQLITE_DATABASE/DATABASE_NAME"

        return self.create_engine(SQLALCHEMY_DATABASE_URL)
