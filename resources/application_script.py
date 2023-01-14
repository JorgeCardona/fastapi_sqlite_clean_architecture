# python .\resources\application_script.py
import argparse
from manager import ResourceManager

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--main_directory_name', type=str, default = 'src')
parser.add_argument('--application_type', type=str, default = 'mix')
parser.add_argument('--application_name', type=str, default = 'clean_architecture')
parser.add_argument('--resource_type', type=str, default = 'all')
parser.add_argument('--resource_name', type=str, default = 'ggg')
parser.add_argument('--template', type=int, default = 1)


args = parser.parse_args()
# capture the value for main directory
main_directory_name = args.main_directory_name
application_type    = args.application_type
application_name    = args.application_name
resource_type       = args.resource_type
resource_name       = args.resource_name
template            = args.template

# create instance for access to methods
resource_manager = ResourceManager()
resource_manager.generate_resource(
                                    main_directory_name=main_directory_name, 
                                    application_type=application_type, 
                                    resource_type=resource_type, 
                                    resource_name=resource_name,
                                    template=template
                                   )

# llama al script y le pasa las variables para crear los recursos solicitados
# python resources/application_script.py --main_directory_name=application --application_type=graphql
# python resources/application_script.py --main_directory_name=felines --application_type=graphql --resource_type=cat