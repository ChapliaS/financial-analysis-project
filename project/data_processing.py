import matplotlib
import pandas as pd
from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
import os
import plotly.express as px

# Очікувані назви колонок
expected_columns = {
    'total_assets': ['total_assets', 'активи', 'assets', 'total'],
    'total_liabilities': ['total_liabilities', 'пасиви', 'liabilities'],
    'net_income': ['net_income', 'чистий прибуток', 'прибуток', 'income']
}

# Функція для завантаження файлів (CSV, Excel, JSON)
def load_data(file):
    if file.filename.endswith('.csv'):
        return pd.read_csv(file)
    elif file.filename.endswith('.xlsx'):
        return pd.read_excel(file)
    elif file.filename.endswith('.json'):
        return pd.read_json(file)
    else:
        raise ValueError('Невідомий формат файлу. Підтримуються тільки .csv, .xlsx, .json')

# Функція для пошуку відповідних колонок за схожістю назв
def find_matching_columns(df):
    matched_columns = {}
    for col in df.columns:
        for key, possible_names in expected_columns.items():
            for name in possible_names:
                if fuzz.ratio(col.lower(), name.lower()) > 80:  # Використовуємо схожість > 80%
                    matched_columns[key] = col
                    break
    return matched_columns

# Функція для аналізу даних після визначення відповідних колонок
def analyze_data(df):
    matched_columns = find_matching_columns(df)

    if 'total_assets' in matched_columns and 'net_income' in matched_columns and 'total_liabilities' in matched_columns:
        total_assets = df[matched_columns['total_assets']].sum()
        net_income = df[matched_columns['net_income']].sum()
        total_liabilities = df[matched_columns['total_liabilities']].sum()

        recommendations = []
        if total_assets < total_liabilities:
            recommendations.append('Зменшити зобов\'язання для покращення ліквідності.')
        if net_income < 0:
            recommendations.append('Розглянути стратегії для збільшення прибутку.')

        return {
            'columns': matched_columns,
            'total_assets': total_assets,
            'net_income': net_income,
            'total_liabilities': total_liabilities,
            'recommendations': recommendations
        }
    else:
        raise ValueError('Не вдалося знайти всі необхідні колонки для аналізу.')

# Функція для побудови статичних графіків фінансових показників
def create_financial_charts(df, matched_columns):
    # Переконайтеся, що папка static існує
    if not os.path.exists('static'):
        os.makedirs('static')

    # Статичний графік активів і пасивів
    plt.figure(figsize=(10, 6))
    plt.plot(df[matched_columns['total_assets']], label='Загальні активи', color='green')
    plt.plot(df[matched_columns['total_liabilities']], label='Загальні пасиви', color='red')
    plt.title('Загальні активи та пасиви')
    plt.xlabel('Час')
    plt.ylabel('Сума')
    plt.legend()
    chart_path = os.path.join('static', 'assets_vs_liabilities.png')
    plt.savefig(chart_path)
    plt.close()

    # Статичний графік чистого прибутку
    plt.figure(figsize=(10, 6))
    plt.plot(df[matched_columns['net_income']], label='Чистий прибуток', color='blue')
    plt.title('Чистий прибуток')
    plt.xlabel('Час')
    plt.ylabel('Прибуток')
    plt.legend()
    chart_path = os.path.join('static', 'net_income.png')
    plt.savefig(chart_path)
    plt.close()




