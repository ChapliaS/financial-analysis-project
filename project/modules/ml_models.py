from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import time

class MLModels:
    def __init__(self):
        # Створюємо моделі Random Forest і SVM
        self.rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.svm_model = SVR(kernel='rbf')

    # Розділення даних на навчальну та тестову вибірки
    def split_data(self, data, target_column):
        X = data[['total_assets', 'total_liabilities', 'net_income']]
        y = data[target_column]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    # Функція для автоматизованого підбору параметрів для Random Forest
    def tune_random_forest(self, X_train, y_train):
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30]
        }
        grid_search = GridSearchCV(RandomForestRegressor(), param_grid, cv=5, scoring='neg_mean_absolute_error')
        grid_search.fit(X_train, y_train)
        return grid_search.best_estimator_, grid_search.best_params_

    # Функція для автоматизованого підбору параметрів для SVM
    def tune_svm(self, X_train, y_train):
        param_grid = {
            'C': [0.01, 0.1, 1, 10, 100],
            'gamma': [0.001, 0.01, 0.1, 1],
            'kernel': ['rbf', 'linear', 'poly']
        }
        grid_search = GridSearchCV(SVR(), param_grid, cv=5, scoring='neg_mean_absolute_error')
        grid_search.fit(X_train, y_train)
        return grid_search.best_estimator_, grid_search.best_params_

    # Метод для тренування Random Forest
    def train_random_forest(self, X_train, y_train):
        self.rf_model.fit(X_train, y_train)
        return self.rf_model

    # Метод для тренування SVM
    def train_svm(self, X_train, y_train):
        self.svm_model.fit(X_train, y_train)
        return self.svm_model

    # Оцінка моделі за декількома метриками (MAE, MSE, R²)
    def evaluate_model(self, model, X_test, y_test):
        start_time = time.time()
        predictions = model.predict(X_test)
        end_time = time.time()

        mae = mean_absolute_error(y_test, predictions)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        execution_time = end_time - start_time

        return {
            'MAE': mae,
            'MSE': mse,
            'R²': r2,
            'Execution Time (seconds)': execution_time
        }




