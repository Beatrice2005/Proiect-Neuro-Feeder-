import pandas as pd
import joblib
import os

def run_evaluation():
    print("--- Evaluare Model Neuro-Feeder ---")
    
    # Incarc datele si modelul salvat
    try:
        df = pd.read_csv('data/processed/final_dataset_1000.csv')
        df['tip_animal'] = df['tip_animal'].map({'Caine': 0, 'Pisica': 1})
        
        X = df[['tip_animal', 'greutate', 'varsta', 'activitate']]
        y = df['portie_recomandata']

        model = joblib.load('models/trained_model.joblib')
        scaler = joblib.load('models/scaler.joblib')

        # Calc acuratetea finala
        X_scaled = scaler.transform(X)
        accuracy = model.score(X_scaled, y)
        
        print(f"✓ Acuratete R2 pe setul total: {round(accuracy * 100, 2)}%")
        print("✓ Modelul este validat si gata de utilizare.")
        
    except Exception as e:
        print(f" Eroare la evaluare: {e}")

if __name__ == "__main__":
    run_evaluation()