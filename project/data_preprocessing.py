import pandas as pd

class DataPreprocessing:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def clean_data(self):
        # Очищення даних від пропущених значень
        self.data = self.data.dropna(subset=['total_assets', 'total_liabilities', 'net_income'])
        return self.data

    def get_data(self):
        return self.data
