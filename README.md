# 📦 Vendor Invoice Intelligence System
### Freight Cost Prediction & Invoice Risk Flagging

## 📌 Project Overview

The **Vendor Invoice Intelligence System** is an end-to-end Machine Learning project designed to support finance and procurement teams by automating freight cost estimation and identifying potentially risky vendor invoices.

The system uses historical invoice and purchase data to build predictive models that help improve financial monitoring, invoice verification, and operational efficiency.

### 🎯 Business Objectives

**1. Freight Cost Prediction (Regression)**

- Predict expected freight costs for vendor invoices.
- Analyze the relationship between invoice quantity, invoice value, and freight charges.
- Support budgeting and procurement planning.

**2. Invoice Risk Flagging (Classification)**

- Identify potentially abnormal vendor invoices.
- Flag invoices requiring manual approval.
- Improve financial control and reduce potential financial leakage.

## 🗄️ Data Sources

Data is stored in a relational SQLite database (`inventory.db`).

The database includes the following tables:

- `vendor_invoice` – Invoice-level financial and timing data.
- `purchases` – Item-level purchase details.
- `purchase_prices` – Reference purchase prices.
- `begin_inventory` – Beginning inventory snapshots.
- `end_inventory` – Ending inventory snapshots.

SQL aggregation is used to generate invoice-level features.

## 📊 Exploratory Data Analysis (EDA)

EDA focuses on business-driven questions:

- Do flagged invoices have higher financial exposure?
- Does freight scale linearly with quantity?
- Does freight cost depend on invoice value?
- Are there unusual invoice and delivery patterns?
- What is the relationship between invoice quantity and freight charges?

Statistical analysis and visualizations are used to understand the data and identify patterns.

## 🤖 Models Used

### 1. Regression – Freight Cost Prediction

- Linear Regression (Baseline)
- Decision Tree Regressor
- Random Forest Regressor (Final Model)

### 2. Classification – Invoice Risk Flagging

- Logistic Regression (Baseline)
- Decision Tree Classifier
- Random Forest Classifier (Tuned Model)

**Hyperparameter Tuning:** GridSearchCV with F1-score to handle class imbalance.

## 📈 Evaluation Metrics

### Freight Cost Prediction

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

### Invoice Risk Flagging

- Accuracy
- Precision
- Recall
- F1-score
- Classification Report
- Feature Importance Analysis

## 🖥️ End-to-End Application

A Streamlit application demonstrates the complete machine learning pipeline.

**Features:**

- Enter invoice details.
- Predict expected freight costs.
- Flag potentially risky invoices in real time.
- Provide human-readable prediction results.
- Support invoice manual approval decisions.

## 💼 Business Impact

- Improved freight cost forecasting.
- Early identification of potentially abnormal invoices.
- Reduced manual invoice verification effort.
- Better financial monitoring and procurement planning.
- Data-driven vendor invoice approval support.



