# clustering.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def run_clustering(df):
    """
    Perform clustering on the dataset and plot the results.

    :param df: DataFrame containing the dataset
    """
    features = ['Taxable Sales', 'Computed Tax', 'Number of Returns']
    X = df[features].copy()

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # K-Means Clustering
    kmeans = KMeans(n_clusters=4, random_state=0)
    kmeans_labels = kmeans.fit_predict(X_scaled)
    df['KMeans_Cluster'] = kmeans_labels

    # DBSCAN Clustering
    dbscan = DBSCAN(eps=0.8, min_samples=5)
    dbscan_labels = dbscan.fit_predict(X_scaled)
    df['DBSCAN_Cluster'] = dbscan_labels

    # PCA for 2D visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    df['PCA1'] = X_pca[:, 0]
    df['PCA2'] = X_pca[:, 1]

    # Plot clusters
    plot_clusters(df)


def plot_clusters(df):
    """
    Plot the K-Means and DBSCAN clustering results.

    :param df: DataFrame with cluster labels
    """
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='KMeans_Cluster', palette='Set2')
    plt.title('KMeans Clustering')

    plt.subplot(1, 2, 2)
    sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='DBSCAN_Cluster', palette='Set1')
    plt.title('DBSCAN Clustering')

    plt.tight_layout()
    plt.show()
