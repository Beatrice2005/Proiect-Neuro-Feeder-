import pandas as pd
import os

def combine_datasets():
    # 1. Incarcam datele generate de tine (400 inregistrari)
    gen_path = 'data/generated/original_contribution_400.csv'
    df_generated = pd.read_csv(gen_path)
    
    # 2. Incarcam datele vechi (cele 600 ramase din raw)
    # Nota: Daca fisierul tau din raw are alt nume, schimba-l aici
    raw_path = 'data/raw/pet_data_raw.csv' 
    if os.path.exists(raw_path):
        df_raw = pd.read_csv(raw_path).head(600)
    else:
        # Daca nu ai fisierul raw, cream unul fictiv pentru a completa pana la 1000
        print("Atentie: Fisierul raw nu a fost gasit. Se genereaza date pentru completare.")
        df_raw = df_generated.copy() # Doar pentru test
        
    # 3. Combinam seturile
    df_final = pd.concat([df_generated, df_raw], ignore_index=True)
    
    # 4. Salvare dataset final pentru antrenare
    output_path = 'data/processed/final_dataset_1000.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_final.to_csv(output_path, index=False)
    
    print(f"Dataset final creat: {output_path}")
    print(f"Total inregistrari: {len(df_final)} (40% originale din generated)")

if __name__ == "__main__":
    combine_datasets()