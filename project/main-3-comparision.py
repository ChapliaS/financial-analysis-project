import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from tkinter import ttk, Tk
import time
import matplotlib.pyplot as plt



# Функція для завантаження даних
def load_data(file_path):
    return pd.read_csv(file_path)


# Функція для обчислення фінансових показників
def calculate_financial_metrics(data):
    data['liquidity_ratio'] = data['current_assets'] / data['current_liabilities']
    data['debt_ratio'] = data['total_liabilities'] / data['total_assets']
    data['ROA'] = data['net_income'] / data['total_assets']
    return data


# Функція для автоматизованого підбору параметрів для Random Forest
def tune_random_forest(X_train, y_train):
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 5, 10, 20, 30, 50]
    }
    grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring='neg_mean_absolute_error')
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_


# Функція для автоматизованого підбору параметрів для SVM
def tune_svm(X_train, y_train):
    param_grid = {
        'C': [0.01, 0.1, 1, 10, 100],
        'gamma': [0.001, 0.01, 0.1, 1],
        'kernel': ['rbf', 'linear', 'poly']
    }
    grid_search = GridSearchCV(SVR(), param_grid, cv=5, scoring='neg_mean_absolute_error')
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_


# Функція для оцінки моделей
def evaluate_model(model, X_train, X_test, y_train, y_test):
    start_time = time.time()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    end_time = time.time()

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    execution_time = end_time - start_time

    return {
        'MAE': round(mae, 4),
        'MSE': round(mse, 4),
        'R²': round(r2, 4),
        'Execution Time (s)': round(execution_time, 4)
    }


# Основна функція для навчання моделей і оцінки
def train_and_evaluate_models(data, target_column):
    X = data[['liquidity_ratio', 'debt_ratio']]
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Підбір параметрів і навчання Random Forest
    print("Підбір параметрів для Random Forest...")
    best_rf_model, rf_params = tune_random_forest(X_train, y_train)
    print(f"Найкращі параметри для Random Forest: {rf_params}")
    rf_results = evaluate_model(best_rf_model, X_train, X_test, y_train, y_test)

    # Підбір параметрів і навчання SVM
    print("Підбір параметрів для SVM...")
    best_svm_model, svm_params = tune_svm(X_train, y_train)
    print(f"Найкращі параметри для SVM: {svm_params}")
    svm_results = evaluate_model(best_svm_model, X_train, X_test, y_train, y_test)

    # Оцінка класичної моделі
    start_time = time.time()
    classical_predictions = [y_train.mean()] * len(y_test)
    end_time = time.time()
    classical_results = {
        'MAE': round(mean_absolute_error(y_test, classical_predictions), 4),
        'MSE': round(mean_squared_error(y_test, classical_predictions), 4),
        'R²': round(r2_score(y_test, classical_predictions), 4),
        'Execution Time (s)': round(end_time - start_time, 4)
    }

    return {
        'classical_results': classical_results,
        'rf_results': rf_results,
        'svm_results': svm_results,
        
    }


# Функція для створення порівняльної таблиці
def generate_comparison_table(results, target_column):
    comparison_data = {
        'Model': ['Classical Model', 'Random Forest', 'SVM'],
        'MAE': [
            results['classical_results']['MAE'],
            results['rf_results']['MAE'],
            results['svm_results']['MAE'],
        ],
        'MSE': [
            results['classical_results']['MSE'],
            results['rf_results']['MSE'],
            results['svm_results']['MSE'],
        ],
        'R²': [
            results['classical_results']['R²'],
            results['rf_results']['R²'],
            results['svm_results']['R²'],
        ],
        'Execution Time (s)': [
            results['classical_results']['Execution Time (s)'],
            results['rf_results']['Execution Time (s)'],
            results['svm_results']['Execution Time (s)'],
        ]
    }
    comparison_df = pd.DataFrame(comparison_data)
    display_table(comparison_df, f"Comparison Table: {target_column}")


# Функція для виведення таблиці через tkinter
def display_table(df, title):
    root = Tk()
    root.title(title)

    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True)

    tree = ttk.Treeview(frame, columns=list(df.columns), show='headings')
    tree.pack(fill='both', expand=True)

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    for index, row in df.iterrows():
        tree.insert('', 'end', values=list(row))

    root.mainloop()



# Основна функція
def main():
    file_path = 'magisterska FINAL COMPOSED/financial_data.csv'

    data = load_data(file_path)
    print("Дані успішно завантажені!")

    data = calculate_financial_metrics(data)

    for target_column in ['ROA', 'liquidity_ratio', 'debt_ratio']:
        print(f"Аналіз для {target_column}...")
        results = train_and_evaluate_models(data, target_column)
        generate_comparison_table(results, target_column)



if __name__ == "__main__":
    main()








