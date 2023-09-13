import numpy as np
from test_env import RuntimeConfig
from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.vo.feature_mappin import feature_map
import pandas as pd


def split_data(x,y, train_size):
    x_train , x_test , y_train , y_test = x[:train_size] , x[train_size:] , y[:train_size] , y[train_size:]
    return  x_train , x_test , y_train , y_test 


def ratio_to_prev(data_df : pd.DataFrame ,feature_df : pd.DataFrame,  column_name :str, period:int = 1) -> pd.DataFrame:
    new_column_name = column_name + PDMappingVO.RATIO+str(period)
    feature_df[new_column_name] =  data_df[column_name].pct_change(periods = period)
    return feature_df, new_column_name

def dividing_two_column(data_df : pd.DataFrame ,feature_df : pd.DataFrame, column1_name :str, column2_name :str)-> pd.DataFrame:
    new_column_name = column1_name + PDMappingVO.DIVIDE + column1_name
    feature_df[new_column_name] =  data_df[[column1_name]].div(data_df[column2_name], axis=0 )
    return feature_df, new_column_name

def make_feature_custom(data_df):
    target_column: str = ""
    feature_df = pd.DataFrame()
    for feature_item in feature_map:
        column_name = feature_item[PDMappingVO.COLUMN_NAME]
        if PDMappingVO.RATIO_PERIODS in feature_item:
            for period in feature_item[ PDMappingVO.RATIO_PERIODS]:
                feature_df, new_column_name = ratio_to_prev(data_df, feature_df,column_name, period )

        if PDMappingVO.DIVIDING in feature_item:
            for divide_column in feature_item[PDMappingVO.DIVIDING]:
                feature_df, new_column_name =  dividing_two_column(data_df, feature_df, column_name, divide_column)

        if PDMappingVO.KEEP_COLUMN in feature_item and feature_item[PDMappingVO.KEEP_COLUMN] :
            new_column_name = column_name
            feature_df[column_name] = data_df[column_name]

        if PDMappingVO.AS_TARGET in feature_item and feature_item[PDMappingVO.AS_TARGET]:
            target_column = new_column_name






    feature_df=feature_df.dropna()

    target_list = feature_df[target_column].to_list()
    feature_df = feature_df.drop(columns = [target_column])
    feature_list = np.array(feature_df)
    x = []
    y = []

    for i in range(48 , len(feature_df)):
        y.append(target_list[i])
        x.append(feature_list[i-1])
        
    return split_data(np.array(x) , np.array(y), train_size = 100)