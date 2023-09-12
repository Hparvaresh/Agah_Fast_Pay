import pandas as pd
from test_env import RuntimeConfig
from sqlalchemy import create_engine
from FPT.vo.sql_mapping_vo import SQLMappingVO

class FastPayTrainPGDao():
    def __init__(self):
        server_name:str = RuntimeConfig.SQL_SERVER_NAME
        database_name:str = RuntimeConfig.SQL_DATABASE_NAME
        username:str = RuntimeConfig.SQL_USERNAME
        password:str =  RuntimeConfig.SQL_PASSWORD
        connection_string = f"{SQLMappingVO.PREFIX_URL}{username}:{password}@{server_name}/{database_name}{SQLMappingVO.SUFFIX_URL}"
        self.engine = create_engine(connection_string)
    
    def read_sql_by_query(self, query:str) -> pd.DataFrame :
        return pd.read_sql(query, self.engine)
    
        
    