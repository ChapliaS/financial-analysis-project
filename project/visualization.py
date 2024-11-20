import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Візуалізація фінансових показників
def plot_financial_metrics(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['ROA'], label='Фактичний ROA')
    plt.title('Фінансові показники (ROA)')
    plt.xlabel('Дата')
    plt.ylabel('ROA')
    plt.legend()
    plt.show()

# Порівняння прогнозів моделей
def plot_predictions(comparison_df):
    plt.figure(figsize=(10, 6))
    
    # Фактичний ROA
    plt.plot(comparison_df['date'], comparison_df['ROA'], label='Фактичний ROA', color='blue')
    
    # Прогнозований ROA Random Forest
    plt.plot(comparison_df['date'], comparison_df['Predicted ROA (Random Forest)'], label='Прогноз Random Forest', color='green')
    
    # Прогнозований ROA SVM
    plt.plot(comparison_df['date'], comparison_df['Predicted ROA (SVM)'], label='Прогноз SVM', color='red')

    plt.title('Порівняння прогнозів моделей машинного навчання')
    plt.xlabel('Дата')
    plt.ylabel('ROA')
    plt.legend()
    plt.show()

# Візуалізація ліквідності, ROA та заборгованості
def plot_additional_metrics(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['liquidity_ratio'], label='Коефіцієнт ліквідності', color='purple')
    plt.plot(data['date'], data['debt_ratio'], label='Коефіцієнт заборгованості', color='orange')
    plt.title('Фінансові показники: Ліквідність та Заборгованість')
    plt.xlabel('Дата')
    plt.ylabel('Коефіцієнти')
    plt.legend()
    plt.show()


def plot_risk_levels(data):
    risk_levels = data[['date', 'liquidity_ratio', 'ROA', 'debt_ratio']].copy()
    risk_levels['Liquidity Risk'] = risk_levels['liquidity_ratio'].apply(lambda x: 'High' if x < 1.5 else 'Medium' if x < 3 else 'Low')
    risk_levels['ROA Risk'] = risk_levels['ROA'].apply(lambda x: 'High' if x < 0.05 else 'Medium' if x < 0.1 else 'Low')
    risk_levels['Debt Risk'] = risk_levels['debt_ratio'].apply(lambda x: 'High' if x > 0.5 else 'Medium' if x > 0.3 else 'Low')

    plt.figure(figsize=(10, 6))
    sns.heatmap(pd.crosstab(risk_levels['date'], risk_levels['Liquidity Risk'], normalize='index'), cmap='coolwarm')
    plt.title('Liquidity Risk Levels Over Time')
    plt.show()

def plot_decision_comparison(data, X_test, rf_predictions, svm_predictions, decision_support):
    comparison_df = data.loc[X_test.index].copy()
    
    # Додаємо прогнозовані дані
    comparison_df['Predicted ROA (Random Forest)'] = rf_predictions
    comparison_df['Predicted ROA (SVM)'] = svm_predictions
    
    # Створюємо стовпці для гібридних рішень
    hybrid_decisions = []
    for idx, (rf_pred, svm_pred) in enumerate(zip(rf_predictions, svm_predictions)):
        row = data.loc[X_test.index[idx]]
        decisions = decision_support.hybrid_decision(row, rf_pred, svm_pred)
        hybrid_decisions.append("; ".join(decisions))
    
    comparison_df['Hybrid Decision'] = hybrid_decisions
    
    # Побудова графіків
    fig, ax = plt.subplots(figsize=(10, 6))

    # Фактичний ROA
    ax.plot(comparison_df['date'], comparison_df['ROA'], label='Фактичний ROA', color='blue')

    # Прогнозований ROA Random Forest
    ax.plot(comparison_df['date'], comparison_df['Predicted ROA (Random Forest)'], label='Прогноз Random Forest', color='green')

    # Прогнозований ROA SVM
    ax.plot(comparison_df['date'], comparison_df['Predicted ROA (SVM)'], label='Прогноз SVM', color='red')

    # Виведення рішень
    for idx, row in comparison_df.iterrows():
        ax.annotate(f"{row['Hybrid Decision']}", (row['date'], row['ROA']), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8, color='black')

    # Налаштування графіку
    ax.set_title('Порівняння рішень на основі класичної моделі та моделей машинного навчання')
    ax.set_xlabel('Дата')
    ax.set_ylabel('ROA')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_summary_table(summary_table):
    summary_table = summary_table.drop(columns=['Hybrid Decision'])
    
    for col in summary_table.select_dtypes(include=['float', 'int']).columns:
        summary_table[col] = summary_table[col].apply(lambda x: f"{x:.2f}")

    root = tk.Tk()
    root.title("Summary Table")


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


    tree["columns"] = list(summary_table.columns)
    tree["show"] = "headings"


    for col in summary_table.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)


    for _, row in summary_table.iterrows():
        tree.insert("", "end", values=list(row))

    # Запуск головного циклу
    root.mainloop()

