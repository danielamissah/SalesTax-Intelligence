# main.py

from load_data import load_data
from regression import run_regression_task
from clustering import run_clustering
from forecasting import time_series_forecasting
from utils import plot_regression_metrics
import pandas as pd

def main():
    # Load data
    df = load_data('./Quarterly_Retail_Sales_Tax_Data_by_County_and_City.csv')

    # Run regression tasks
    metrics_tax = run_regression_task(df.copy(), 'Computed Tax', 'Predict Computed_Tax')
    metrics_sales = run_regression_task(df.copy(), 'Taxable Sales', 'Predict Taxable_Sales')

    metrics_df = pd.DataFrame([metrics_tax, metrics_sales])

    # Plot regression metrics
    plot_regression_metrics(metrics_df)

    # Run clustering task
    run_clustering(df)

    # Time series forecasting
    time_series_forecasting(df)

if __name__ == '__main__':
    main()
