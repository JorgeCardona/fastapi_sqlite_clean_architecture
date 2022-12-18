# uvicorn main:clean_architecture --host localhost --reload --port 5555

from configuration.fastapi.fast_api_configuration import clean_architecture
#from configuration.database.db_config import get_session
from services.service_product import ProductServices
from configuration.log.logging import log_api

###poner log donde es!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
log_api.warning('buenoooo')
