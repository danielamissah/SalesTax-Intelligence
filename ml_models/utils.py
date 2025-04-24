# utils.py

import matplotlib.pyplot as plt
import seaborn as sns


def plot_regression_metrics(metrics_df):
    """
    Plot regression metrics like R², MAE, RMSE.

    :param metrics_df: DataFrame containing the regression metrics
    """
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    axs[0].bar(metrics_df['Task'], metrics_df['Train_R2'], alpha=0.6, label='Train')
    axs[0].bar(metrics_df['Task'], metrics_df['Test_R2'], alpha=0.6, label='Test')
    axs[0].set_title('R² Score')
    axs[0].legend()

    axs[1].bar(metrics_df['Task'], metrics_df['Train_MAE'], alpha=0.6, label='Train')
    axs[1].bar(metrics_df['Task'], metrics_df['Test_MAE'], alpha=0.6, label='Test')
    axs[1].set_title('MAE')
    axs[1].legend()

    axs[2].bar(metrics_df['Task'], metrics_df['Train_RMSE'], alpha=0.6, label='Train')
    axs[2].bar(metrics_df['Task'], metrics_df['Test_RMSE'], alpha=0.6, label='Test')
    axs[2].set_title('RMSE')
    axs[2].legend()

    plt.suptitle('Regression Metrics Comparison')
    plt.tight_layout()
    plt.show()
