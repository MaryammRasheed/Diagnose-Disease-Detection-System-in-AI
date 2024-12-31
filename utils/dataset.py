import pandas as pd

def load_symptom_data():
    # Load symptom severity and disease datasets
    symptom_severity = pd.read_csv("datasets/Symptom-severity.csv")
    disease_data = pd.read_csv("datasets/disease_dataset.csv")
    return symptom_severity, disease_data
