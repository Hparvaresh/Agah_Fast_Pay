import pandas as pd
import numpy as np
from FPT.vo.pd_mapping_vo import PDMappingVO

def rename_column(df : pd.DataFrame, old_column_name : str, new_column_name :str) -> pd.DataFrame:
    return df.rename(columns={ old_column_name : new_column_name})

def date_to_string(df : pd.DataFrame,date_column_name : str) -> pd.DataFrame :
    df[date_column_name] = df[date_column_name].apply(lambda x : str(x)[:10])
    return df
    
def sort_base_column(df : pd.DataFrame,sort_column_name : str) -> pd.DataFrame :
    df = df.sort_values(sort_column_name)
    return df.reset_index(drop=True)


def groupby_sum_column(df : pd.DataFrame,groupby_column_name : str, sum_column_name:str):
    return df.groupby(groupby_column_name)[sum_column_name].sum().reset_index()

def manage_money_date(df : pd.DataFrame, date_column:str, sum_output_column:str):
    df = rename_column(df, date_column, PDMappingVO.DATE_COLUMN)
    df = rename_column(df, '', sum_output_column)
    df = date_to_string(df, PDMappingVO.DATE_COLUMN)
    df = groupby_sum_column(df, PDMappingVO.DATE_COLUMN, sum_output_column)
    df = sort_base_column(df, PDMappingVO.DATE_COLUMN)
    return df

def manage_money_title(df : pd.DataFrame,
                       date_column:str,
                       amount_column:str,
                       title_column:str, 
                       sum_output_harmoney_column:str,
                       sum_output_check_column:str,
                       sum_output_fast_pey_column:str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    
    df = rename_column(df, date_column, PDMappingVO.DATE_COLUMN)
    df = date_to_string(df, PDMappingVO.DATE_COLUMN)
    df_payment_check = df[df[title_column] == PDMappingVO.PERSIAN_CHECK]
    df_payment_harmony = df[df[title_column] == PDMappingVO.PERSIAN_HARMONEY]
    df_payment_fastpay = df[df[title_column] == PDMappingVO.PERSIAN_FAST_PAY]
    df_payment_harmony = groupby_sum_column(df_payment_harmony, PDMappingVO.DATE_COLUMN, amount_column)
    df_payment_harmony = rename_column(df_payment_harmony, amount_column, sum_output_harmoney_column)
    df_payment_check = groupby_sum_column(df_payment_check, PDMappingVO.DATE_COLUMN, amount_column)
    df_payment_check = rename_column(df_payment_check, amount_column ,sum_output_check_column)
    df_payment_fastpay = groupby_sum_column(df_payment_fastpay, PDMappingVO.DATE_COLUMN, amount_column)
    df_payment_fastpay = rename_column(df_payment_fastpay, amount_column , sum_output_fast_pey_column)
    return df_payment_harmony, df_payment_check, df_payment_fastpay


    
def merge_list_of_df(dfs_list, 
                     merge_on_column:str,
                     merge_harmony_check_column:str,
                     sum_balance_check:str, 
                     sum_balance_harmony:str) -> pd.DataFrame:
    
    assert len(dfs_list) > 2
    merge_df = dfs_list[0]
    for df in dfs_list[1:]:
        merge_df = pd.merge(merge_df, df , on=merge_on_column, how=PDMappingVO.HOW_MERGE_OUTER)
    merge_df = merge_df.dropna()
    merge_df[merge_harmony_check_column] = list(np.array(merge_df[sum_balance_check].to_list()) + np.array(merge_df[sum_balance_harmony].to_list()) )
    merge_df = merge_df.sort_values(merge_on_column)
    merge_df = merge_df.reset_index(drop=True)
    return merge_df


        

