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

        return ProductsUseCasesGraphQL().get_object_list()
    
    @strawberry.field
    def get_first_object(self) -> ProductGraphQl:

        return ProductsUseCasesGraphQL().get_first_record()
    
    @strawberry.field
    def get_last_object(self) -> ProductGraphQl:

        return ProductsUseCasesGraphQL().get_last_record()

    
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
        return f'record with id={id} deleted succesfully'

    @strawberry.mutation
    def upgrade_product(self, id: int, name: str = None, categorie: str = None, price: int = None) -> str:
        object_ = ProductsUseCasesGraphQL().update_record(id=id,name=name,categorie=categorie,price=price)
        return f'record with id={id} updated succesfully'
                              
@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 10) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)
            

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)



graphql_app = GraphQL(schema)