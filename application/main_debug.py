from configuration.fastapi.fast_api_configuration import API_HOST, API_PORT
from main import clean_architecture
# INICIAR ESTE SCRIPT EN MODO DEBUG PARA DEBUGGEAR LA APLICACION
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app=clean_architecture, 
                host=API_HOST, 
                port=API_PORT)
    