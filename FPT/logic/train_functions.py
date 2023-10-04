import numpy as np
import sys
from sklearn.metrics import mean_absolute_error


from FPT.vo.pd_mapping_vo import PDMappingVO
from FPT.vo.models_vo import ModelsVO
# import torch
# from torch.autograd import Variable

# Linear Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor

# Support Vector Machines
from sklearn.svm import SVR
# Nearest Neighbors
from sklearn.neighbors import KNeighborsRegressor

# Tree-Based Models
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor

# Kernel Ridge Regression
from sklearn.kernel_ridge import KernelRidge

# Neural Network-Based Models
from sklearn.neural_network import MLPRegressor

# Ensemble Methods
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor

# Gaussian Processes
from sklearn.gaussian_process import GaussianProcessRegressor


# RANSAC Regressor
from sklearn.linear_model import RANSACRegressor

#classifier
from sklearn.svm import SVC
from xgboost.sklearn import XGBClassifier


def train_model(x_train, y_train, x_test, y_test, feature_map):
    train_model_list = ""
    
    # Find the desired model type in the feature mapping
    for feature_item in feature_map:
        if PDMappingVO.TRAIN_MODEL in feature_item:
            train_model_list = feature_item[PDMappingVO.TRAIN_MODEL]
    
    assert train_model_list != [], PDMappingVO.NO_MODEL_ERR
    best_mae = 9999999999999999999999999
    best_model = None
    for train_model_type in train_model_list:
        # Initialize the chosen regression model based on the mapping
        if train_model_type == ModelsVO.LINEAR_RGRESSION:
            model = LinearRegression()
        elif train_model_type == ModelsVO.DECISON_TREE_REGRESSION:
            model = DecisionTreeRegressor()
        elif train_model_type == ModelsVO.SVR:
            model = SVR()
        elif train_model_type == ModelsVO.RANDOM_FOREST_REGRESSION:
            model = RandomForestRegressor()
        elif train_model_type == ModelsVO.GRADIEN_BOOSTING_REGRESSION:
            model = GradientBoostingRegressor()    
        elif train_model_type == ModelsVO.RIDGE:
            model = Ridge()    
        elif train_model_type == ModelsVO.LASSO:
            model = Lasso()    
        elif train_model_type == ModelsVO.ELASTIC_NET:
            model = ElasticNet()    
        elif train_model_type == ModelsVO.SGD_REGRESSION:
            model = SGDRegressor()    
        elif train_model_type == ModelsVO.K_NEIGHBORS_REGRESSION:
            model = KNeighborsRegressor()    
        elif train_model_type == ModelsVO.KERNEL_RIDGE:
            model = KernelRidge()    
        elif train_model_type == ModelsVO.EXTRACT_TREES_REGRESSOR:
            model = ExtraTreesRegressor()    
        elif train_model_type == ModelsVO.MLP_REGRESSOR:
            model = MLPRegressor()    
        elif train_model_type == ModelsVO.ADA_BOOST_REGRESSOR:
            model = AdaBoostRegressor()    
        elif train_model_type == ModelsVO.BIGGINING_REGRESSOR:
            model = BaggingRegressor()    
        elif train_model_type == ModelsVO.GAUSSIAN_PROCESS_REGRESSOR:
            model = GaussianProcessRegressor()    
        elif train_model_type == ModelsVO.RANSAC_REGRESSOR:
            model = RANSACRegressor()     
        elif train_model_type == ModelsVO.GRADIEN_BOOSTING_REGRESSION:
            model = GradientBoostingRegressor()  
            
        ####start classifiers
        elif train_model_type == ModelsVO.SVC:
            model = SVC()
        elif train_model_type == ModelsVO.XGB_CLASSIFIER:
            model = XGBClassifier()
        else:
            raise ValueError("Invalid model type in feature mapping.")
        
        # Train the regression model
        model.fit(x_train, y_train)

        # Make predictions on the test data and calculate Mean Absolute Error (MAE)
        y_pred = model.predict(x_test)
        mae = mean_absolute_error(y_test, y_pred)
        print(f"{train_model_type} Mean Absolute Error (MAE): {mae:.2f}")
        if mae < best_mae :
            best_mae = mae
            best_model = model
    
    return best_model


def predict_model(model, x_test, y_test, feature_map, scaler=None, real_col_value=None):

    x_test, y_test, real_col_value =  x_test[55:], y_test[55:], real_col_value[55:]
    # Find the increase factor in the feature mapping
    y_pred = model.predict(x_test)
    model_type:str =""
    for item  in feature_map:
        if not PDMappingVO.TYPE in item:
            continue
        if item[PDMappingVO.TYPE] == PDMappingVO.CLASSIFICATION:
            model_type = PDMappingVO.CLASSIFICATION
        elif item[PDMappingVO.TYPE] == PDMappingVO.REGRESSION:
            model_type = PDMappingVO.REGRESSION
        else :
            raise ValueError(PDMappingVO.NO_MODEL_TYPE)
            
    if not isinstance(y_pred, list):
        transformed_y_pred = y_pred.tolist()
    else :
        transformed_y_pred = y_pred
    if model_type == PDMappingVO.REGRESSION:
        if real_col_value:
            transformed_y_pred = (y_pred * np.array(real_col_value[:-1])) + np.array(
                real_col_value[:-1]
            )
            transformed_y_test = (y_test * np.array(real_col_value[:-1])) + np.array(
                real_col_value[:-1]
            )

        elif scaler:
            transformed_y_pred = scaler.inverse_transform([y_pred])
            transformed_y_test = scaler.inverse_transform([y_test])
            transformed_y_test = transformed_y_test[0]
        else:
            raise ValueError(PDMappingVO.NO_TRANSFORM_OBJ)
    if model_type == PDMappingVO.CLASSIFICATION:
        if real_col_value:
            multi_pred = [0 if x == 0 else -0.2 if x==1 else 0.7 for x in y_pred]
            
            transformed_y_pred = (multi_pred * np.array(real_col_value[:-1])) + np.array(
                real_col_value[:-1]
            )
            
            transformed_y_test = (y_test * np.array(real_col_value[:-1])) + np.array(
                real_col_value[:-1]
            )        
    
    return transformed_y_pred, transformed_y_test
