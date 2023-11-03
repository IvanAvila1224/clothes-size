import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from joblib import dump

df = pd.read_csv('data/final_test.csv')


df = df.dropna()

X = df[['weight', 'age', 'height']]
y = df['size']

# Codificar la variable categórica 'size'
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)


regressor = RandomForestRegressor(n_estimators=300,max_depth=50, random_state=0)
regressor.fit(X, y)


dump(regressor, 'model/ropa-size-prediction.joblib')


dump(label_encoder, 'model/label_encoder.joblib')