import pandas as pd
import joblib as joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.neural_network import MLPRegressor

csv = pd.read_csv('/Users/i554234/uni/pein/course_project/data/data.csv')
x = csv[['AirTemp', 'Press', 'UMR']]
y = csv[['NO', 'NO2', 'O3', 'RM10']]
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, test_size=0.3, random_state=0)

scaler_x = RobustScaler()
scaler_x.fit(x_train)
x_train_scaled = scaler_x.transform(x_train)
x_test_scaled = scaler_x.transform(x_test)
joblib.dump(scaler_x, 'scaler_x.joblib')

scaler_y = RobustScaler()
scaler_y.fit(y_train)
y_train_scaled = scaler_y.transform(y_train)
y_test_scaled = scaler_y.transform(y_test)
joblib.dump(scaler_y, 'scaler_y.joblib')

mlp = MLPRegressor(max_iter = 1000, verbose=0, n_iter_no_change=17)
mlp.fit(x_train_scaled, y_train_scaled)
joblib.dump(mlp, 'mlp.joblib')

print(mlp.score(x_test_scaled, y_test_scaled))

arr = np.array([[25, 955, 80]])
arr_scaled = scaler_x.transform(arr)
print(mlp.predict(arr_scaled))
