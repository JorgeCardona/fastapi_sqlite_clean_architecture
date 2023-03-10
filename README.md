# https://emojipedia.org
# https://gist.github.com/rxaviers/7360908
Repository with projects especially focused on Computer Science and Natural Sciences.

![Alt text](resources/clean_architecture.jpg)
# π SCAFFOLDING FOR CLEAN ARCHITECTURE IN MICROSERVICES

```
π¦jorge_cardona_project [project_directory]
β πdeployment [package]
β πrequirements [package]
β πtest [package]
β π README.md
β β οΈ .gitignore
β πapplication [package]
β β£ πconfiguration
β β£ πlog
β β£ πhtmlcov
β β£ πutils
β β£ πdomain [package]
β β β£ πentities [package]
β β β£ πinterfaces [package]
β β β β πrepositories [package]
β β β β πbusiness_logic [package]
β β β£ πusecases [package]
β β β£ πservices [package]
β β£ main.py [__main__]
```

# PROJECT PACKAGES STRUCTURE
```
π¦jorge_cardona_project [project_directory]
β πapplication [package]
β β£ π main.py [__main__]
β β£ πconfiguration
β β£ β π rest
β β β£ β π© app_configuration.py
β β£ β π environment
β β β£ β π‘ environment_configuration.py
β β£ β π  database
β β β£ β π database_configuration.py
β β£ β π log
β β β£ β π log_configuration.py
β β£ β π cors
β β β£ β π§ cors_configuration.py
β β£ β π swagger
β β β£ β πͺ swagger_configuration.py
β β£ πlog
β β£ β π¬ logging.log
β β£ πhtmlcov
β β£ β π main_py.html
β β£ πutils
β β£ β π script.py
β β£ β π° file.yaml
β β£ β π image.jpg
β β£ πdomain [package]
β β β£ πentities [package]
β β β β£ πentity_one
β β β β β π model_for_entity_ONE.py
β β β β β π¦ schema_for_entity_ONE.py
β β β β£ πentity_two
β β β β β π model_for_entity_TWO.py
β β β β β π¦ schema_for_entity_TWO.py
β β β β£ πentity_n
β β β β β π model_for_entity_N.py
β β β β β π¦ schema_for_entity_N.py
β β β£ πinterfaces [package]
β β β β πrepositories [package]
β β β β β β π database_method_model_Entity_ONE.py
β β β β β β π database_method_model_Entity_TWO.py
β β β β β β π database_method_model_Entity_N.py
β β β β πbusiness_logic [package]
β β β β β β π¦ business_logic_method_model_Entity_ONE.py
β β β β β β π¦ business_logic_method_model_Entity_TWO.py
β β β β β β π¦ business_logic_method_model_Entity_N.py
β β β£ πusecases [package]
β β β β β π use_case_implementation_business_repository_logic_model_ONE.py
β β β β β π use_case_implementation_business_repository_logic_model_TWO.py
β β β β β π use_case_implementation_business_repository_logic_model_N.py
β β β£ πservices [package]
β β β β β βοΈ services_use_case_implementation_model_ONE.py
β β β β β βοΈ services_use_case_implementation_model_TWO.py
β β β β β βοΈ services_use_case_implementation_model_N.py
β πdeployment [package]
β β π³ Dockerfile
β β π° Manifest.yaml
β πrequirements [package]
β β π requirements.txt
β πtest [package]
β β β£ πtest_case_one
β β β β π use_case_implementation_one.py
β β β β π services_use_case_implementation_one.py
β β β£ πtest_case_two
β β β β π use_case_implementation_two.py
β β β β π services_use_case_implementation_two.py
β β β£ πtest_case_n
β β β β π use_case_implementation_n.py
β β β β π services_use_case_implementation_n.py
β π README.md
β β οΈ .gitignore
```

# Application
Directory that contains the packages with the application code.

# Configuration
Contains all configuration files for the Application

# Log
Save information about the application log.

# htmlcov
Save unit testing coverage information about the application code.

# Utils
Contains transversal resources for the application, that is not possible to include in other layers.

# Entities
is a package that contains modules, like Models and Schemas, the module it's a plain script, it contains only the class definition and no logic in the classes.
- **Models**: are modules that contain the fields from a table on the database and it is represented by a class.
- **Schemas**: these are modules that contain the fields Used to validate data we receive as well as to reformat the data that we want to send to the client/browser, so just contains the fields that we want to return in the request.

# Interfaces
are interfaces that contain only the methods that need to be implemented in the use cases one directory by class.
- **Repository**: Contains modules with methods that are needed to communicate with the database by class.
- **Business**: Contains modules with methods that are needed to process the information by class.

# Use Cases
is a package that contains modules, the module is a class that implements the methods from the package interfaces(Repository, Business) and defines the business logic by module.

# Services
is a package that contains modules, the module is a class that contains the API services by functionality or by class and use the UseCases classes.

# Web, Devices, DB, UI, External Interfaces
layer that communicates internal API services with API consumers.

# Deployment
Directory that contains the Dockerfile, k8s Manifest, and every file needed for the deployment.

# Requirements
Directory containing the requirements.txt with the definition of project dependencies.

# Test
Directory that contains the unit testing from the Use Cases and Services files.
