# regression.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def run_regression_task(df, target_column, task_name):
    """
    Perform regression task using Random Forest Regressor.

    :param df: DataFrame containing the dataset
    :param target_column: The target variable column
    :param task_name: Name of the task for reporting
    :return: Dictionary with evaluation metrics
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Identify categorical features
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

    # Preprocessor for categorical features
    preprocessor = ColumnTransformer(transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ], remainder='passthrough')

    # Define pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit model
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    metrics = {
        'Task': task_name,
        'Train_R2': r2_score(y_train, y_train_pred),
        'Test_R2': r2_score(y_test, y_test_pred),
        'Train_MAE': mean_absolute_error(y_train, y_train_pred),
        'Test_MAE': mean_absolute_error(y_test, y_test_pred),
        'Train_RMSE': mean_squared_error(y_train, y_train_pred, squared=False),
        'Test_RMSE': mean_squared_error(y_test, y_test_pred, squared=False),
    }

    return metrics
