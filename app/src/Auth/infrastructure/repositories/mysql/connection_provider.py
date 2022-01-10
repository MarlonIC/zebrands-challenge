import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

load_dotenv()
path_connection = 'mysql://{}:{}@{}/{}'.format(
    os.getenv('MYSQL_USERNAME'),
    os.getenv('MYSQL_PASSWORD'),
    os.getenv('MYSQL_HOST'),
    os.getenv('MYSQL_DATABASE')
)
engine = create_engine(
    path_connection,
    isolation_level='READ UNCOMMITTED',
    echo=True,
    poolclass=NullPool
)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
