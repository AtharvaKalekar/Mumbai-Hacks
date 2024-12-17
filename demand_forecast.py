import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def build_linear_regression_model(data):
    X = data[['day_of_week', 'hour', 'is_weekend']]  # Example features
    y = data['sales']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    return model, predictions
