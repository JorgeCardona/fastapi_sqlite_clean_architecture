from domain.entities.schemas.schema_product_graphql import ProductGraphQl
from usecases.usecase_graphql import ProductsUseCasesGraphQL

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
    def add_book(self, name: str, categorie: str, price: int) -> ProductGraphQl:
        entity = ProductGraphQl(id=1,name=name,categorie=categorie,price=price)
        object_ = ProductsUseCasesGraphQL().insert_one_record(name=name,categorie=categorie,price=price)
        return entity
                      
@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 10) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)
            

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)



graphql_app = GraphQL(schema)