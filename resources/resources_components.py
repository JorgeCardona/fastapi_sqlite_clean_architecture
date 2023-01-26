class Resources:
    
    def __init__(self, main_directory_name, application_type):
        
        self.application_directory_name = main_directory_name
        self.application_application_type = application_type

        self.configurations_directory = f'{self.application_directory_name}/configuration'
        self.domain_directory         = f'{self.application_directory_name}/domain'
        self.entities_directory       = f'{self.domain_directory}/entities'
        self.interfaces_directory     = f'{self.domain_directory}/interfaces'
        self.usecases_directory       = f'{self.application_directory_name}/usecases'
        self.services_directory       = f'{self.application_directory_name}/services'
        
        # tiene la informacion de cada carpeta del proyecto
        self.entities_resources       = dict()             
        self.interfaces_resources     = dict()        
        self.use_cases_resources      = dict()
        self.services_resources       = dict()
        self.all_resources_dictionary = dict() 

        # guarda la informacion de los recursos de cada componente
        self.all_base_directories   = list()
        self.all_directory_suffixes = list()
        self.all_module_suffixes    = list()
        self.all_module_templates   = list()
             
        # load all directory names for project
        self.scaffolding_directories_list = self.__scaffolding_directories__()
        
        # dictionary for creates resource
        self.resources = self.get_resources_list()
        
    def __scaffolding_directories__(self):

        self.models_directory         = f'{self.entities_directory}/models'
        self.schemas_directory        = f'{self.entities_directory}/schemas'

        self.repositories_directory   = f'{self.interfaces_directory}/repositories'
        self.business_logic_directory = f'{self.interfaces_directory}/business_logic'
        

        self.basic_directory          = ['test',
                                        'deployment',
                                        'requirements']
        
        # TODO --------- eliminar la linea siguiente, es solo para que no genere otros directorios en las pruebas
        self.basic_directory = []
 
        self.complete_directory_list = [
                                        self.configurations_directory, 
                                        self.entities_directory, 
                                        self.repositories_directory,
                                        self.business_logic_directory, 
                                        self.usecases_directory, 
                                        self.services_directory
                                       ]
        self.complete_directory_list.extend(self.basic_directory)
        
        print('self.complete_directory_list',self.complete_directory_list)
        
        return self.complete_directory_list

    def get_entities_resources(self):
    
        from templates import models_template, schemas_template
        
        self.entity_directory_suffix         = '_entity'
        self.model_module_suffix             = '_model.py'
        self.schema_module_suffix            = '_schema.py'

        self.model_module_template           = models_template
        self.schema_module_template          = schemas_template
        
        self.entity_resources = {
            'entity':{
                'root_path':[self.entities_directory],
                'directory_suffixes': [self.entity_directory_suffix] * 2,
                'base_directories':[self.entities_directory] * 2,
                'module_suffixes': [self.model_module_suffix, self.schema_module_suffix],
                'module_template':[self.model_module_template, self.schema_module_template],
                'configuration_directories' : self.configurations_directory
            },
            'model':{
                'root_path':[self.entities_directory],
                'directory_suffixes': [self.entity_directory_suffix],
                'base_directories':[self.entities_directory],
                'module_suffixes': [self.model_module_suffix],
                'module_template':[self.model_module_template],
                'configuration_directories' : self.configurations_directory
            },            
            'schema':{
                'root_path':[self.entities_directory],
                'directory_suffixes': [self.entity_directory_suffix],
                'base_directories':[self.entities_directory],
                'module_suffixes': [self.schema_module_suffix],
                'module_template':[self.schema_module_template],
                'configuration_directories' : self.configurations_directory
            }            
        }
        
        self.all_resources_dictionary = {**self.all_resources_dictionary, **self.entity_resources}
        return self.entities_resources
        
    def get_interfaces_resources(self):
    
        from templates import repositories_template, business_logic_template
        
        self.repository_directory_suffix     = '_repository'
        self.repository_module_suffix        = '_repository.py'
        self.repository_module_template      = repositories_template
               
        self.business_logic_directory_suffix = '_business_logic'
        self.business_logic_module_suffix    = '_business_logic.py'
        self.business_logic_module_template  = business_logic_template
        
        self.interfaces_resources = { 
            'interface':{
                'root_path':[self.interfaces_directory],
                'directory_suffixes': [self.repository_directory_suffix, self.business_logic_directory_suffix], 
                'base_directories':[self.repositories_directory, self.business_logic_directory],
                'module_suffixes': [self.repository_module_suffix, self.business_logic_module_suffix],
                'module_template':[self.repository_module_template, self.business_logic_module_template],
                'configuration_directories' : self.configurations_directory
            },            
            'repository':{
                'root_path':[self.repositories_directory],
                'directory_suffixes': [self.repository_directory_suffix],                
                'base_directories':[self.repositories_directory],
                'module_suffixes': [self.repository_module_suffix],
                'module_template':[self.repository_module_template],
                'configuration_directories' : self.configurations_directory
            },    
            'business_logic':{
                'root_path':[self.business_logic_directory],
                'directory_suffixes': [self.business_logic_directory_suffix],                
                'base_directories':[self.business_logic_directory],
                'module_suffixes': [self.business_logic_module_suffix],
                'module_template':[self.business_logic_module_template],
                'configuration_directories' : self.configurations_directory
            }
        }
        
        self.all_resources_dictionary = {**self.all_resources_dictionary, **self.interfaces_resources}
        return self.interfaces_resources      
        

    def get_usecases_resources(self):
        
        from templates import usecases_template
        
        self.usecase_directory_suffix        = '_usecase'
        self.usecase_module_suffix           = '_usecase.py'
        self.usecase_module_template         = usecases_template
        
        self.use_cases_resources = {
            'usecase':{
                'root_path':[self.usecases_directory],
                'directory_suffixes': [self.usecase_directory_suffix],
                'base_directories':[self.usecases_directory],
                'module_suffixes': [self.usecase_module_suffix],
                'module_template':[self.usecase_module_template],
                'configuration_directories' : self.configurations_directory
            }     
        }
        
        self.all_resources_dictionary = {**self.all_resources_dictionary, **self.use_cases_resources}
        return self.use_cases_resources

    def get_services_resources(self):
        
        from templates import services_template
        
        self.service_directory_suffix        = '_service'
        self.service_module_suffix           = '_service.py'
        self.service_module_template         = services_template   
        
        self.services_resources = {  
            'service':{
                'root_path':[self.services_directory],
                'directory_suffixes': [self.service_directory_suffix],
                'base_directories':[self.services_directory],
                'module_suffixes': [self.service_module_suffix],
                'module_template':[self.service_module_template],
                'configuration_directories' : [self.services_directory]
            },      
        }
        
        self.all_resources_dictionary = {**self.all_resources_dictionary, **self.services_resources}
        return self.services_resources
    
    def get_all_resources_components(self):

        # load the other resources
        self.get_configuration_resources() 
        self.get_entities_resources()  
        self.get_interfaces_resources()
        self.get_usecases_resources()
        self.get_services_resources()
        
        components = ['model','schema','repository','business_logic','usecase','service']
            
        for directory in components:
            self.all_base_directories.extend(self.all_resources_dictionary.get(directory).get('root_path'))
            self.all_directory_suffixes.extend(self.all_resources_dictionary.get(directory).get('directory_suffixes'))
            self.all_module_suffixes.extend(self.all_resources_dictionary.get(directory).get('module_suffixes'))
            self.all_module_templates.extend(self.all_resources_dictionary.get(directory).get('module_template'))

        self.all_resources = {
            'all':{
                    'base_directories': self.all_base_directories,
                    'directory_suffixes': self.all_directory_suffixes,
                    'module_suffixes': self.all_module_suffixes,
                    'module_template': self.all_module_templates,
                    'configuration_directories' : self.configuration_directories
                  }
        }
        
        self.all_resources_dictionary = {**self.all_resources_dictionary, **self.all_resources}
        
        return self.all_resources
        
    def get_configuration_resources(self):
        
        api_type_directory = '/graphql' if self.application_application_type == 'GRAPHQL' else '/rest' if self.application_application_type == 'REST' else '/mix'
        
        self.configurations_directories = [
                       api_type_directory,
                       '/core',
                       '/environment',
                       '/end_points',
                       '/database',
                       '/cors',
                       '/log',
                       '/swagger',
                       '/utils'                     
                       ]
        
        directories = [self.configurations_directory + directory for directory in self.configurations_directories]
        # add configurations_directories_list
        self.scaffolding_directories_list.extend(directories)
        
        self.configuration_directories = [directory for directory in directories]
        
        return self.configuration_directories
    
                
    def get_resources_list(self):
                             
        self.get_all_resources_components()
        
        list_of_resources = dict()
        components = ['entity','model','schema','interface','repository','business_logic','usecase','service','all']
        
        # creates a dictionary with all key:value for resources
        for resource in components:            
            list_of_resources[resource] = self.all_resources_dictionary.get(resource)
            
        return list_of_resources