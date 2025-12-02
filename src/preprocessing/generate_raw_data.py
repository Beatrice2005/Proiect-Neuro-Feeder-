import pandas as pd
import numpy as np
import os
NUM_OBSERVATIONS = 15000 
OUTPUT_DIR = 'data/'
RAW_DATA_PATH = os.path.join(OUTPUT_DIR, 'raw', 'raw_data.csv')

os.makedirs(os.path.join(OUTPUT_DIR, 'raw'), exist_ok=True) 

def generate_data(n_samples):
    print(f"-> Generare {n_samples} observatii pentru Neuro-Feeder")
    np.random.seed(42) 

    animal_ids = [f"PET_{i+1:05d}" for i in range(n_samples)] 
    
    weights = np.random.normal(loc=15.0, scale=5.0, size=n_samples)
    weights = np.clip(weights, 5.0, 30.0).round(2)
    
    ages = np.random.uniform(0.5, 12.0, size=n_samples).round(1)
    
    activity = np.random.normal(loc=4.0, scale=2.5, size=n_samples)
    activity = np.clip(activity, 0.5, 12.0).round(1)

    food_grams_base = 80 + (weights * 8) + (activity * 18) - (ages * 2) 
    age_factor = np.where(ages < 1.0, 1.5, np.where(ages > 8.0, 0.9, 1.0))
    food_grams = food_grams_base * age_factor + np.random.normal(0, 15, n_samples)
    food_grams = np.clip(food_grams, 10, 500).round(0)
    
    data = pd.DataFrame({
        'animal_id': animal_ids, 
        'greutatea_curenta': weights,
        'varsta_animalului': ages,
        'orele_de_activitate': activity,
        'grame_hrana_necesare': food_grams
    })
    
    data.to_csv(RAW_DATA_PATH, index=False)
    print(f"   -> Fisierul brut a fost salvat: {RAW_DATA_PATH}")
    return data

def perform_eda(data):
    print("\n\n#####################################################")
    print("## 3. Analiza Exploratorie a Datelor (EDA) - Rezultate ##")
    print("#####################################################")
    
    numerical_data = data.drop(columns=['animal_id']) 
    
    print("\n--- Statistici Descriptive (Medie, Min-Max, Deviatie Standard) ---")
    print(numerical_data.describe().transpose())
    
    print("\n--- Corelatia cu Variabila Tinta ---")
    correlation_matrix = numerical_data.corr(numeric_only=True)
    print("Corelatia variabilelor de intrare cu 'grame_hrana_necesare':")
    print(correlation_matrix['grame_hrana_necesare'].sort_values(ascending=False))
    
    print("\n Generarea datelor si Analiza EDA au fost finalizate.")

if __name__ == '__main__':
    data_df = generate_data(NUM_OBSERVATIONS)
    perform_eda(data_df)
    print(f"\nFisierul RAW a fost salvat in: {RAW_DATA_PATH}")