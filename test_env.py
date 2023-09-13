# from gcl.utils.config.common_config import CommonsBaseConfig


# class RuntimeConfig(CommonsBaseConfig):
class RuntimeConfig():
    SQL_SERVER_NAME:str = "172.31.35.44"
    SQL_DATABASE_NAME:str = "BiCustomerMoneyConsept"
    SQL_USERNAME:str = "metis_developer"
    SQL_PASSWORD:str =  "340$Uuxwp7Mcxo7Khy"
    LOCAL_DATA_PATH = "local_data"
    
    
    MERGE_TABLE_NAME:str= "merge_table"
    DOLLAR_PATH:str = "Dollar_D.txt"
    INDEX_EXCEL_PATH:str = "metisData.xlsx"