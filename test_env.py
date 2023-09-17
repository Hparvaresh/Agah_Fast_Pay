# from gcl.utils.config.common_config import CommonsBaseConfig


# class RuntimeConfig(CommonsBaseConfig):
class RuntimeConfig():
    SQL_SERVER_NAME:str = "172.31.35.44"
    SQL_DATABASE_NAME:str = "BiCustomerMoneyConsept"
    SQL_USERNAME:str = "metis_developer"
    SQL_PASSWORD:str =  "340$Uuxwp7Mcxo7Khy"
    LOCAL_DATA_PATH = "local_data"
    
    
    MERGE_DF_FILLED_FAST_PAY_NOT_0:str = "merged_df_filled_fast_pay_not_0"
    MERGE_DF_FILLED_FAST_PAY_IS_0:str = "merged_df_filled_fast_pay_is_0"
    DOLLAR_PATH:str = "Dollar_D.txt"
    INDEX_EXCEL_PATH:str = "metisData.xlsx"