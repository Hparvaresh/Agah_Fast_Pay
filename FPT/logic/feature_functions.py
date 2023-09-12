import numpy as np
from test_env import RuntimeConfig
from FPT.vo.pd_mapping_vo import PDMappingVO


def split_data(x,y):
    return x[:70] , x[70:] , y[:70] , y[70:]

def make_feature_custom(df):
    sum_deposit = df[PDMappingVO.DEPOSIT_MONEY_OUTPUT_NAME].to_list()
    sum_balance = df[PDMappingVO.BALANCE_MONEY_OUTPUT_NAME].to_list()
    sum_payment = df[PDMappingVO.PAYMENT_MONEY_OUTPUT_NAME].to_list()
    is_IPO_ticket = df[PDMappingVO.IPO_TICKET].to_list()
    dollar = df[PDMappingVO.DOLLAR_VALUE].to_list()
    index = df[PDMappingVO.INDEX_INDEX_VALUE].to_list()
    fast_pay = df[PDMappingVO.SUM_FAST_PAY_OUTPUT_NAME].to_list()

    y_real_Imines1 = []
    x = []
    y = []

    for i in range(48 , len(fast_pay)):
        y_real_Imines1.append(fast_pay[i-1])
        y.append((fast_pay[i] - fast_pay[i-1]) / fast_pay[i-1])
        x.append([ sum_deposit[i-1]/sum_balance[i-1] ,
                sum_payment[i-1]/sum_balance[i-1] ,
                (fast_pay[i-1] - fast_pay[i-2]) / fast_pay[i-2] ,
                (fast_pay[i-2] - fast_pay[i-3]) / fast_pay[i-3] ,
                (fast_pay[i-3] - fast_pay[i-4]) / fast_pay[i-4] ,
                    (dollar[i-1] - dollar[i-2]) / dollar[i-2] ,
                    (index[i-1] - index[i-2]) / index[i-2] ,
                    is_IPO_ticket[i] ])
        
    return split_data(np.array(x) , np.array(y))