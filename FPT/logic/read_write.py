import os
import pandas as pd
from FPT.dal.dal import Dal
from test_env import RuntimeConfig
from FPT.logic.pandas_functions import *
from FPT.vo.sql_mapping_vo import SQLMappingVO
from FPT.vo.pd_mapping_vo import PDMappingVO




def read_table_from_db( query:str) -> pd.DataFrame:
    dal = Dal() 
    return dal.read_sql_by_query(query)


def read_table_from_csv (table_path :str) -> pd.DataFrame :
    if os.path.isfile(table_path):
        return pd.read_csv(table_path, index_col=0)
    return pd.DataFrame()


def make_table_path(table_name, suffix_path:str =None):
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), RuntimeConfig.LOCAL_DATA_PATH)
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    if  suffix_path:
        return os.path.join(data_path, table_name + suffix_path +PDMappingVO.SUFFIX_CSV)
    return os.path.join(data_path, table_name +PDMappingVO.SUFFIX_CSV) 

def make_query_select_column_and_sum_groupby(table_name:str,
                                             date_column:str,
                                             sum_column:str,
                                             grpup_column:str) -> str:
    
        return f"{SQLMappingVO.SELECT} {date_column} , {SQLMappingVO.SUM}({sum_column}) {SQLMappingVO.FROM} {table_name} {SQLMappingVO.GROUP_BY} {grpup_column}"
    
    
def make_query_select_from_list(table_name:str,
                                column_list:list) -> str:
    
    item_in_query = " , ".join(column_list)
    return f"{SQLMappingVO.SELECT} {item_in_query} {SQLMappingVO.FROM} {table_name}"


def read_table_custom1(table_name:str,
                       date_column:str,
                       sum_column:str,
                       grpup_column:str,
                       sum_output_column:str):
    
    query = make_query_select_column_and_sum_groupby(table_name,date_column ,sum_column, grpup_column)
    df = read_table_from_db(query)
    
    return df

def read_table_custom2(table_name:str,
                       date_column:str,
                       amount_column:str,
                       title_column:str, 
                       sum_output_harmoney_column:str,
                       sum_output_check_column:str,
                       sum_output_fast_pey_column:str):
    
    table_path = make_table_path(table_name, suffix_path=SQLMappingVO.SUFFIX_ALL)
    table_path = table_path 
    df = read_table_from_csv(table_path)
    if df.empty: 
        query = make_query_select_from_list(table_name,
                                                        [amount_column,
                                                            date_column,
                                                            title_column] )
        
        df = read_table_from_db(query) 
        df.to_csv(table_path)
     
    df_payment_harmony, df_payment_check, df_payment_fastpay = manage_money_title(df, 
                                                                                date_column,
                                                                                amount_column,
                                                                                title_column, sum_output_harmoney_column, sum_output_check_column, sum_output_fast_pey_column
                                                                                )
    return df_payment_harmony, df_payment_check, df_payment_fastpay

def read_dollar():
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), RuntimeConfig.LOCAL_DATA_PATH)
    dollar_path = os.path.join(data_path,RuntimeConfig.DOLLAR_PATH)
    assert os.path.isfile(dollar_path)
    df_dollar = pd.read_csv(dollar_path , delimiter=',')
    dollar_p = list((np.array(df_dollar[PDMappingVO.DOLLAR_OPEN]) + np.array(df_dollar[PDMappingVO.DOLLAR_HIGH]) + np.array(df_dollar[PDMappingVO.DOLLAR_LOW]))/3)
    dollar_date = df_dollar[PDMappingVO.DOLLAR_PER].apply(lambda x : str(x)[:4] + '-' + str(x)[4:6] + '-' + str(x)[6:])
    df_dollar = pd.DataFrame()
    df_dollar[PDMappingVO.DATE_COLUMN] = dollar_date
    df_dollar[PDMappingVO.DOLLAR_VALUE] = dollar_p
    return df_dollar
    
    
def read_index():
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), RuntimeConfig.LOCAL_DATA_PATH)
    index_excel_path = os.path.join(data_path,RuntimeConfig.INDEX_EXCEL_PATH)
    df_index = pd.read_excel(index_excel_path , sheet_name=0)
    df_index[PDMappingVO.DATE_COLUMN] = df_index[PDMappingVO.INDEX_SINCE].apply(lambda x : str(x)[:10])
    df_index = df_index.drop(columns=[PDMappingVO.INDEX_SINCE])
    df_index = df_index.groupby(PDMappingVO.DATE_COLUMN)[PDMappingVO.INDEX_VALUE].mean().reset_index()
    df_index = df_index.rename(columns={PDMappingVO.INDEX_VALUE: PDMappingVO.INDEX_INDEX_VALUE})
    return df_index

def read_IPO():
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), RuntimeConfig.LOCAL_DATA_PATH)
    IPO_excel_path = os.path.join(data_path,RuntimeConfig.INDEX_EXCEL_PATH)
    df_IPO = pd.read_excel(IPO_excel_path , sheet_name=1)
    df_IPO = df_IPO[[PDMappingVO.IPO_NAME , PDMappingVO.INDEX_SINCE]]
    df_IPO[PDMappingVO.DATE_COLUMN] = df_IPO[PDMappingVO.INDEX_SINCE].apply(lambda x : str(x)[:10])
    df_IPO = df_IPO.drop(columns=[PDMappingVO.INDEX_SINCE])
    return df_IPO

    