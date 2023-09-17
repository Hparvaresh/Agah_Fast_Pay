import numpy as np
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.vo.models_vo import ModelsVO
from FPT.vo.feature_mapping import feature_map


def train_model(x_train, y_train, x_test, y_test):
    """
    Train a regression model based on the specified model type in the feature mapping.
    
    Args:
        x_train (numpy.ndarray): Training feature data.
        y_train (numpy.ndarray): Training target data.
        x_test (numpy.ndarray): Testing feature data.
        y_test (numpy.ndarray): Testing target data.
    
    Returns:
        sklearn.base.BaseEstimator: Trained regression model.
    """
    train_model_type = ""
    
    # Find the desired model type in the feature mapping
    for feature_item in feature_map:
        if PDMappingVO.TRAIN_MODEL in feature_item:
            train_model_type = feature_item[PDMappingVO.TRAIN_MODEL]
    
    assert train_model_type != "", PDMappingVO.NO_MODEL_ERR
    
    # Initialize the chosen regression model based on the mapping
    if train_model_type == ModelsVO.LINEAR_RGRESSION:
        model = LinearRegression()
    elif train_model_type == ModelsVO.DECISON_TREE_REGRESSION:
        model = DecisionTreeRegressor()
    elif train_model_type == ModelsVO.SVR:
        model = SVR()
    elif train_model_type == ModelsVO.RANDOM_FOREST_REGRESSION:
        model = RandomForestRegressor()
    else:
        raise ValueError("Invalid model type in feature mapping.")
    
    # Train the regression model
    model.fit(x_train, y_train)

    # Make predictions on the test data and calculate Mean Absolute Error (MAE)
    y_pred = model.predict(x_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"{train_model_type} Mean Absolute Error (MAE): {mae:.2f}")
    
    return model


def predict_model(model, x_test, y_test, scaler=None, real_col_value=None):
    """
    Predict target values using the trained regression model and apply necessary transformations.
    
    Args:
        model (sklearn.base.BaseEstimator): Trained regression model.
        x_test (numpy.ndarray): Testing feature data.
        y_test (numpy.ndarray): Testing target data.
        scaler (sklearn.preprocessing.StandardScaler, optional): Scaler for inverse transformations.
        real_col_value (list, optional): Real column values for additional transformations.
    
    Returns:
        list: Transformed predicted target values.
        numpy.ndarray: Transformed true target values.
    """
    increase_factor = 1
    
    # Find the increase factor in the feature mapping
    for feature_item in feature_map:
        if PDMappingVO.INCREASE_FACTOR in feature_item:
            increase_factor = feature_item[PDMappingVO.INCREASE_FACTOR]

    # Make predictions using the model
    y_pred = model.predict(x_test)

    # Apply transformations based on the provided parameters
    if real_col_value:
        transformed_y_pred = (y_pred * np.array(real_col_value[:-1])) + np.array(
            real_col_value[:-1]
        )
        transformed_y_test = (y_test * np.array(real_col_value[:-1])) + np.array(
            real_col_value[:-1]
        )
        transformed_y_pred = [x * increase_factor for x in transformed_y_pred]

    elif scaler:
        transformed_y_pred = scaler.inverse_transform([y_pred])
        transformed_y_test = scaler.inverse_transform([y_test])
        transformed_y_pred = [x * increase_factor for x in transformed_y_pred[0]]
        transformed_y_test = transformed_y_test[0]
    else:
        raise ValueError(PDMappingVO.NO_TRANSFORM_OBJ)
    
    return transformed_y_pred, transformed_y_test
