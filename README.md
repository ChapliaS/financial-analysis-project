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

Before running the project, ensure you have Python installed (>=3.9). Install required libraries using:
```bash
pip install -r requirements.txt
```

## How to Run

To run the project, follow these steps:

1. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

2. Set Up the Virtual Environment
It is recommended to use a virtual environment to avoid conflicts with your system Python setup.
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```
3. Install Required Dependencies
```bash
Install all the necessary Python packages using the requirements.txt file:
pip install -r requirements.txt
```
4. Prepare Input Data
Make sure the financial_data.csv file is placed in the same directory as the project. This file contains the financial data required for the calculations.

5. Run the Scripts
- To calculate financial coefficients and generate visualizations (ROA, Liquidity, Debt Ratio):

```bash
python project/main-1-calc-grph.py
```
ps. to generate graphics uncomment " plot_comparison_graphs(data, results, target_column) #vizualization ". 

- To get decision-making recommendations based on the analyzed data:

```bash
python project/main-2-decisions.py
```
- To compare model accuracy and execution times:

```bash
python project/main-3-comparision.py
```
6. View the Results
Visualizations and outputs will be displayed in the terminal or generated as files in the project directory.

7. Deactivate the Virtual Environment
After running the project, you can deactivate the virtual environment by running:
```bash
deactivate
```


