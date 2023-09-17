from datetime import datetime
from FPT.logic.read_write import (
    make_table_path,
    read_table_from_csv,
    read_table_custom1,
    read_table_custom2,
    read_dollar,
    read_index,
    read_IPO,
)
from test_env import RuntimeConfig
from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.logic.pandas_functions import manage_money_date, merge_list_of_df
import pandas as pd
from persiantools.jdatetime import JalaliDate
from sklearn.preprocessing import StandardScaler


# Function to create an information table by merging various data sources.
def make_info_table():
    # Create a table path for the balance data.
    table_path = make_table_path(PDMappingVO.BALANCE_TABLE_NAME)
    # Read the balance data from CSV file.
    balance_df = read_table_from_csv(table_path)
    # If the balance data is empty, generate and process it.
    if balance_df.empty:
        balance_df = read_table_custom1(
            table_name=PDMappingVO.BALANCE_TABLE_NAME,
            date_column=PDMappingVO.BALANCE_DATE_NAME,
            sum_column=PDMappingVO.BALANCE_MONEY_NAME,
            grpup_column=PDMappingVO.BALANCE_DATE_NAME,
            sum_output_column=PDMappingVO.BALANCE_MONEY_OUTPUT_NAME,
        )
        balance_df = manage_money_date(
            balance_df,
            PDMappingVO.BALANCE_DATE_NAME,
            PDMappingVO.BALANCE_MONEY_OUTPUT_NAME,
        )
        balance_df.to_csv(table_path)

    # Repeat the same process for deposit and payment data.
    table_path = make_table_path(PDMappingVO.DEPOSIT_TABLE_NAME)
    deposit_df = read_table_from_csv(table_path)
    if deposit_df.empty:
        deposit_df = read_table_custom1(
            table_name=PDMappingVO.DEPOSIT_TABLE_NAME,
            date_column=PDMappingVO.DEPOSIT_DATE_NAME,
            sum_column=PDMappingVO.DEPOSIT_MONEY_NAME,
            grpup_column=PDMappingVO.DEPOSIT_DATE_NAME,
            sum_output_column=PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
        )
        deposit_df = manage_money_date(
            deposit_df,
            PDMappingVO.DEPOSIT_DATE_NAME,
            PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME,
        )
        deposit_df.to_csv(table_path)

    table_path = make_table_path(PDMappingVO.PAYMENT_TABLE_NAME)
    payment_df = read_table_from_csv(table_path)
    if payment_df.empty:
        payment_df = read_table_custom1(
            table_name=PDMappingVO.PAYMENT_TABLE_NAME,
            date_column=PDMappingVO.PAYMENT_DATE_NAME,
            sum_column=PDMappingVO.PAYMENT_MONEY_NAME,
            grpup_column=PDMappingVO.PAYMENT_DATE_NAME,
            sum_output_column=PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
        )
        payment_df = manage_money_date(
            payment_df,
            PDMappingVO.PAYMENT_DATE_NAME,
            PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME,
        )
        payment_df.to_csv(table_path)

    # Read and process additional payment data.
    df_payment_harmony_path = make_table_path(PDMappingVO.SUM_HARMONEY_OUTPUT_NAME)
    df_payment_harmony = read_table_from_csv(df_payment_harmony_path)

    df_payment_check_path = make_table_path(PDMappingVO.SUM_CHECK_OUTPUT_NAME)
    df_payment_check = read_table_from_csv(df_payment_check_path)

    df_payment_fastpay_path = make_table_path(PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME)
    df_payment_fastpay = read_table_from_csv(df_payment_fastpay_path)

    if df_payment_harmony.empty or df_payment_check.empty or df_payment_fastpay.empty:
        df_payment_harmony, df_payment_check, df_payment_fastpay = read_table_custom2(
            PDMappingVO.PAYMENT_TABLE_NAME,
            PDMappingVO.PAYMENT_DATE_NAME,
            PDMappingVO.PAYMENT_MONEY_NAME,
            PDMappingVO.PAYMENT_TYPE_TITLE,
            PDMappingVO.SUM_HARMONEY_OUTPUT_NAME,
            PDMappingVO.SUM_CHECK_OUTPUT_NAME,
            PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME,
        )
        df_payment_harmony.to_csv(df_payment_harmony_path)
        df_payment_check.to_csv(df_payment_check_path)
        df_payment_fastpay.to_csv(df_payment_fastpay_path)

    # Read and merge data, including dollar and index data.
    merge_df_path = make_table_path(RuntimeConfig.MERGE_TABLE_NAME)
    merge_df = read_table_from_csv(merge_df_path)

    dollar_df = read_dollar()
    index_df = read_index()
    if merge_df.empty:
        merge_df = merge_list_of_df(
            dfs_list=[
                payment_df,
                deposit_df,
                balance_df,
                df_payment_harmony,
                df_payment_check,
                df_payment_fastpay,
                index_df,
                dollar_df,
            ],
            merge_on_column=PDMappingVO.DATE_COLUMN,
            merge_harmony_check_column=PDMappingVO.SUM_HARMONEY_CHECK,
            sum_balance_check=PDMappingVO.SUM_HARMONEY_OUTPUT_NAME,
            sum_balance_harmony=PDMappingVO.SUM_CHECK_OUTPUT_NAME,
        )
        merge_df.to_csv(merge_df_path)

    # Read IPO data and merge it with the existing data.
    IPO_df = read_IPO()
    merge_df = pd.merge(
        merge_df, IPO_df, on=PDMappingVO.DATE_COLUMN, how=PDMappingVO.HOW_MERGE_LEFT
    )
    merge_df = merge_df.fillna(0)
    merge_df[PDMappingVO.IPO_TICKET] = [
        x if x == 0 else 1 for x in merge_df[PDMappingVO.IPO_NAME].to_list()
    ]
    merge_df = merge_df.drop(columns=[PDMappingVO.IPO_NAME])
    merge_df[PDMappingVO.DATE_COLUMN] = merge_df.apply(
        lambda row: JalaliDate(
            datetime.strptime(
                row[PDMappingVO.DATE_COLUMN], PDMappingVO.DATE_TIME_FORMAT
            )
        ),
        axis=1,
    )
    return merge_df
