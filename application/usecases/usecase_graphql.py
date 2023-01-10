from configuration.environment.env import Environment
from sqlalchemy import text
from domain.entities.schemas.schema_product_graphql import ProductGraphQl
from sqlalchemy import select, insert, delete, update

from domain.interfaces.repositories.repository_products import Session, get_session, Depends, List
from domain.entities.models.model_products import Product as model

""" 
mutation adicionar{
  addBook(
    name:"uno",
    categorie:"humor",
    price:1978
  ) {
	name
  }
},
query todos{
  getObjectList{
    id,
    name,
    price
  }
},

query ultimo{
  getLastObject{
    price,
    id
  }
},
query primero{
  getFirstObject{
    name,
    categorie
  }
},
subscription subscripcion{
  
  count
},
"""
class ProductsUseCasesGraphQL:

    def get_object_list(self, offset: int = 0, limit: int = 100):
           
        with Environment('dev').get_connection() as connection:
            result = connection.execute(text("SELECT * FROM products"))
            
            results_as_dict = result.mappings().all()
        return results_as_dict
           
    def insert_one_record(self, name, categorie, price) -> int:
    
        with Environment('dev').get_connection() as connection:
            
            query = insert(model).values(name=name, categorie=categorie, price=price)
            
            result = connection.execute(query)
            
        return result
    
    def get_first_record(self):

        with Environment('dev').get_connection() as connection:
            result = connection.execute(text("SELECT * FROM products"))
            results_as_dict = result.mappings().first()
        
        return results_as_dict
    
    def get_last_record(self):
    
        with Environment('dev').get_connection() as connection:
            result = connection.execute(text("SELECT * FROM products ORDER BY id DESC"))
            
            results_as_dict = result.mappings().first()
        
        return results_as_dict
           
    def get_all_records(self):
        with Environment('dev').get_connection() as connection:
            result = connection.execute(text("SELECT * FROM products"))
            
            results_as_dict = result.mappings().all()
        
        return results_as_dict
      
    def delete_record(self, id) -> int:
    
        with Environment('dev').get_connection() as connection:
            
            query = delete(model).where(model.id == id)
            result = connection.execute(query)
            
        return result
      
      
    def get_record(self, id):
          
        with Environment('dev').get_connection() as connection:
          
          query = select(model).where(model.id == id)

          result = connection.execute(query)
        
        return result
      
      
    def update_record(self, id, name=None, categorie=None, price=None) -> int:
          
        record = self.get_record(id)
        
        if record :
          values = {'name':name,
                    'categorie':categorie,
                    'price':price
                    }
          
          with Environment('dev').get_connection() as connection:
              
              query = update(model).where(model.id == id).values(
                values
              )
              result = connection.execute(query)
              
          return result
        
        return None