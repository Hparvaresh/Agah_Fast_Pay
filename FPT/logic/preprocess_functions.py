from datetime import datetime
from FPT.logic.read_write import *
from test_env import RuntimeConfig
from FPT.logic.pandas_functions import *
from persiantools.jdatetime import JalaliDate
from sklearn.preprocessing import StandardScaler


   
def make_info_table():
    table_path = make_table_path(PDMappingVO.BALANCE_TABLE_NAME)
    balance_df = read_table_from_csv(table_path)
    if balance_df.empty: 
        balance_df = read_table_custom1(table_name= PDMappingVO.BALANCE_TABLE_NAME,
                                                                date_column = PDMappingVO.BALANCE_DATE_NAME,
                                                                sum_column = PDMappingVO.BALANCE_MONEY_NAME,
                                                                grpup_column = PDMappingVO.BALANCE_DATE_NAME,
                                                                sum_output_column = PDMappingVO.BALANCE_MONEY_OUTPUT_NAME)
        balance_df = manage_money_date(balance_df, PDMappingVO.BALANCE_DATE_NAME, PDMappingVO.BALANCE_MONEY_OUTPUT_NAME)
        balance_df.to_csv(table_path)
        
    table_path = make_table_path(PDMappingVO.DEPOSIT_TABLE_NAME)
    deposit_df = read_table_from_csv(table_path)
    if deposit_df.empty:    
        deposit_df =  read_table_custom1(table_name= PDMappingVO.DEPOSIT_TABLE_NAME,
                                                            date_column = PDMappingVO.DEPOSIT_DATE_NAME,
                                                            sum_column = PDMappingVO.DEPOSIT_MONEY_NAME,
                                                            grpup_column = PDMappingVO.DEPOSIT_DATE_NAME,
                                                            sum_output_column = PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME)
        deposit_df = manage_money_date(deposit_df, PDMappingVO.DEPOSIT_DATE_NAME, PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME)
        deposit_df.to_csv(table_path)
        
    table_path = make_table_path(PDMappingVO.PAYMENT_TABLE_NAME)
    payment_df = read_table_from_csv(table_path)
    if payment_df.empty:      
        payment_df =  read_table_custom1(table_name= PDMappingVO.PAYMENT_TABLE_NAME,
                                                            date_column = PDMappingVO.PAYMENT_DATE_NAME,
                                                            sum_column = PDMappingVO.PAYMENT_MONEY_NAME,
                                                            grpup_column = PDMappingVO.PAYMENT_DATE_NAME,
                                                            sum_output_column = PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME)
        payment_df = manage_money_date(payment_df, PDMappingVO.PAYMENT_DATE_NAME, PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME)
        payment_df.to_csv(table_path)
    
    
    df_payment_harmony_path = make_table_path(PDMappingVO.SUM_HARMONEY_OUTPUT_NAME)
    df_payment_harmony= read_table_from_csv(df_payment_harmony_path)
    
    df_payment_check_path = make_table_path(PDMappingVO.SUM_CHECK_OUTPUT_NAME)
    df_payment_check= read_table_from_csv(df_payment_check_path)
    
    df_payment_fastpay_path = make_table_path( PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME)
    df_payment_fastpay= read_table_from_csv(df_payment_fastpay_path)
    
    if df_payment_harmony.empty or df_payment_check.empty or df_payment_fastpay.empty:
        df_payment_harmony, df_payment_check, df_payment_fastpay = read_table_custom2(PDMappingVO.PAYMENT_TABLE_NAME,
                                                                    PDMappingVO.PAYMENT_DATE_NAME, 
                                                                    PDMappingVO.PAYMENT_MONEY_NAME, 
                                                                    PDMappingVO.PAYMENT_TYPE_TITLE,
                                                                    PDMappingVO.SUM_HARMONEY_OUTPUT_NAME,
                                                                    PDMappingVO.SUM_CHECK_OUTPUT_NAME,
                                                                    PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME)
        df_payment_harmony.to_csv(df_payment_harmony_path)
        df_payment_check.to_csv(df_payment_check_path)
        df_payment_fastpay.to_csv(df_payment_fastpay_path)
    
    merge_df_path = make_table_path(RuntimeConfig.MERGE_TABLE_NAME)
    merge_df= read_table_from_csv(merge_df_path)
    
    dollar_df = read_dollar()
    index_df = read_index()
    if merge_df.empty:
        merge_df = merge_list_of_df(  
                                    dfs_list = [payment_df,
                                                deposit_df,
                                                balance_df,
                                                df_payment_harmony,
                                                df_payment_check,
                                                df_payment_fastpay,
                                                index_df,
                                                dollar_df],
                                    merge_on_column = PDMappingVO.DATE_COLUMN,
                                    merge_harmony_check_column = PDMappingVO.SUM_HARMONEY_CHECK,
                                    sum_balance_check = PDMappingVO.SUM_HARMONEY_OUTPUT_NAME,
                                    sum_balance_harmony = PDMappingVO.SUM_CHECK_OUTPUT_NAME,
                                    )
        merge_df.to_csv(merge_df_path)
        
    IPO_df = read_IPO()
    merge_df = pd.merge(merge_df , IPO_df , on=PDMappingVO.DATE_COLUMN ,  how=PDMappingVO.HOW_MERGE_LEFT)
    merge_df = merge_df.fillna(0)
    merge_df[PDMappingVO.IPO_TICKET] = [ x if x==0 else 1 for x in merge_df[PDMappingVO.IPO_NAME].to_list() ]
    merge_df = merge_df.drop(columns=[PDMappingVO.IPO_NAME])
    merge_df[PDMappingVO.DATE_COLUMN] = merge_df.apply(lambda row: JalaliDate(datetime.strptime(row[PDMappingVO.DATE_COLUMN],PDMappingVO.DATE_TIME_FORMAT )), axis=1)
    return merge_df


def standard_df(df:pd.DataFrame) -> pd.DataFrame:
        col_to_exclude = df[PDMappingVO.DATE_COLUMN]
        df = df.drop(PDMappingVO.DATE_COLUMN, axis=1)
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(df)
        scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
        scaled_df[PDMappingVO.DATE_COLUMN] = col_to_exclude.values
        return scaled_df