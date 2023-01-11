from domain.entities.schemas.schema_product_graphql import ProductGraphQl
from usecases.usecase_graphql import ProductsUseCasesGraphQL
from configuration.graphql.graphql_config import GRAPHQL_ROUTE

import strawberry
from strawberry.asgi import GraphQL
from typing import AsyncGenerator, List
import asyncio

@strawberry.type
class Query:
  
    @strawberry.field
    def get_object_list(self) -> List[ProductGraphQl]:

        return ProductsUseCasesGraphQL().get_all_records()
    
    @strawberry.field
    def get_first_object(self) -> ProductGraphQl:

        return ProductsUseCasesGraphQL().get_first_record()
    
    @strawberry.field
    def get_last_object(self) -> ProductGraphQl:

        return ProductsUseCasesGraphQL().get_last_record()

    @strawberry.field
    def get_specific_record(self, id: int) -> List[ProductGraphQl]:

        return ProductsUseCasesGraphQL().get_record(id=id) 
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_product(self, name: str, categorie: str, price: int) -> ProductGraphQl:
        entity = ProductGraphQl(id=1,name=name,categorie=categorie,price=price)
        object_ = ProductsUseCasesGraphQL().insert_one_record(name=name,categorie=categorie,price=price)
        return entity
    
    @strawberry.mutation
    def remove_product(self, id: int) -> str:
        object_ = ProductsUseCasesGraphQL().delete_record(id=id)
        return f'record with id={id} deleted succesfully' if  object_ else f'record with id={id} does not exists'

    @strawberry.mutation
    def upgrade_product(self, id: int, name: str = None, categorie: str = None, price: int = None) -> str:
        entity = ProductGraphQl(id=id,name=name,categorie=categorie,price=price)
        
        object_ = ProductsUseCasesGraphQL().update_record(entity=entity)
        return object_ if object_ else f'record with id={id} does not exists'
                              
@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 10) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)
            

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)



graphql_app = GraphQL(schema)