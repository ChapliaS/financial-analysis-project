from modules.data_preprocessing import DataPreprocessing
from modules.financial_metrics import FinancialMetrics
from modules.ml_models import MLModels
from modules.decision_support import DecisionSupport


# 1. Завантаження та обробка даних
file_path = 'magisterska FINAL COMPOSED/financial_data.csv'
data_preprocessor = DataPreprocessing(file_path)
data = data_preprocessor.clean_data()

# 2. Розрахунок класичних фінансових показників
metrics = FinancialMetrics(data)
financial_metrics = metrics.calculate_all()
print(financial_metrics.head())

# 3. Навчання моделей машинного навчання
ml_models = MLModels()
X_train, X_test, y_train, y_test = ml_models.split_data(data, 'ROA')

# Підбір параметрів для Random Forest
best_rf_model, rf_best_params = ml_models.tune_random_forest(X_train, y_train)
print(f"Найкращі параметри для Random Forest: {rf_best_params}")

# Підбір параметрів для SVM
best_svm_model, svm_best_params = ml_models.tune_svm(X_train, y_train)
print(f"Найкращі параметри для SVM: {svm_best_params}")

# Оцінка моделей з оптимізованими параметрами
rf_results = ml_models.evaluate_model(best_rf_model, X_test, y_test)
svm_results = ml_models.evaluate_model(best_svm_model, X_test, y_test)

# Збереження прогнозованих значень у змінні
rf_predictions = best_rf_model.predict(X_test)
svm_predictions = best_svm_model.predict(X_test)

# Виведення результатів для Random Forest
# print("Random Forest Results:")
# for metric, value in rf_results.items():
#     print(f"{metric}: {value}")

# Виведення результатів для SVM
# print("SVM Results:")
# for metric, value in svm_results.items():
#     print(f"{metric}: {value}")

# 4. Прийняття рішень на основі результатів моделей
decision_support = DecisionSupport(data)
decision_support.make_decisions(X_test, best_rf_model.predict(X_test), best_svm_model.predict(X_test))

# Порівняння прогнозів моделей
comparison_df = data.loc[X_test.index].copy()
comparison_df['Predicted ROA (Random Forest)'] = best_rf_model.predict(X_test)
comparison_df['Predicted ROA (SVM)'] = best_svm_model.predict(X_test)


# Генерація звіту
# generate_report(rf_results, svm_results)

