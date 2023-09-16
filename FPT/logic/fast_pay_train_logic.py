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
        (x_train , x_test , y_train , y_test), scaler, real_col_value = make_feature_custom(merge_df)
        # plot_plotly(merge_df)
        model = train_model( x_train, y_train, x_test  , y_test)
        transformed_y_pred, transformed_y_test = predict_model(model,x_test, y_test, scaler, real_col_value)
        output_df = pd.DataFrame({'predict':transformed_y_pred,
                                   'real':transformed_y_test})

        plot_model_predict(output_df)
        

            
            
    def run(self):
        self.merge_all_tables_in_one()