def generate_report(rf_results, svm_results, file_name="report.txt"):
    with open(file_name, "w") as report_file:
        report_file.write("Random Forest Results:\n")
        for metric, value in rf_results.items():
            report_file.write(f"{metric}: {value}\n")
        
        report_file.write("\nSVM Results:\n")
        for metric, value in svm_results.items():
            report_file.write(f"{metric}: {value}\n")

        report_file.write("\nRecommendations based on the models:\n")