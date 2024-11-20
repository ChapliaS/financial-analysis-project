class FinancialMetrics:
    def __init__(self, data):
        self.data = data

    def calculate_liquidity_ratio(self):
        self.data['liquidity_ratio'] = self.data['total_assets'] / self.data['total_liabilities']
    
    def calculate_roa(self):
        self.data['ROA'] = self.data['net_income'] / self.data['total_assets']

    def calculate_debt_ratio(self):
        self.data['debt_ratio'] = self.data['total_liabilities'] / self.data['total_assets']

    def calculate_all(self):
        self.calculate_liquidity_ratio()
        self.calculate_roa()
        self.calculate_debt_ratio()
        return self.data[['liquidity_ratio', 'ROA', 'debt_ratio']]
