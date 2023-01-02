# uvicorn graph_ql:app --host localhost --reload --port 5555
# http://localhost:5555/graphql, en postman siempre metodo post
""" 
query listUserByName{
  userList{
    name
    }
},
query listUserByAge{
  userList{
    age
    }
},
mutation addUser{
  addUserFunction(name:"uno",age:25){
    name
  }
}
"""

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from typing import List


@strawberry.type
class User:
    name: str
    age: int


user = [User(name="Patrick", age=100), User(name="July", age=22)]

@strawberry.type
class Query:
    @strawberry.field
    def user_list(self) -> List[User]: # retorna la lista de usuarios creados
        return user



@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user_function(self, name: str, age: int) -> User: # retorna solo el usuario creado
        user_added = User(name=name, age=age)
        user.append(user_added)
        return user_added

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)