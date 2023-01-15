class CreateResources:
    
    def __init__(self, main_directory_name, application_type):
        
        self.application_directory_name = str(main_directory_name).lower()
        self.application_application_type = str(application_type).upper()
        
        self.configurations_directory = f'{self.application_directory_name}/configuration'
        self.domain_directory         = f'{self.application_directory_name}/domain'
        self.entities_directory       = f'{self.domain_directory}/entities'
        self.models_directory         = f'{self.entities_directory}/models'
        self.schemas_directory        = f'{self.entities_directory}/schemas'
        self.interfaces_directory     = f'{self.domain_directory}/interfaces'
        self.repositories_directory   = f'{self.interfaces_directory}/repositories'
        self.business_logic_directory = f'{self.interfaces_directory}/business_logic'
        self.usecases_directory       = f'{self.application_directory_name}/usecases'
        self.services_directory       = f'{self.application_directory_name}/services'
        self.basic_directory          = ['test',
                                        'deployment',
                                        'requirements']
        # TODO --------- eliminar la linea siguiente, es solo para que no genere otros directorios en las pruebas
        self.basic_directory= []
        self.configurations_directories   = None   
        self.scaffolding_directories_list = [self.interfaces_directory, self.usecases_directory, self.services_directory]
        
        # dictionary for creates resource
        self.resources = self.get_resources_list()
        
    def get_resources_list(self):
        
        from templates import model_template, schema_template, repository_template, business_logic_template, usecase_template, service_template
        
        self.entity_directory_suffix         = '_entity'
        self.model_module_suffix             = '_model.py'
        self.schema_module_suffix            = '_schema.py'

        self.model_module_template           = model_template
        self.schema_module_template          = schema_template
        
        
        self.repository_directory_suffix     = '_repository'
        self.repository_module_suffix        = '_repository.py'
        self.repository_module_template      = repository_template
        
        
        self.business_logic_directory_suffix = '_business'
        self.business_logic_module_suffix    = '_business_logic.py'
        self.business_logic_module_template  = business_logic_template
                
        
        self.usecase_directory_suffix        = '_usecase'
        self.usecase_module_suffix           = '_usecase.py'
        self.usecase_module_template         = usecase_template
                
                        
        self.service_directory_suffix        = '_service'
        self.service_module_suffix           = '_service.py'
        self.service_module_template         = service_template
        
        self.all_module_templates = [
                                      self.model_module_template, 
                                      self.schema_module_template,
                                      self.repository_module_template, 
                                      self.business_logic_module_template, 
                                      self.usecase_module_template, 
                                      self.service_module_template
                                    ]  
                        
        self.all_base_directories = [
                                      self.entities_directory, 
                                      self.entities_directory,
                                      self.repositories_directory, 
                                      self.business_logic_directory, 
                                      self.usecases_directory, 
                                      self.services_directory
                                    ]   

        self.all_directory_suffixes = [
                                        self.entity_directory_suffix,
                                        self.entity_directory_suffix,
                                        self.repository_directory_suffix,
                                        self.business_logic_directory_suffix,
                                        self.usecase_directory_suffix,               
                                        self.service_directory_suffix            
                                      ]
                        
        self.all_module_suffixes = [
                                    self.model_module_suffix,
                                    self.schema_module_suffix,
                                    self.repository_module_suffix,
                                    self.business_logic_module_suffix,
                                    self.usecase_module_suffix,
                                    self.service_module_suffix
                                   ]

        self.configuration_directories = self.__configurations_directories_list__()
        
        list_of_resources = {

            'entity':{
                'directory_suffixes': [self.entity_directory_suffix] * 2,
                'base_directories':[self.entities_directory] * 2,
                'module_suffixes': [self.model_module_suffix, self.schema_module_suffix],
                'module_template':[self.model_module_template, self.schema_module_template],
                'configuration_directories' : self.configuration_directories
            },
            'model':{
                'directory_suffixes': [self.entity_directory_suffix],
                'base_directories':[self.entities_directory],
                'module_suffixes': [self.model_module_suffix],
                'module_template':[self.model_module_template],
                'configuration_directories' : self.configuration_directories
            },            
            'schema':{
                'directory_suffixes': [self.entity_directory_suffix],
                'base_directories':[self.entities_directory],
                'module_suffixes': [self.schema_module_suffix],
                'module_template':[self.schema_module_template],
                'configuration_directories' : self.configuration_directories
            },
            'interface':{
                'directory_suffixes': [self.repository_directory_suffix, self.business_logic_directory_suffix], 
                'base_directories':[self.repositories_directory, self.business_logic_directory],
                'module_suffixes': [self.repository_module_suffix, self.business_logic_module_suffix],
                'module_template':[self.repository_module_template, self.business_logic_module_template],
                'configuration_directories' : self.configuration_directories
            },            
            'repository':{
                'directory_suffixes': [self.repository_directory_suffix],                
                'base_directories':[self.repositories_directory],
                'module_suffixes': [self.repository_module_suffix],
                'module_template':[self.repository_module_template],
                'configuration_directories' : self.configuration_directories
            },    
            'business':{
                'directory_suffixes': [self.business_logic_directory_suffix],                
                'base_directories':[self.business_logic_directory],
                'module_suffixes': [self.business_logic_module_suffix],
                'module_template':[self.business_logic_module_template],
                'configuration_directories' : self.configuration_directories
            }, 
       
            'usecase':{
                'directory_suffixes': [self.usecase_directory_suffix],
                'base_directories':[self.usecases_directory],
                'module_suffixes': [self.usecase_module_suffix],
                'module_template':[self.usecase_module_template],
                'configuration_directories' : self.configuration_directories
            },    
            'service':{
                'directory_suffixes': [self.service_directory_suffix],
                'base_directories':[self.services_directory],
                'module_suffixes': [self.service_module_suffix],
                'module_template':[self.service_module_template],
                'configuration_directories' : self.configuration_directories
            },  
            'all':{
                'base_directories': self.all_base_directories,
                'directory_suffixes': self.all_directory_suffixes,
                'module_suffixes': self.all_module_suffixes,
                'module_template': self.all_module_templates,
                'configuration_directories' : self.configuration_directories
            },  
        }
        
        return list_of_resources
                 
    def __basics_directories_list__(self):
        
        self.scaffolding_directories_list.extend(self.basic_directory)
        return [self.basic_directory]

    def __configurations_directories_list__(self):
        
        api_type_directory = '/graphql' if self.application_application_type == 'GRAPHQL' else '/rest'
        
        self.configurations_directories = [
                       api_type_directory,
                       '/environment',
                       '/end_points',
                       '/database',
                       '/cors',
                       '/log',
                       '/utils'                     
                       ]
        
        directories = [self.configurations_directory + directory for directory in self.configurations_directories]
        # add configurations_directories_list
        self.scaffolding_directories_list.extend(directories)
        
        return [directory for directory in directories]
        
    def __domain_directories_list__(self):
        
        directories = [
                       self.entities_directory,
                       self.repositories_directory,
                       self.business_logic_directory,
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
      
    def create_init_file(self, directory):
        
        self.create_file(f'{directory}/__init__.py')
          
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
            
            print('----directory', directory)
            #  if the directory is inside the source code folder, creates __init__.py
            if directory.__contains__('/'):
                self.create_init_file(directory)
        
        # add the main module in the root of the project
        self.create_file(f'{self.application_directory_name}/main.py')  

        print('All Directories were created Successfully')
        
    def create_resource(self, resource_type, resource_name, template):
        """_summary_
        Creates every resource python file into folder
        it depends from resource_type

        Args:
            resource_type (_type_): every diferent resource type
            file_name (_type_): name of file to create
        """        
        
        self.create_scaffolding()
        
        if resource_name:
            
            dictionary = self.resources.get(resource_type)
        
            base_directories = dictionary.get('base_directories')
            directory_suffixes =  dictionary.get('directory_suffixes')
            module_suffixes = dictionary.get('module_suffixes')
            resource_name = resource_name
            module_template = dictionary.get('module_template')

            # option if wants to create from template
            if template == 1:
                
                from templates import create_file, rest_template, end_points_template,environment_template, cors_template, database_template, log_template, utils_template
                
                configuration_directories = dictionary.get('configuration_directories')
                
                for directory in configuration_directories:
                    
                    file_name = str(directory).split('/')[-1]
                    
                    file_to_create = f'{directory}/{file_name}_configuration.py'
                    
                    # get the function for processing the template
                    select_template = f'{file_name}_template'
                    
                    # get text from template for create the module, converts string on variable o function using 'locals()' like preffix
                    template_code = locals()[select_template](resource_name)
                
                    print('directory_template', file_to_create, select_template)
                    
                    # creates the file with the content
                    create_file(file=file_to_create, template=template_code)
                            
            for index, directory_value in enumerate(base_directories):
                
                if 'entities' in directory_value:                
                    # crea el nombre del directorio basado en el nombre del archivo
                    directory_value = f'{directory_value}/{resource_name}{directory_suffixes[index]}' 
                    # si los archivos estan dentro de un mismo directorio con nombre unificado
                    from os import makedirs              
                    makedirs(directory_value, exist_ok=True)
                # creates _init_.py file if does not exists into the directory
                self.create_init_file(f'{directory_value}')
                
                # define the file and directory to creates the module
                file_to_create = f'{directory_value}/{resource_name}{module_suffixes[index]}'
                
                # option if wants to create from template
                if template == 1:
                    
                    from templates import create_file
                    
                    # get the function for processing the template
                    select_template = module_template[index]
                    # get text from template for create the module
                    template_code = select_template(resource_name)
                    
                    # creates the file with the content
                    create_file(file=file_to_create, template=template_code)
                else:
                    # create the file into the folder
                    self.create_file(file_to_create)
            
     
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