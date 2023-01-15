from resources_generator import CreateResources

# class for raise custom exception when the Resource type does not exists
class InvalidResourceTypeException(Exception):
    pass

# class for interacting script values with application
class ResourceManager:
    
    def resources_list(self):
        
        return [
                'scaffolding',
                'all',
                'entity', 
                'schema', 
                'model', 
                'interface', 
                'repository', 
                'usecase', 
                'service'            
            ]


    def create_instance(self, main_directory_name, application_type):
        
        return CreateResources(main_directory_name=main_directory_name, application_type=application_type)
    
    
    def generate_resource(self, main_directory_name, application_type, resource_type, resource_name):
        
        resources = self.resources_list()
        
        try:
        
            if str(resource_type).lower() in resources:
            
                application_instance =  self.create_instance(main_directory_name=main_directory_name, application_type=application_type)
                
                execute = application_instance.create_resource(resource_type=resource_type, resource_name=resource_name)
                
                print(f'resource type {resource_type} Created Successfully')
                
            else:
                raise InvalidResourceTypeException
            
        except InvalidResourceTypeException:
            print(f'the resource {resource_type} does not exists, the available resources that are possible creates are {resources}')