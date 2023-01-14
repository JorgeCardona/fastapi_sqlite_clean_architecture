from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
# importacion de modulos con ruta RELATIVA completa del proyecto desde el inicio de cada carpeta para no tener que usar los puntos '...'
from configuration.graphql.graphql_config import GRAPHQL_ROUTE, GRAPHQL_ALIAS
from configuration.cors.cross_origin_config import CORSMiddleware, origins 
from configuration.swagger.swagger_configuration import SWAGGER_ROUTE, SWAGGER_REDOC_ROUTE, SWAGGER_REDOC_ALIAS

# INSTANCIA DE FASTAPI, PARA CONFIGURACION E INICIO DE LA APLICACION
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

# adicionadas configuracion de rutas personalizadas para la documentacion de SWAGGER
clean_architecture.docs_url = SWAGGER_ROUTE
clean_architecture.redoc_url = SWAGGER_REDOC_ROUTE

# adicionados la informacion para mostrar en swagger
clean_architecture.openapi_tags = tags_metadata

# REDIRECCIONAMIENTO DE PETICIONES A OTRAS URL
from starlette.responses import RedirectResponse

# funcion que ejecuta el redireccionamiento solicitado
def redirect_url_response(url):
    return RedirectResponse(url=f"{url}")

# redireccionamiento a la documentacion cuando se abre el path principal en el navegador
# include_in_schema=False, oculta el endpoint de la documentacion de swagger
@clean_architecture.get("/", include_in_schema=False)
def swagger_url(url=SWAGGER_ROUTE):
    return redirect_url_response(url)

# redireccionamiento para redoc
@clean_architecture.get(f"{SWAGGER_REDOC_ALIAS}", include_in_schema=False)
def swagger_redoc_url(url=SWAGGER_REDOC_ROUTE):
    return redirect_url_response(url)

# redireccionamiento a la consola graphql cuando se pone un alias
@clean_architecture.get(f"{GRAPHQL_ALIAS}", include_in_schema=False)
def graphql_url(url=GRAPHQL_ROUTE):
    return redirect_url_response(url)

# definicion de parametros de configuracion para la API
API_PORT = 5555
API_HOST = 'localhost'

# metodo para iniciar la aplicacion equivalente a uvicorn main:clean_architecture --host localhost --reload --port 5555
def run_application():
    import uvicorn
    uvicorn.run(app='main:clean_architecture', 
                host=API_HOST, 
                port=API_PORT,
                reload=True
                )