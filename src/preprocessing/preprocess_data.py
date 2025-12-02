import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

INPUT_DATA_PATH = 'data/raw/raw_data.csv'
OUTPUT_DIR = 'data/'
SCALER_PATH = 'config/StandardScaler.joblib'

def preprocess_and_split():
    print("\n#####################################################")
    print("## 4. Rulare Preprocesare si Structurare (Sectiunea 4) ##")
    print("#####################################################")
    
    try:
        data = pd.read_csv(INPUT_DATA_PATH)
    except FileNotFoundError:
        print(f"Eroare: Fisierul de date brute nu a fost gasit la {INPUT_DATA_PATH}.")
        return

    features = ['greutatea_curenta', 'varsta_animalului', 'orele_de_activitate']
    target = 'grame_hrana_necesare'
    
    X = data[features]
    y = data[target]
        
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42
    )
    
    print(f"\n   -> Training: {len(X_train)} | Validation: {len(X_val)} | Test: {len(X_test)}")
    
    scaler = StandardScaler()
    scaler.fit(X_train)
    
    X_train_scaled = scaler.transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)
    
    joblib.dump(scaler, SCALER_PATH)
    print(f"   -> Salvat: {SCALER_PATH} (StandardScaler)")
    
    def save_set(X_scaled, y_data, name):
        df = pd.DataFrame(X_scaled, columns=features)
        df[target] = y_data.values 
        df.to_csv(os.path.join(OUTPUT_DIR, name, f'{name}_set.csv'), index=False)

    save_set(X_train_scaled, y_train, 'train')
    save_set(X_val_scaled, y_val, 'validation')
    save_set(X_test_scaled, y_test, 'test')
    
    print("\n✅ Toate livrabilele P2 au fost generate si salvate.")

if __name__ == '__main__':
    preprocess_and_split()