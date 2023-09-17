# Import necessary libraries
import numpy as np
import pandas as pd
from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.vo.feature_mapping import feature_map
from sklearn.preprocessing import StandardScaler
from FPT.utils.pd_plot import plot_model_predict, plot_plotly

# Function to split data into training and testing sets
def split_data(x, y, real_target=None, train_size=None):
    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = (
        x[:train_size],
        x[train_size:],
        y[:train_size],
        y[train_size:],
    )
    real_test_target: list = []
    if real_target:
        real_test_target = real_target[train_size - 1:]
    return x_train, x_test, y_train, y_test, real_test_target

# Function to calculate the ratio of a column to its previous value
def ratio_to_prev(
    data_df: pd.DataFrame, feature_df: pd.DataFrame, column_name: str, period: int = 1
):
    new_column_name = column_name + PDMappingVO.RATIO + str(period)

    feature_df[new_column_name] = data_df[column_name].pct_change(periods=period)
    return feature_df, new_column_name

# Function to divide two columns
def dividing_two_column(
    data_df: pd.DataFrame,
    feature_df: pd.DataFrame,
    column1_name: str,
    column2_name: str,
):
    new_column_name = column1_name + PDMappingVO.DIVIDE + column2_name
    feature_df[new_column_name] = data_df[[column1_name]].div(
        data_df[column2_name], axis=0
    )
    return feature_df, new_column_name

# Function to standardize a column
def standardized_column(
    data_df: pd.DataFrame, feature_df: pd.DataFrame, column1_name: str
):
    new_column_name = column1_name + PDMappingVO.standard
    scaler = StandardScaler()
    scaler.fit(data_df[[column1_name]])
    feature_df[[new_column_name]] = scaler.fit_transform(data_df[[column1_name]])
    return feature_df, new_column_name, scaler

# Function to take the logarithm of a column
def logarithm_column(
    data_df: pd.DataFrame, feature_df: pd.DataFrame, column1_name: str
):
    new_column_name = column1_name + PDMappingVO.LOGARITHM
    feature_df[new_column_name] = data_df[[column1_name]].apply(lambda x: np.log10(x))
    return feature_df, new_column_name

# Main function to create custom features from the data
# Main function to create custom features from the data
def make_feature_custom(data_df):
    target_column: str = ""
    scaler_obj = None

    feature_df = pd.DataFrame()
    
    # Iterate through each feature item in the feature mapping
    for feature_item in feature_map:
        if not PDMappingVO.COLUMN_NAME in feature_item:
            continue
        column_name = feature_item[PDMappingVO.COLUMN_NAME]
        new_scaler_obj = None
        new_real_col_flag: bool = False
        
        # Check if the feature should include ratio values
        if PDMappingVO.GET_RATIO in feature_item:
            for period in feature_item[PDMappingVO.GET_RATIO]:
                feature_df, new_column_name = ratio_to_prev(
                    data_df, feature_df, column_name, period
                )
                new_real_col_flag = True
        
        # Check if the feature should include divided values
        if PDMappingVO.GET_DIVIDE in feature_item:
            for divide_column in feature_item[PDMappingVO.GET_DIVIDE]:
                feature_df, new_column_name = dividing_two_column(
                    data_df, feature_df, column_name, divide_column
                )
        
        # Check if the feature should include logarithmic transformations
        if (
            PDMappingVO.GET_LOGARITHM in feature_item
            and feature_item[PDMappingVO.GET_LOGARITHM]
        ):
            feature_df, new_column_name = logarithm_column(
                data_df, feature_df, column_name
            )
        
        # Check if the feature should include standardized values
        if (
            PDMappingVO.GET_STANDARD in feature_item
            and feature_item[PDMappingVO.GET_STANDARD]
        ):
            feature_df, new_column_name, new_scaler_obj = standardized_column(
                data_df, feature_df, column_name
            )
        
        # Check if the feature should include the original column
        if (
            PDMappingVO.KEEP_COLUMN in feature_item
            and feature_item[PDMappingVO.KEEP_COLUMN]
        ):
            new_column_name = column_name
            feature_df[column_name] = data_df[column_name]
        
        # Check if the feature should be used as the target column
        if (
            PDMappingVO.AS_TARGET in feature_item
            and feature_item[PDMappingVO.AS_TARGET]
        ):
            target_column = new_column_name
            if new_scaler_obj:
                scaler_obj = new_scaler_obj
            if new_real_col_flag:
                feature_df[PDMappingVO.REAL_TARGET] = data_df[column_name]

    # Remove rows with missing values
    feature_df = feature_df.dropna()

    # Prepare the target and feature lists
    target_list = feature_df[target_column].to_list()
    feature_df = feature_df.drop(columns=[target_column])
    real_target: list = []
    if PDMappingVO.REAL_TARGET in feature_df.columns:
        real_target = feature_df[PDMappingVO.REAL_TARGET].to_list()[48:]
        feature_df = feature_df.drop(columns=[PDMappingVO.REAL_TARGET])
    feature_list = np.array(feature_df)
    
    # Split the data into training and testing sets
    x: list = []
    y: list = []
    for i in range(48, len(feature_df)):
        y.append(target_list[i])
        x.append(feature_list[i - 1])
    x_train, x_test, y_train, y_test, real_test_target = split_data(
        np.array(x), np.array(y), real_target, train_size=70
    )
    
    return x_train, x_test, y_train, y_test, real_test_target, scaler_obj
