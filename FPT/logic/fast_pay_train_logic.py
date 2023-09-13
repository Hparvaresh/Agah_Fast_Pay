import pandas as pd
# from gcl.utils.base.singleton import Singleton
from FPT.logic.pandas_functions import *
from FPT.logic.preprocess_functions import *
from FPT.utils.pd_plot import *
from FPT.logic.feature_functions import *
from FPT.logic.train_functions import *

# class FastPayTrainLogic(metaclass=Singleton):
class FastPayTrainLogic():
    def __init__(
        self,
    ) -> None:
        pass
    
    
    def merge_all_tables_in_one(self):
        merge_df = make_info_table()
        # scaled_df = standard_df(merge_df)
        x_train , x_test , y_train , y_test = make_feature_custom(merge_df)
        decision_tree_regression( x_train, y_train, x_test  , y_test)
        linear_regression( x_train, y_train, x_test  , y_test)
        svr( x_train, y_train, x_test  , y_test)
        random_forest_regression( x_train, y_train, x_test  , y_test)
        # plot_plotly(scaled_df)
        

            
            
    def run(self):
        self.merge_all_tables_in_one()