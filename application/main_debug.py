from configuration.fastapi.fast_api_configuration import API_APP, API_HOST, API_PORT

import uvicorn
if __name__ == "__main__":
    uvicorn.run(app=API_APP, 
                host=API_HOST, 
                port=API_PORT)
    