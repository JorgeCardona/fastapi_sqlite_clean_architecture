import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--creation', type=str, default = None)
parser.add_argument('--name', type=str, default = None)
parser.add_argument('--application_type', type=str, default = 'REST')

args = parser.parse_args()

from resources_generator import CreateResources

resource = str(args.creation).lower()
name = args.name

if  resource == 'scaffolding':
    CreateResources().create_scaffolding()
    
if  resource == 'entity' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'schema' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'model' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
 
if  resource == 'interface' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
       
if  resource == 'repository' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'business' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'usecase' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'service' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'all' and name:
    CreateResources().create_resource(resource_type=resource, file_name=name)
    

# llama al script y le pasa las variables para crear los recursos solicitados
# python aplication_script.py --creation=MODEL --name=deportes
# python aplication_script.py --creation=all --name=gatuno