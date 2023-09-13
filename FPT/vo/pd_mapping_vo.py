
class PDMappingVO():
    DATE_COLUMN: str = "date"
    SUFFIX_CSV:str = ".csv"
    PERSIAN_CHECK:str = "چک"
    PERSIAN_HARMONEY:str =  "هارمونی"
    PERSIAN_FAST_PAY: str = "فست پی"
    HOW_MERGE_OUTER:str = "outer"
    HOW_MERGE_LEFT:str = 'left'
    UPPER_LEFT:str = "upper left"
    DATE_TIME_FORMAT:str = "%Y-%m-%d"
    DOLLAR_OPEN:str = "<Open>"
    DOLLAR_HIGH:str = "<High>" 
    DOLLAR_LOW:str = "<Low>"
    DOLLAR_PER:str = "<Per>"
    DOLLAR_VALUE:str = "dollar_value"
    
    INDEX_SINCE:str = "Since"
    INDEX_VALUE:str = "Value"
    INDEX_INDEX_VALUE:str = "index_value"
    KEEP_COLUMN:str = "keep_column"
    AS_TARGET:str = "as_target"


    
    
    
    BALANCE_TABLE_NAME:str = "CustomerBalance"
    BALANCE_DATE_NAME:str = "StartDate"
    BALANCE_MONEY_NAME:str = "CashBalance"
    BALANCE_MONEY_OUTPUT_NAME:str = "sum_balance"
    
    DEPOSIT_TABLE_NAME:str = "CustomerDeposit"
    DEPOSIT_DATE_NAME:str = "EffectiveDate"
    DEPOSIT_MONEY_NAME:str = "Amount"
    DEPOSIT_MONEY_OUTPUT_NAME:str = "sum_deposit"
    
    PAYMENT_TABLE_NAME:str = "CustomerPayment"
    PAYMENT_DATE_NAME:str = "PaymentDate"
    PAYMENT_MONEY_NAME:str = "Amount"
    PAYMENT_TYPE_TITLE:str ="PaymentTypeTitle"
    PAYMENT_MONEY_OUTPUT_NAME:str = "sum_payment"
    
    SUM_HARMONEY_OUTPUT_NAME:str = "sum_balance_harmony"
    SUM_CHECK_OUTPUT_NAME:str = "sum_balance_check"
    SUM_FAST_PAY_OUTPUT_NAME:str = "sum_balance_fastpay"
    
    SUM_HARMONEY_CHECK:str = 'sum_harmony_check'
    IPO_NAME:str = "Name"
    IPO_TICKET:str = 'is_IPO_ticket'

    RATIO:str = "_ratio_"
    DIVIDE:str = "_divide_"
    COLUMN_NAME:str = "column_name"
    RATIO_PERIODS:str= "ratio_periods"
    DIVIDING:str = "dividing"
    
