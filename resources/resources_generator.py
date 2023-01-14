class CreateResources:
    
    def __init__(self, name='application', application_type='REST'):
        
        self.application_directory_name = name
        self.application_application_type = str(application_type).upper()
        
        self.configurations_directory = f'{self.application_directory_name}/configuration'
        self.domain_directory         = f'{self.application_directory_name}/domain'
        self.entities_directory       = f'{self.domain_directory}/entities'
        self.models_directory         = f'{self.entities_directory}/models'
        self.schemas_directory        = f'{self.entities_directory}/schemas'
        self.interfaces_directory     = f'{self.domain_directory}/interfaces'
        self.repositories_directory   = f'{self.interfaces_directory}/repositories'
        self.business_directory       = f'{self.interfaces_directory}/business'
        self.usecases_directory       = f'{self.application_directory_name}/usecases'
        self.services_directory       = f'{self.application_directory_name}/services'
        self.basic_directory          = ['test',
                                        'deployment',
                                        'requirements']
        # TODO --------- eliminar la linea siguiente, es solo para que no genere otros directorios en las pruebas
        self.basic_directory= []            
        self.scaffolding_directories_list = [self.usecases_directory, self.services_directory]
        
        # dictionary for creates resource
        self.resources ={
            'entity':{
                'directory':[self.entities_directory, self.entities_directory],
                'shared_directory': ['entity_', 'entity_'],
                'suffix': ['_model.py','_schema.py'],
                'template':[]
            },
            'model':{
                'directory':[self.entities_directory],
                'shared_directory': ['entity_'],
                'suffix': ['_model.py'],
                'template':['code_templates/09_model_template.py']
            },            
            'schema':{
                'directory':[self.entities_directory],
                'shared_directory': ['entity_'],
                'suffix': ['_schema.py'],
                'template':[]
            },
            'interface':{
                'directory':[self.repositories_directory, self.business_directory],
                'suffix': ['_repository.py', '_business.py'],
                'template':[]
            },            
            'repository':{
                'directory':[self.repositories_directory],
                'suffix': ['_repository.py'],
                'template':[]
            },    
            'business':{
                'directory':[self.business_directory],
                'suffix': ['_business.py'],
                'template':[]
            },   
            'usecase':{
                'directory':[self.usecases_directory],
                'suffix': ['_usecase.py'],
                'template':[]
            },    
            'service':{
                'directory':[self.services_directory],
                'suffix': ['_service.py'],
                'template':[]
            },  
            'all':{
                'directory':[self.entities_directory, 
                             self.entities_directory,
                             self.repositories_directory, 
                             self.business_directory, 
                             self.usecases_directory, 
                             self.services_directory
                            ],
                'suffix': [
                           '_model.py',
                           '_schema.py',
                           '_repository.py',
                           '_business.py',
                           '_usecase.py',
                           '_service.py'                           
                           ],
                'template':[]
            },  
        }
                 
    def __basics_directories_list__(self):
        
        self.scaffolding_directories_list.extend(self.basic_directory)
        return [self.basic_directory]

    def __configurations_directories_list__(self):
        
        api_type_directory = '/graphql' if self.application_application_type == 'GRAPHQL' else '/rest'
        
        configurations_directories = [
                       api_type_directory,
                       '/environment',
                       '/database',
                       '/utils',
                       '/cors',
                       '/log'                       
                       ]
        
        directories = [self.configurations_directory + directory for directory in  configurations_directories]
        # add configurations_directories_list
        self.scaffolding_directories_list.extend(directories)
        
        return [self.configurations_directory + directory for directory in directories]
        
    def __domain_directories_list__(self):
        
        directories = [
                       self.entities_directory,
                       self.repositories_directory,
                       self.business_directory,
                      ]

        # add configurations_directories_list
        self.scaffolding_directories_list.extend(directories)
        
        return directories

    def __scaffolding_directories_list__(self):

        # load every list from every function and add to scaffolding list
        self.__basics_directories_list__()
        self.__configurations_directories_list__()
        self.__domain_directories_list__  ()     
        
        # order list by name
        self.scaffolding_directories_list.sort()
        
        return self.scaffolding_directories_list

    def create_file(self, file, template=None):
        
        """_summary_
        create every python file required

        Args:
            file (_type_): name of file to create
            template (_type_): create content into the file using template for it
        """
        
        from os import path

        # if exists file does not replace it
        if not path.exists(file):            
            with open(f'{file}','w') as file_create:
                pass
        
    def create_scaffolding(self):
        """_summary_

        creates every directory defined for clean architecture
        Returns:
            _type_: successfull mesage
        """
        from os import makedirs
        
        directories_list = self.__scaffolding_directories_list__()

        for directory in directories_list:
            
            # creates every directory on the list, if a directory exists ignore creating it
            makedirs(directory, exist_ok=True)
            
            #  if the directory is inside the source code folder, creates __init__.py
            if directory.__contains__('/'):
                self.create_file(f'{directory}/__init__.py')    

        return 'All Directories were created Successfully'
        
    def create_resource(self, resource_type, file_name):
        """_summary_
        Creates every resource python file into folder
        it depends from resource_type

        Args:
            resource_type (_type_): every diferent resource type
            file_name (_type_): name of file to create
        """
        
        dictionary = self.resources.get(resource_type)
        
        directory = dictionary.get('directory')
        resource_name =  dictionary.get('suffix')
        file = str(file_name).lower()
        shared_directory = dictionary.get('shared_directory')
        
        self.create_scaffolding()
        
        for index, directory_value in enumerate(directory):
            
            # si los archivos estan dentro de un mismo directorio con nombre unificado
            if shared_directory:
                from os import makedirs
                # crea el nombre del directorio basado en el nombre del archivo
                directory_value = f'{directory_value}/{shared_directory[index]}{file}'               
                makedirs(directory_value, exist_ok=True)

            self.create_file(f'{directory_value}/{file}{resource_name[index]}')
     
    def create_resource_from_template(self, resource_type, file_name):
        """_summary_
        Creates every resource python file into folder
        it depends from resource_type

        Args:
            resource_type (_type_): every diferent resource type
            file_name (_type_): name of file to create
        """
        
        dictionary = self.resources.get(resource_type)
        
        directory = dictionary.get('directory')
        resource_name =  dictionary.get('suffix')
        file = str(file_name).lower()
        template_base = dictionary.get('template')
        
        self.create_scaffolding()
        
        for index, directory_value in enumerate(directory):

            self.create_file(file=f'{directory_value}/{file}{resource_name[index]}', template=template_base)