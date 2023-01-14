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
        """_summary_

        echo -> will log all statements,
        pool_recycle -> the pool to recycle connections after the given number of seconds has passed. 
        pool_size -> the number of connections to keep open inside the connection pool

        Returns:
            _type_: engine
        """
            
        #Creates database engine
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL,
            connect_args={"check_same_thread": False},
            echo =True,
            pool_recycle=3600
        )
        
        return engine
               
    def get_engine_dev(self):
        """_summary_
        set SQLITE database for testing the application
        Returns:
            _type_: database engine
        """        
        
        #Define database values
        DATABASE_NAME = 'clean_architecture.db'
        DIRECTORY_SAVE_SQLITE_DATABASE = 'configuration/database/sqlite_test'
        SQLALCHEMY_DATABASE_URL = f"sqlite:///{DIRECTORY_SAVE_SQLITE_DATABASE}/{DATABASE_NAME}"

        return self.create_engine(SQLALCHEMY_DATABASE_URL)

        
    def get_engine(self):
        """_summary_
        capture enviroment variables and create URL DATABASE CONNECTION

        # DIALECT MUST BE CONTAINS DRIVER IF NECESSARY-> dialect+driver
        postgresql+pg8000, postgresql+psycopg2 
        mysql+mysqldb, mysql+pymysql 
        oracle+cx_oracle 
        mssql+pyodbc, mssql+pymssql
        
        Returns:
            _type_: database engine
        """
        # environment variables

        dialect = os.environ["DB_DIALECT"]
        user = os.environ["DB_USER"]
        password = os.environ["DB_PASSWORD"]
        host = os.environ["DB_HOST"]
        port = os.environ["DB_PORT"]
        database = os.environ["DB_NAME"]
    
        # create url connection to database
        SQLALCHEMY_DATABASE_URL = "{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" \
                                  .format(DB_DIALECT=dialect, DB_USER=user, DB_PASSWORD=password, \
                                          DB_HOST=host, DB_PORT=port, DB_NAME=database)

        return self.create_engine(SQLALCHEMY_DATABASE_URL)
    
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