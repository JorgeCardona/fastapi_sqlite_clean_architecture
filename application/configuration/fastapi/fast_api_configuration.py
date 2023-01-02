from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from ..cors.cross_origin_config import CORSMiddleware, origins 

clean_architecture = FastAPI()

def custom_openapi():
    if clean_architecture.openapi_schema:
        return clean_architecture.openapi_schema
        
    openapi_schema = get_openapi(
        title="Clean Architecture Api Documentation",
        version="1.0.1",
        terms_of_service="http://example.com/terms/",
        description="Documentation for my custom OpenAPI schema",
            contact={
        "name": "Jorge Cardona",
        "url": "https://github.com/JorgeCardona/portfolio",
        "email": "jorgecardona@utp.edu.co",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    
        routes=clean_architecture.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }

    clean_architecture.openapi_schema = openapi_schema

    return clean_architecture.openapi_schema

# SWAGGER CONFIG
clean_architecture.openapi = custom_openapi

# CORS CONFIG
clean_architecture.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# METADATA CONFIG, agrupa los endpoints en el swagger y muestra su etiqueta y descripcion relacionada
tags_metadata = [
    {
        "name": "products",
        "description": "Operations with products. All operations and logic is also here.",
    },
    {
        "name": "users",
        "description": "Manage Users. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Users external docs",
            "url": "https://jorgecardona.com/",
        },
    },
]

clean_architecture.openapi_tags = tags_metadata