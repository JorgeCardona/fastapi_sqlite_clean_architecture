# uvicorn main:clean_architecture --host localhost --reload --port 5555

from configuration.fastapi.fast_api_configuration import clean_architecture
from services.service_products import ProductsServices
from services.service_users import UsersServices