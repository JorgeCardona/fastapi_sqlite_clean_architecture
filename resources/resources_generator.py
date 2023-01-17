from resources_components import Resources

class CreateResources:
    
    def __init__(self, main_directory_name, application_type):

        self.application_directory_name = str(main_directory_name).lower()
        self.application_application_type = str(application_type).upper()
                
        resources_instance = Resources(main_directory_name=self.application_directory_name, application_type=self.application_application_type)
        self.complete_directory_list = resources_instance.complete_directory_list
        self.resources = resources_instance.resources           
       

    def create_file(file, template):
        
        with open(file,'w') as escribir:
            escribir.write(template)
        #print(template)
        
    
    def create_file(self, file, template=None):
        
        """_summary_
        create every python module required

        Args:
            file (_type_): name of file to create
            template (_type_): create content into the file using template for it
        """
        
        from os import path

        # if exists file does not replace it
        if not path.exists(file):            
            with open(f'{file}','w') as file_to_create:
                if template:
                    file_to_create.write(template)
              
    def create_init_file(self, directory):
        
        self.create_file(f'{directory}/__init__.py')
          
    def create_scaffolding(self):
        """_summary_

        creates every directory defined for clean architecture
        Returns:
            _type_: successfull mesage
        """
        from os import makedirs

        directories_list = self.complete_directory_list
        
        # get all directories that is necessary creates
        for directory in directories_list:
            
            # creates every directory on the list, if a directory exists ignore creating it
            makedirs(directory, exist_ok=True)
            
            #  if the directory is inside the source code folder, creates __init__.py
            if directory.__contains__('/'):
                self.create_init_file(directory)
        
        # add the main module in the root of the project
        self.create_file(f'{self.application_directory_name}/main.py')  

        print('All Directories were created Successfully')
    
    def create_configuration_files_from_templates(self, resources_dictionary, resource_name):
    
        from templates import core_template, rest_template, end_points_template, environment_template, cors_template, database_template, log_template, swagger_template, utils_template
        
        configuration_directories = resources_dictionary.get('configuration_directories')
        
        for directory in configuration_directories:
            
            file_name = str(directory).split('/')[-1]
            
            file_to_create = f'{directory}/{file_name}_configuration.py'

            if 'end_points' in file_name:
                
                file_to_create = f'{directory}/{resource_name}_{file_name}_configuration.py'
                            
            # get the function for processing the template
            select_template = f'{file_name}_template'
            
            # get text from template for create the module, converts string on variable o function using 'locals()' like preffix
            template_code = locals()[select_template](resource_name)
            
            # creates the file with the content
            self.create_file(file=file_to_create, template=template_code)
            
        print('All Configuration Files has been Created!!!')     
        
    def create_clean_architecture_components_from_template(self, selected_template, resource_name, file_to_create):
        
        # get the function for processing the template
        select_template = selected_template
        # get text from template for create the module
        template_code = select_template(resource_name)
        
        # creates the file with the content
        self.create_file(file=file_to_create, template=template_code)        
                
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

            # option if wants to create resources from template
            if template == 1:
                
                self.create_configuration_files_from_templates(resources_dictionary= dictionary, resource_name=resource_name)
                            
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

                    # get the function for processing the template
                    select_template = module_template[index]
                    # creates, models, schemas, repositories, business_logic, usecases, services using templates                                        
                    self.create_clean_architecture_components_from_template(selected_template=select_template, 
                                                                            resource_name=resource_name, 
                                                                            file_to_create=file_to_create)
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