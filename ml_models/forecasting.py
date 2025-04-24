# forecasting.py

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def time_series_forecasting(df):
    """
    Perform time series forecasting using Holt-Winters Exponential Smoothing model.

    :param df: DataFrame containing the dataset
    """

    df['Quarter Ending'] = pd.to_datetime(df['Quarter Ending'])
    df = df.sort_values('Quarter Ending')

    # Set datetime index
    df.set_index('Quarter Ending', inplace=True)

    # Forecasting Computed_Tax using Holt-Winters
    train = df['Computed Tax'][:-4]
    test = df['Computed Tax'][-4:]

    model = ExponentialSmoothing(train, seasonal='add', seasonal_periods=4)
    fitted_model = model.fit()
    forecast = fitted_model.forecast(steps=4)

    # Combine forecast and test for plotting
    forecast_index = test.index
    forecast_series = pd.Series(forecast, index=forecast_index)

    # Plot forecast
    plot_forecast(train, test, forecast_series)

    # Forecast evaluation metrics
    mae = mean_absolute_error(test, forecast)
    rmse = mean_squared_error(test, forecast, squared=False)
    r2 = r2_score(test, forecast)

    print(f'MAE: {mae:.2f}, RMSE: {rmse:.2f}, R²: {r2:.2f}')


def plot_forecast(train, test, forecast_series):
    """
    Plot the forecast results.

    :param train: Training dataset
    :param test: Test dataset
    :param forecast_series: Forecasted values
    """
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train, label='Train')
    plt.plot(test.index, test, label='Test', color='orange')
    plt.plot(forecast_series.index, forecast_series, label='Forecast', color='green')
    plt.title('Forecast of Computed_Tax')
    plt.xlabel('Date')
    plt.ylabel('Computed_Tax')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
