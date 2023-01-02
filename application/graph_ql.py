# uvicorn graph_ql:app --host localhost --reload --port 5555
# http://localhost:5555/graphql
""" 
query user_info{
  user{
    name
  }
}
"""

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL



@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)


schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)