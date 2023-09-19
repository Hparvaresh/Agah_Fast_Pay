import pandas as pd
from FPT.logic.preprocess_functions import make_info_table
from FPT.utils.pd_plot import  plot_plotly, plot_plotly_date
from FPT.vo.feature_mapping import train_feature_map_ratio, test_feature_map_ratio, train_feature_map_custom, test_feature_map_custom
from FPT.logic.feature_functions import make_feature_custom
from FPT.logic.train_functions import train_model, predict_model

class FastPayTrainLogic:
    """
    FastPayTrainLogic class for merging tables and training a model.
    """

    def __init__(self):
        pass

    def merge_and_train(self):
        """
        Merge tables and train a machine learning model.
        """
        # train_feature_map = train_feature_map_ratio
        # test_feature_map = test_feature_map_ratio
        
        train_feature_map = train_feature_map_custom
        test_feature_map = test_feature_map_custom
        
        merged_df_filled_fast_pay_not_0, merged_df_filled_fast_pay_is_0 = make_info_table()
        
        (
            x_train,
            y_train,
            real_train_target,
            train_scaler,
        ) = make_feature_custom(merged_df_filled_fast_pay_is_0, train_feature_map)
        
        (
            x_test,
            y_test,
            real_test_target,
            test_scaler,
        ) = make_feature_custom(merged_df_filled_fast_pay_not_0, test_feature_map)
        
        model = train_model(x_train, y_train, x_test, y_test, train_feature_map)
        
        transformed_y_pred, transformed_y_test = predict_model(
            model, x_test, y_test,test_feature_map, test_scaler, real_test_target
        )
        output_df = pd.DataFrame(
            {"predict": transformed_y_pred, "real": transformed_y_test}
        )

        plot_plotly(output_df, "predict_output")

    def run(self):
        """
        Run the FastPay training logic.
        """
        self.merge_and_train()

if __name__ == "__main__":
    fastpay_logic = FastPayTrainLogic()
    fastpay_logic.run()
