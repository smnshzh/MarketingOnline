import sqlmodel
from sqlmodel import Field, Session, SQLModel
from setting import db_params_mysql as dpm
class MySQL:
    def __init__(self, username=dpm["user"], 
                 password=dpm["password"], 
                 server_name=dpm["host"], 
                 database_name=dpm["database"]):
        self.engine = sqlmodel.create_engine(
            f"mysql+pymysql://{username}:{password}@{server_name}/{database_name}"
        )
       

class PostgreSQL:
    def __init__(self, username: str, password: str, server_name: str, database_name: str):
        self.engine = sqlmodel.create_engine(
            f"postgresql+psycopg2://{username}:{password}@{server_name}/{database_name}"
        )

class SQLite:
    def __init__(self, database_name: str):
        self.engine = sqlmodel.create_engine(
            f"sqlite:///{database_name}.db"
        )

class SQLServer:
    def __init__(self, username: str, password: str, server_name: str, database_name: str):
        self.engine = sqlmodel.create_engine(
            f"mssql+pyodbc://{username}:{password}@{server_name}/{database_name}"
        )

class Oracle:
    def __init__(self, username: str, password: str, server_name: str, database_name: str):
        self.engine = sqlmodel.create_engine(
            f"oracle+cx_oracle://{username}:{password}@{server_name}/{database_name}"
        )

class CockroachDB:
    def __init__(self, username: str, password: str, server_name: str, database_name: str):
        self.engine = sqlmodel.create_engine(
            f"cockroachdb+psycopg2://{username}:{password}@{server_name}/{database_name}"
        )

class MariaDB:
    def __init__(self, username: str, password: str, server_name: str, database_name: str):
        self.engine = sqlmodel.create_engine(
            f"mariadb+pymysql://{username}:{password}@{server_name}/{database_name}"
        )



