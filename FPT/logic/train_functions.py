import numpy as np
from sklearn.svm import SVR
from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.vo.feature_mappin import feature_map
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

def train_model(x_train, y_train, x_test, y_test):
    train_model:str = ""
    for feature_item in feature_map:
        if not PDMappingVO.TRAIN_MODEL in feature_item:
            continue 
        train_model = feature_item[PDMappingVO.TRAIN_MODEL]

    if train_model == PDMappingVO.LINEAR_RGRESSION:
        model = LinearRegression()
    if train_model == PDMappingVO.DECISON_TREE_REGRESSION:
        model = DecisionTreeRegressor()
    if train_model == PDMappingVO.SVR:
        model = SVR()
    if train_model == PDMappingVO.RANDOM_FOREST_REGRESSION:
        model = RandomForestRegressor()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"{train_model} Mean Absolute Error (MAE): {mae:.2f}")
    return model




def predict_model(model,x_test, y_test, scaler= None, real_col_value =None):
    increase_factor:float = 1
    for feature_item in feature_map:
        if not PDMappingVO.INCREASE_FACTOR in feature_item:
            continue 
        increase_factor = feature_item[PDMappingVO.INCREASE_FACTOR]


    y_pred = model.predict(x_test)

    if real_col_value:
        transformed_y_pred = (y_pred * np.array(real_col_value[:-1])) + np.array(real_col_value[:-1])
        transformed_y_test = (y_test * np.array(real_col_value[:-1])) + np.array(real_col_value[:-1])

    if scaler:
        transformed_y_pred = scaler.inverse_transform([y_pred])
        transformed_y_test = scaler.inverse_transform([y_test])
    transformed_y_pred = [x * increase_factor  for x in transformed_y_pred[0]]
    transformed_y_test = transformed_y_test [0]
    return transformed_y_pred, transformed_y_test


