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
    print('se va a crear SCAFFOLDING')
    CreateResources().create_scaffolding()
    
if  resource == 'entity' and name:
    print('se va a crear ENTITY')
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'schema' and name:
    print('se va a crear SCHEMA')
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'model' and name:
    print('se va a crear MODEL')
    CreateResources().create_resource(resource_type=resource, file_name=name)
 
if  resource == 'interface' and name:
    print('se va a crear INTERFACE')
    CreateResources().create_resource(resource_type=resource, file_name=name)
       
if  resource == 'repository' and name:
    print('se va a crear REPOSITORY')
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'business' and name:
    print('se va a crear BUSINESS')
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'usecase' and name:
    print('se va a crear REPOSITORY')
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'service' and name:
    print('se va a crear BUSINESS')
    CreateResources().create_resource(resource_type=resource, file_name=name)
    
if  resource == 'all' and name:
    print('se va a crear todo')
    CreateResources().create_resource(resource_type=resource, file_name=name)
    

# llama al script y le pasa las variables para crear los recursos solicitados
python aplication_script.py --creation=MODEL --name=deportes
python aplication_script.py --creation=all --name=gatuno