import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configuration.environment.environment_config import Environment

instance = Environment('dev')
get_session = instance.get_session