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

    def get_database_url(self):
        
        # if does not exist environment defined, use the local environment database connection
        if self.environment:
            self.database_dialect  = 'sqlite'
            self.database_host     = 'configuration/database/sqlite_local'
            self.database_name     = 'clean_architecture.db'
                        
            self.complete_data_base_url = "{DB_DIALECT}:///{DB_HOST}/{DB_NAME}" \
                                          .format(DB_DIALECT=self.database_dialect, DB_HOST=self.database_host, DB_NAME=self.database_name)                                          
        else:
            self.database_dialect       = os.environ["DB_DIALECT"]
            self.database_user          = os.environ["DB_USER"]
            self.database_password      = os.environ["DB_PASSWORD"]
            self.database_host          = os.environ["DB_HOST"]
            self.database_port          = os.environ["DB_PORT"]
            self.database_database_name = os.environ["DB_NAME"]
            self.complete_data_base_url = "{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" \
                                           .format(DB_DIALECT=self.database_dialect, DB_USER=self.database_user, \
                                                   DB_PASSWORD=self.database_password, DB_HOST=self.database_host, \
                                                   DB_PORT=self.database_port, DB_NAME=self.database_name)       
        return self.complete_data_base_url
        
        
        
    def get_engine(self):
        """_summary_

        echo -> will log all statements,
        pool_recycle -> the pool to recycle connections after the given number of seconds has passed. 
        pool_size -> the number of connections to keep open inside the connection pool

        Returns:
            _type_: engine
        """
            
        #Creates database engine
        engine = create_engine(
            self.complete_data_base_url,
            connect_args={'check_same_thread': False},
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