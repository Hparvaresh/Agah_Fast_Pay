
class SQLMappingVO():
    PREFIX_URL: str = "mssql+pyodbc://"
    SUFFIX_URL:str = "?driver=ODBC+Driver+17+for+SQL+Server"
    SELECT:str = "SELECT"
    SUM:str = "SUM"
    FROM:str = "FROM"
    GROUP_BY:str = "GROUP BY"
    SUFFIX_ALL:str = "_all"
    DELIMITER=','
