from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.svm import SVR


def linear_regression(x_train, y_train, x_test, y_test):
    model = LinearRegression()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    y_pred_train = model.predict(x_train)


    mae = mean_absolute_error(y_test, y_pred)

    print(f"LinearRegression Mean Absolute Error (MAE): {mae:.2f}")
    
def decision_tree_regression(x_train, y_train, x_test, y_test):
    model = DecisionTreeRegressor()

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    y_pred_train = model.predict(x_train)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"DecisionTreeRegressor Mean Absolute Error (MAE): {mae:.2f}")
    
def svr(x_train, y_train, x_test, y_test):
    model = SVR()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    y_pred_train = model.predict(x_train)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"SVR Mean Absolute Error (MAE): {mae:.2f}")
    
def random_forest_regression(x_train, y_train, x_test, y_test):
    model = RandomForestRegressor()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    y_pred_train = model.predict(x_train)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"RandomForestRegressor Mean Absolute Error (MAE): {mae:.2f}")
 