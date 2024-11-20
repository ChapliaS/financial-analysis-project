class DecisionSupport:
    def __init__(self, data):
        self.data = data

    def decision_based_on_classical_model(self, row):
        # Прийняття рішень на основі класичної моделі (ліквідність, ROA, заборгованість)
        decisions = []
        
        # Ліквідність
        if row['liquidity_ratio'] < 1.5:
            increase_by = (1.5 - row['liquidity_ratio']) / row['liquidity_ratio'] * 100
            decisions.append(f"Класична модель: Рекомендовано підвищити ліквідність на {increase_by:.2f}%. Рівень ризику: високий.")
        elif row['liquidity_ratio'] < 3:
            increase_by = (3 - row['liquidity_ratio']) / row['liquidity_ratio'] * 100
            decisions.append(f"Класична модель: Рекомендовано переглянути ліквідність (підвищити на {increase_by:.2f}%). Рівень ризику: середній.")
        
        # ROA
        if row['ROA'] < 0.05:
            increase_by = (0.05 - row['ROA']) / row['ROA'] * 100
            decisions.append(f"Класична модель: Рекомендовано підвищити рентабельність активів на {increase_by:.2f}%. Рівень ризику: високий.")
        elif row['ROA'] < 0.10:
            increase_by = (0.10 - row['ROA']) / row['ROA'] * 100
            decisions.append(f"Класична модель: Рекомендовано стежити за рентабельністю активів (підвищити на {increase_by:.2f}%). Рівень ризику: середній.")
        
        # Заборгованість
        if row['debt_ratio'] > 0.5:
            reduce_by = (row['debt_ratio'] - 0.5) / row['debt_ratio'] * 100
            decisions.append(f"Класична модель: Рекомендується зменшити рівень заборгованості на {reduce_by:.2f}%. Рівень ризику: високий.")
        elif row['debt_ratio'] > 0.3:
            reduce_by = (row['debt_ratio'] - 0.3) / row['debt_ratio'] * 100
            decisions.append(f"Класична модель: Рекомендується знизити заборгованість на {reduce_by:.2f}%. Рівень ризику: середній.")
        
        return decisions

    def decision_based_on_ml_models(self, rf_pred, svm_pred):
        # Прийняття рішень на основі моделей машинного навчання
        decisions = []
    
        # Визначаємо поріг для ROA
        threshold = 0.05  # Задаємо поріг як 5%
        
        # Прийняття рішень для Random Forest
        if rf_pred < threshold:
            percentage_increase_rf = ((threshold - rf_pred) / rf_pred) * 100
            decisions.append(f"Random Forest: Прогнозований ROA низький. Рекомендується підвищити на {percentage_increase_rf:.2f}% для зниження ризику.")
        else:
            decisions.append("Random Forest: Прогнозований ROA у нормі.")
        
        # Прийняття рішень для SVM
        if svm_pred < threshold:
            percentage_increase_svm = ((threshold - svm_pred) / svm_pred) * 100
            decisions.append(f"SVM: Прогнозований ROA низький. Рекомендується підвищити на {percentage_increase_svm:.2f}% для зниження ризику.")
        else:
            decisions.append("SVM: Прогнозований ROA у нормі.")
        return decisions

    def assess_predicted_risk(self, rf_pred, svm_pred):
        # Оцінка ризику на основі прогнозів моделей машинного навчання
        predicted_risk = []
        
        # Оцінка ризику за Random Forest
        if rf_pred < 0.05:
            predicted_risk.append('Random Forest: Прогнозований ризик високий.')
        elif rf_pred < 0.1:
            predicted_risk.append('Random Forest: Прогнозований ризик середній.')
        else:
            predicted_risk.append('Random Forest: Прогнозований ризик низький.')
        
        # Оцінка ризику за SVM
        if svm_pred < 0.05:
            predicted_risk.append('SVM: Прогнозований ризик високий.')
        elif svm_pred < 0.1:
            predicted_risk.append('SVM: Прогнозований ризик середній.')
        else:
            predicted_risk.append('SVM: Прогнозований ризик низький.')
        
        return predicted_risk
    

    def analyze_impact_of_metrics(self, row):
        # Вплив ліквідності
        if row['liquidity_ratio'] < 1.5:
            liquidity_impact = 'Ліквідність нижча за норму: високий вплив на ризик.'
        elif row['liquidity_ratio'] < 3:
            liquidity_impact = 'Ліквідність близька до норми: середній вплив на ризик.'
        else:
            liquidity_impact = 'Ліквідність у нормі: низький вплив на ризик.'

        # Вплив рентабельності активів (ROA)
        if row['ROA'] < 0.05:
            roa_impact = 'ROA нижче за норму: високий вплив на ризик.'
        elif row['ROA'] < 0.10:
            roa_impact = 'ROA близька до норми: середній вплив на ризик.'
        else:
            roa_impact = 'ROA у нормі: низький вплив на ризик.'

        # Вплив заборгованості
        if row['debt_ratio'] > 0.5:
            debt_impact = 'Заборгованість перевищує норму: високий вплив на ризик.'
        elif row['debt_ratio'] > 0.3:
            debt_impact = 'Заборгованість близька до норми: середній вплив на ризик.'
        else:
            debt_impact = 'Заборгованість у нормі: низький вплив на ризик.'

        return liquidity_impact, roa_impact, debt_impact
    
    def hybrid_decision(self, row, rf_pred, svm_pred):
        # Гібридне рішення на основі класичної моделі та моделей машинного навчання
        decisions = []
        
        # Класична модель
        if row['liquidity_ratio'] < 1.5:
            decisions.append('Гібридна модель: Рекомендовано підвищити ліквідність. Ризик за класичною моделлю високий.')
        elif row['liquidity_ratio'] < 3:
            decisions.append('Гібридна модель: Рекомендовано переглянути ліквідність. Ризик за класичною моделлю середній.')
        
        if row['ROA'] < 0.05:
            decisions.append('Гібридна модель: Рекомендовано підвищити рентабельність активів. Ризик за класичною моделлю високий.')
        elif row['ROA'] < 0.10:
            decisions.append('Гібридна модель: Рекомендовано стежити за рентабельністю активів. Ризик за класичною моделлю середній.')
            
        if row['debt_ratio'] > 0.5:
            decisions.append('Гібридна модель: Зменшити рівень заборгованості. Ризик за класичною моделлю високий.')
        elif row['debt_ratio'] > 0.3:
            decisions.append('Гібридна модель: Рекомендується знизити заборгованість. Ризик за класичною моделлю середній.')
        
        # Прогнози моделей машинного навчання
        if rf_pred < 0.05:
            decisions.append('Гібридна модель: Прогнозований ROA за Random Forest низький. Можливі ризики в майбутньому.')
        if svm_pred < 0.05:
            decisions.append('Гібридна модель: Прогнозований ROA за SVM низький. Можливі ризики в майбутньому.')

        return decisions if decisions else ['Гібридна модель: Показники в нормі.']

    def make_decisions(self, X_test, rf_predictions, svm_predictions):
        for idx, (rf_pred, svm_pred) in enumerate(zip(rf_predictions, svm_predictions)):
            row = self.data.loc[X_test.index[idx]]
            classical_decisions = self.decision_based_on_classical_model(row)
            ml_decisions = self.decision_based_on_ml_models(rf_pred, svm_pred)
            hybrid_decisions = self.hybrid_decision(row, rf_pred, svm_pred)

            # Аналіз впливу фінансових показників
            liquidity_impact, roa_impact, debt_impact = self.analyze_impact_of_metrics(row)

            # Оцінка прогнозованих ризиків
            predicted_risk = self.assess_predicted_risk(rf_pred, svm_pred)

            # Виведення рішень для кожної моделі
            print(f"Дата: {row['date']}")
            print("Рішення на основі класичної моделі:")
            for decision in classical_decisions:
                print(f"- {decision}")
            print("Рішення на основі моделей машинного навчання:")
            for decision in ml_decisions:
                print(f"- {decision}")
            print("Гібридне рішення (поєднання класичної моделі та прогнозів):")
            for decision in hybrid_decisions:
                print(f"- {decision}")

            # Виведення впливу показників
            print("Аналіз впливу фінансових показників:")
            print(f"- {liquidity_impact}")
            print(f"- {roa_impact}")
            print(f"- {debt_impact}")

            # Виведення прогнозованих ризиків
            print("Прогнозовані ризики на основі моделей машинного навчання:")
            for risk in predicted_risk:
                print(f"- {risk}")

            print('-' * 40)
