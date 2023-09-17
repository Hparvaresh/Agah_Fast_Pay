import pandas as pd
from FPT.logic.preprocess_functions import make_info_table
from FPT.utils.pd_plot import  plot_plotly, plot_plotly_date
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
        info_table = make_info_table()
        
        (
            x_train,
            x_test,
            y_train,
            y_test,
            real_test_target,
            scaler,
        ) = make_feature_custom(info_table)
        
        model = train_model(x_train, y_train, x_test, y_test)
        transformed_y_pred, transformed_y_test = predict_model(
            model, x_test, y_test, scaler, real_test_target
        )

        output_df = pd.DataFrame(
            {"predict": transformed_y_pred, "real": transformed_y_test}
        )

        plot_plotly(output_df)

    def run(self):
        """
        Run the FastPay training logic.
        """
        self.merge_and_train()

if __name__ == "__main__":
    fastpay_logic = FastPayTrainLogic()
    fastpay_logic.run()
