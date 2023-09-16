import numpy as np
import pandas as pd
from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.vo.feature_mappin import feature_map
from sklearn.preprocessing import StandardScaler


def split_data(x,y, train_size):
    x_train , x_test , y_train , y_test = x[:train_size] , x[train_size:] , y[:train_size] , y[train_size:]
    return  x_train , x_test , y_train , y_test 


def ratio_to_prev(data_df : pd.DataFrame ,feature_df : pd.DataFrame,  column_name :str, period:int = 1) :
    new_column_name = column_name + PDMappingVO.RATIO+str(period)
    real_col_value = data_df[column_name]
    feature_df[new_column_name] =  data_df[column_name].pct_change(periods = period)
    return feature_df, new_column_name, real_col_value

def dividing_two_column(data_df : pd.DataFrame ,feature_df : pd.DataFrame, column1_name :str, column2_name :str):
    new_column_name = column1_name + PDMappingVO.DIVIDE + column2_name
    feature_df[new_column_name] =  data_df[[column1_name]].div(data_df[column2_name], axis=0 )
    return feature_df, new_column_name

def standardized_column(data_df : pd.DataFrame ,feature_df : pd.DataFrame, column1_name :str):
    new_column_name = column1_name + PDMappingVO.standard 
    scaler = StandardScaler()
    scaler.fit(data_df[[column1_name]])
    feature_df[[new_column_name]] = scaler.fit_transform(data_df[[column1_name]])
    return feature_df, new_column_name, scaler


def logarithm_column(data_df : pd.DataFrame ,feature_df : pd.DataFrame, column1_name :str):
    new_column_name = column1_name + PDMappingVO.LOGARITHM 
    feature_df[new_column_name] =  data_df[[column1_name]].apply(lambda x: np.log10(x))
    return feature_df, new_column_name

def make_feature_custom(data_df):
    target_column: str = ""
    scaler_obj = None
    real_col_value = None
    feature_df = pd.DataFrame()
    for feature_item in feature_map:
        if not PDMappingVO.COLUMN_NAME in feature_item:
            continue 
        column_name = feature_item[PDMappingVO.COLUMN_NAME]
        new_scaler_obj = None
        new_real_col_value = None
        if PDMappingVO.GET_RATIO in feature_item:
            for period in feature_item[ PDMappingVO.GET_RATIO]:
                feature_df, new_column_name, new_real_col_value = ratio_to_prev(data_df, feature_df,column_name, period )

        if PDMappingVO.GET_DIVIDE in feature_item:
            for divide_column in feature_item[PDMappingVO.GET_DIVIDE]:
                feature_df, new_column_name =  dividing_two_column(data_df, feature_df, column_name, divide_column)

        if PDMappingVO.GET_LOGARITHM in feature_item and feature_item[PDMappingVO.GET_LOGARITHM]:
            feature_df, new_column_name = logarithm_column(data_df, feature_df,column_name )

        if PDMappingVO.GET_STANDARD in feature_item and feature_item[PDMappingVO.GET_STANDARD]:
            feature_df, new_column_name,new_scaler_obj = standardized_column(data_df, feature_df,column_name )

        if PDMappingVO.KEEP_COLUMN in feature_item and feature_item[PDMappingVO.KEEP_COLUMN] :
            new_column_name = column_name
            feature_df[column_name] = data_df[column_name]

        if PDMappingVO.AS_TARGET in feature_item and feature_item[PDMappingVO.AS_TARGET]:
            target_column = new_column_name
            if new_scaler_obj:
                scaler_obj = new_scaler_obj
            if new_real_col_value:
                real_col_value = new_real_col_value






    feature_df=feature_df.dropna()

    target_list = feature_df[target_column].to_list()
    feature_df = feature_df.drop(columns = [target_column])
    feature_list = np.array(feature_df)
    x = []
    y = []

    for i in range(48 , len(feature_df)):
        y.append(target_list[i])
        x.append(feature_list[i-1])
        
    return split_data(np.array(x) , np.array(y), train_size = 70), scaler_obj, real_col_value