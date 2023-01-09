# uvicorn main:clean_architecture --host localhost --reload --port 5555
# importacion de modulos con ruta RELATIVA completa del proyecto desde el inicio de cada carpeta para no tener que usar los puntos '...'
from configuration.fastapi.fast_api_configuration import clean_architecture
from services.service_products import ProductsServices
from services.service_users import UsersServices
from services.service_product_graphql import graphql_app, GRAPHQL_ROUTE


clean_architecture.add_route(GRAPHQL_ROUTE, graphql_app)
clean_architecture.add_websocket_route(GRAPHQL_ROUTE, graphql_app)