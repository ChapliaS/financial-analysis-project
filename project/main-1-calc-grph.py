import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from tkinter import ttk, Tk
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_financial_metrics(data):
    data['liquidity_ratio'] = data['current_assets'] / data['current_liabilities']
    data['debt_ratio'] = data['total_liabilities'] / data['total_assets']
    data['ROA'] = data['net_income'] / data['total_assets']
    return data

# Функція для навчання моделей
def train_models(data, target_column):
    X = data[['liquidity_ratio', 'debt_ratio']]
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_predictions = rf_model.predict(X_test)
    
    # SVM
    svm_model = SVR(kernel='rbf')
    svm_model.fit(X_train, y_train)
    svm_predictions = svm_model.predict(X_test)

    return {
        'X_test': X_test,
        'y_test': y_test,
        'rf_predictions': rf_predictions,
        'svm_predictions': svm_predictions
    }

# Функція для створення таблиці результатів
def generate_summary_table(results, target_column):
    summary_df = pd.DataFrame({
        'Фактичне значення': results['y_test'].values.round(2),
        'Прогноз Random Forest': results['rf_predictions'].round(2),
        'Прогноз SVM': results['svm_predictions'].round(2),
    })
    display_summary_table(summary_df, title=f"Summary Table: {target_column}")

# Функція для виводу таблиці через tkinter
def display_summary_table(summary_df, title="Summary Table"):
    root = Tk()
    root.title(title)

    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True)

    tree_scroll_y = ttk.Scrollbar(frame, orient="vertical")
    tree_scroll_y.pack(side="right", fill="y")

    tree_scroll_x = ttk.Scrollbar(frame, orient="horizontal")
    tree_scroll_x.pack(side="bottom", fill="x")

    tree = ttk.Treeview(frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
    tree.pack(fill="both", expand=True)

    tree_scroll_y.config(command=tree.yview)
    tree_scroll_x.config(command=tree.xview)

    tree["columns"] = list(summary_df.columns)
    tree["show"] = "headings"

    for col in summary_df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)

    for _, row in summary_df.iterrows():
        tree.insert("", "end", values=list(row))

    root.mainloop()


# Функція для побудови графіків
def plot_comparison_graphs(data, results, target_column):
    plt.figure(figsize=(12, 6))
    
    # Фактичні значення (Classical Model)
    plt.plot(data['date'].iloc[results['y_test'].index], results['y_test'].values, label='Класична модель', color='blue')
    
    # Прогнози Random Forest
    plt.plot(data['date'].iloc[results['y_test'].index], results['rf_predictions'], label='Random Forest', color='green')
    
    # Прогнози SVM
    plt.plot(data['date'].iloc[results['y_test'].index], results['svm_predictions'], label='SVM', color='red')
    
    plt.title(f'Порівняння моделей для {target_column}')
    plt.xlabel('Дата')
    plt.ylabel(target_column)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()    

# Основна функція
def main():
    file_path = 'magisterska FINAL COMPOSED/financial_data.csv'  

    # Завантаження даних
    data = load_data(file_path)
    print("Дані успішно завантажені!")

    # Обчислення фінансових показників
    data = calculate_financial_metrics(data)

    # Аналіз для кожного з показників
    for target_column in ['ROA', 'liquidity_ratio', 'debt_ratio']:
        print(f"Аналіз для {target_column}...")
        results = train_models(data, target_column)
        generate_summary_table(results, target_column)
        #plot_comparison_graphs(data, results, target_column) #vizualization

if __name__ == "__main__":
    main()






