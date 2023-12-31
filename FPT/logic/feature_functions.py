# Import necessary libraries
import numpy as np
import pandas as pd
import math
from FPT.vo.pd_mapping_vo import PDMappingVO
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from FPT.utils.pd_plot import plot_plotly, plot_plotly_date


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
        real_test_target = real_target[train_size - 1 :]
    return x_train, x_test, y_train, y_test, real_test_target


# Function to calculate the ratio of a column to its previous value
def ratio_to_prev(
    data_df: pd.DataFrame,
    feature_df: pd.DataFrame,
    column_name: str,
    period: int = 1,
    shift: int = 0,
):
    assert period > 0
    assert shift >= 0
    new_column_name = column_name + PDMappingVO.RATIO + str(period) + PDMappingVO.SHIFT + str(shift)
    # ratio_list:list = [None]
    # for i in range(1,len(data_df)):
    #     ratio_list.append((data_df[column_name][i]-data_df[column_name][i-1] )/ data_df[column_name][i-1])
    # feature_df[new_column_name] = ratio_list
    feature_df[new_column_name] = data_df[column_name].pct_change(periods=period)
    feature_df[new_column_name] = feature_df[new_column_name].shift(shift)
    return feature_df, new_column_name


def classify_to_prev(
    data_df: pd.DataFrame,
    feature_df: pd.DataFrame,
    column_name: str,
    lower_upper: list = [-0.25, 0.25],
    shift: int = 0,
):
    
    assert shift >= 0
    new_column_name = column_name + PDMappingVO.CLASSIFY + PDMappingVO.SHIFT + str(shift)
    ratio_list:list = [None]
    for i in range(1,len(data_df)):
        ratio_list.append(2 if ((data_df[column_name][i]-data_df[column_name][i-1] )/ data_df[column_name][i-1]) > lower_upper[1] else 1 if ((data_df[column_name][i]-data_df[column_name][i-1] )/ data_df[column_name][i-1]) < lower_upper[0] else 0)
    feature_df[new_column_name] = ratio_list
    feature_df[new_column_name] = feature_df[new_column_name].shift(shift)
    return feature_df, new_column_name

def get_coef_windows(data_df: pd.DataFrame,
    feature_df: pd.DataFrame,
    column_name: str,
    window:int = 5,
    shift: int = 0,):
    new_column_name = column_name + PDMappingVO.COEF + PDMappingVO.SHIFT + str(shift)
    data_list = data_df[column_name]
    data_list = data_list
    coef_list:list = [None for i in range(window)]
    for i in range(window, len(data_list)):
        x = np.array([i for i in range(window)])
        y = data_list[i- window:i].values.reshape(-1, 1)
        s,i  = np.polyfit(x, y, 1)
        atan = math.atan(s)
        coef_list.append(atan)
    feature_df[new_column_name] = coef_list
    feature_df[new_column_name] = feature_df[new_column_name].shift(shift)
    return feature_df, new_column_name
        
# Function to divide two columns
def dividing_two_column(
    data_df: pd.DataFrame,
    feature_df: pd.DataFrame,
    column1_name: str,
    column2_name: str,
    shift:int = 1
):
    new_column_name = column1_name + PDMappingVO.DIVIDE + column2_name + PDMappingVO.SHIFT + str(shift)
    # div_list:list = []
    # for i in range(len(data_df)):
    #     div_list.append(data_df[column1_name][i]/data_df[column2_name][i])
        
    # feature_df[new_column_name] = div_list
    feature_df[new_column_name] = data_df[[column1_name]].div(
        data_df[column2_name], axis=0
    )
    feature_df[new_column_name] = feature_df[new_column_name].shift(shift)
    return feature_df, new_column_name


# Function to standardize a column
def standardized_column(
    data_df: pd.DataFrame,
    feature_df: pd.DataFrame,
    column1_name: str,
    shift:int = 1
):
    new_column_name = column1_name + PDMappingVO.STANDARD + PDMappingVO.SHIFT + str(shift)
    scaler = StandardScaler()
    scaler.fit(data_df[[column1_name]])
    feature_df[[new_column_name]] = scaler.fit_transform(data_df[[column1_name]])
    feature_df[new_column_name] = feature_df[new_column_name].shift(shift)
    return feature_df, new_column_name, scaler


# Function to take the logarithm of a column
def logarithm_column(
    data_df: pd.DataFrame,
    feature_df: pd.DataFrame,
    column1_name: str,
    shift: int = 1
):
    new_column_name = column1_name + PDMappingVO.LOGARITHM + PDMappingVO.SHIFT + str(shift)
    feature_df[new_column_name] = data_df[[column1_name]].apply(lambda x: np.log10(x))
    feature_df[new_column_name] = feature_df[new_column_name].shift(shift)
    return feature_df, new_column_name


# Main function to create custom features from the data
def make_feature_custom(data_df, feature_map):
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
                for shift in feature_item[PDMappingVO.GET_SHIFT]:
                    feature_df, new_column_name = ratio_to_prev(
                        data_df, feature_df, column_name, period, shift
                    )
                    new_real_col_flag = True

        if PDMappingVO.GET_CLASSIFY in feature_item:
            for shift in feature_item[PDMappingVO.GET_SHIFT]:
                feature_df, new_column_name = classify_to_prev(
                    data_df, feature_df, column_name, feature_item[PDMappingVO.GET_CLASSIFY], shift
                )
                new_real_col_flag = True
        if PDMappingVO.GET_COEF in feature_item:
            for window in feature_item[PDMappingVO.GET_COEF ]:
                for shift in feature_item[PDMappingVO.GET_SHIFT]:
                    feature_df, new_column_name = get_coef_windows(data_df,
                                                                            feature_df,
                                                                            column_name,
                                                                            window,
                                                                            shift)
        # Check if the feature should include divided values
        if PDMappingVO.GET_DIVIDE in feature_item:
            for divide_column in feature_item[PDMappingVO.GET_DIVIDE]:
                for shift in feature_item[PDMappingVO.GET_SHIFT]:
                    feature_df, new_column_name = dividing_two_column(
                        data_df, feature_df, column_name, divide_column, shift
                    )

        # Check if the feature should include logarithmic transformations
        if (PDMappingVO.GET_LOGARITHM in feature_item
            and feature_item[PDMappingVO.GET_LOGARITHM]):
            
            for shift in feature_item[PDMappingVO.GET_SHIFT]:
                feature_df, new_column_name = logarithm_column(
                    data_df, feature_df, column_name, shift
                )

        # Check if the feature should include standardized values
        if (PDMappingVO.GET_STANDARD in feature_item
            and feature_item[PDMappingVO.GET_STANDARD] ):
            for shift in feature_item[PDMappingVO.GET_SHIFT]:
                feature_df, new_column_name, new_scaler_obj = standardized_column(
                    data_df, feature_df, column_name, shift
                )

        # Check if the feature should include the original column
        if (PDMappingVO.KEEP_COLUMN in feature_item
            and feature_item[PDMappingVO.KEEP_COLUMN]):
            
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
    
    #Plot features with pyplot
    for feature_item in feature_map:
        if not PDMappingVO.PLOT_FEATURE in feature_item:
            continue
        if (PDMappingVO.PLOT_FEATURE in feature_item
                and feature_item[PDMappingVO.PLOT_FEATURE] ):
            cols = data_df.columns.difference(['date'])
            sc = StandardScaler()
            df = pd.DataFrame()
            df[cols] = sc.fit_transform(data_df[cols])
            df['date'] = data_df['date']
            plot_plotly_date(df[5:], "standard data")
            plot_plotly_date(data_df[5:], "real data")
            plot_plotly(feature_df[5:], "features")
  
            
    # Prepare the target and feature lists
    target_list = feature_df[target_column].to_list()
    feature_df = feature_df.drop(columns=[target_column])
    real_target: list = []
    if PDMappingVO.REAL_TARGET in feature_df.columns:
        real_target = feature_df[PDMappingVO.REAL_TARGET].to_list()[4:]
        feature_df = feature_df.drop(columns=[PDMappingVO.REAL_TARGET])
    feature_list = np.array(feature_df)

    # Split the data into training and testing sets
    x: list = []
    y: list = []
    for i in range(5, len(feature_df)):
        y.append(target_list[i])
        x.append(feature_list[i])
    return x, y, real_target, scaler_obj
