# Financial Analysis Project

## Description

This project provides tools for analyzing financial metrics using classical and machine learning models (Random Forest and SVM). It includes:
- **Visualization of financial metrics** (ROA, liquidity ratio, debt ratio) and comparison of prediction accuracy.
- **Decision-making recommendations** based on analyzed metrics.
- **Comparison of model performance** in terms of accuracy and execution speed.

## Project Structure

- **`main-1-calc-grph.py`**: Computes financial metrics and generates visualizations comparing models.
- **`main-2-decisions.py`**: Provides decision-making recommendations based on financial data.
- **`main-3-comparision.py`**: Evaluates model accuracy and performance speed.
- **Modules**:
  - `data_preprocessing.py`: Handles data cleaning and preparation.
  - `financial_metrics.py`: Computes financial ratios (ROA, liquidity ratio, debt ratio).
  - `ml_models.py`: Trains and evaluates Random Forest and SVM models.
  - `decision_support.py`: Integrates model results into decision-making logic.
  - `visualization.py`: Creates charts and graphs for data visualization.

## Requirements

Before running the project, ensure you have Python installed (>=3.7). Install required libraries using:
```bash
pip install -r requirements.txt
