# SalesTax Intelligence

**SalesTax Intelligence** is a comprehensive data analysis and machine learning project designed to analyze and predict sales tax patterns, classify counties or cities based on tax contributions, perform anomaly detection, and cluster counties for segmentation. The project integrates data wrangling, machine learning, and visualization tools like **SQL**, **Power BI**, **Tableau**, **Excel**, and **Streamlit** to deliver actionable insights to stakeholders.

The project includes the following:
- **ETL pipeline** to clean and prepare the data for analysis.
- **Machine Learning models** for regression, classification, clustering, and anomaly detection.
- **Power BI Dashboard** for interactive data visualization.


---

## Features

- **Sales Tax Prediction**: Predicts computed tax values based on taxable sales data using regression models.
- **High/Low Tax Classification**: Classifies counties or cities into high and low tax contributors using classification models.
- **Economic Segmentation**: Clusters counties into distinct groups based on their sales tax data using KMeans clustering.
- **Anomaly Detection**: Identifies suspicious or anomalous tax entries using Isolation Forests.
- **Interactive Dashboard**: Power BI dashboard for visualizing trends, insights, and the results of the machine learning models.
- **Streamlit App**: A web app for running machine learning tasks interactively, demonstrating regression, classification, clustering, and anomaly detection.

---

## Project Overview

This project involves the following steps:
1. **Data Extraction**: Extract data from an Excel sheet containing tax-related information for various counties and cities.
2. **Data Transformation**: Perform data cleaning, transformation, and feature engineering using SQL and Python.
3. **ETL Pipeline**: Implement ETL processes to clean, aggregate, and transform data before loading it into Power BI.
4. **Machine Learning Models**: Develop and train models for tax prediction (regression), classification (tax contributor categories), clustering (economic segmentation), and anomaly detection (suspicious tax entries).
5. **Power BI Dashboard**: Create an interactive dashboard to visualize trends, insights, and the results of the machine learning models.
6. **Streamlit Demo**: Build a Streamlit web app to interactively demonstrate the machine learning models.

---
## 💻 Sample Dashboard Screenshots

Here are some sample screenshots of the Power BI dashboard visualizations:

![KPI Cards for Tax Insights](assets/screenshots/kpi_cards.png)
*Figure 1: KPI Cards for Total Tax, Taxable Sales, and Average Tax per Return.*

![Tax Trend Over Time](assets/screenshots/sales_trend.png)
*Figure 2: Line Chart showing tax trends over time (Month vs Computed Tax)..*

![Product (County/City) Tax Performance](assets/screenshots/product_performance.png)
*Figure 3: Bar Chart comparing tax performance across counties.*


---

## Getting Started

To get started with the project locally, follow these steps:

### Prerequisites

- Python 3.x
- **Pandas**, **Scikit-Learn**, **Matplotlib**, **Seaborn**, **Streamlit**, **Power BI**, and **SQL** should be installed.

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/SalesTax-Intelligence.git
    cd SalesTax-Intelligence
    ```

2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the **SalesTax dataset** (link to your data):

    [Download Dataset](https://catalog.data.gov/dataset/quarterly-retail-sales-tax-data-by-county-and-city)



---

## Project Structure

```bash
SalesTax-Intelligence/
│
├── data/
│   └── sales_tax_data.xlsx          # Raw data used for analysis
│
├── etl/
│   ├── sql_queries.sql             # SQL scripts for data transformations and loading
│   └── preprocess_data.py          # Python script for data preprocessing and transformations
│
├── ml_models/
│   ├── regression_model.py         # Regression model for tax prediction
│   ├── classification_model.py     # Classification model for high/low tax classification
│   ├── clustering_model.py         # KMeans clustering model for segmentation
│   └── anomaly_detection_model.py  # Isolation Forest model for anomaly detection
│
│
├── powerbi_dashboard/
│   └── dashboard.pbix              # Power BI file with interactive visuals
│
└── README.md                       # Project documentation



