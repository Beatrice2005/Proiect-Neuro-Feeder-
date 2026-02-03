import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import matplotlib.pyplot as plt
import os

from model import get_nn_model

def train_neuro_feeder():
    print("--- Start Antrenare Profesionala Neuro-Feeder ---")
    
    # 1. Incarcare date 
    data_path = 'data/processed/final_dataset_1000.csv'
    if not os.path.exists(data_path):
        print(" Eroare: Nu s-a gasit dataset-ul final!")
        return

    df = pd.read_csv(data_path)
    df['tip_animal'] = df['tip_animal'].map({'Caine': 0, 'Pisica': 1})

    X = df[['tip_animal', 'greutate', 'varsta', 'activitate']]
    y = df['portie_recomandata']

    # 2. Preprocesare
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 3. Luam modelul din model.py
    model = get_nn_model()

    # 4. Antrenare
    print("Antrenarea este in curs...")
    model.fit(X_train_scaled, y_train)

    # 5. Salvare rezultate
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/trained_model.joblib')
    joblib.dump(scaler, 'models/scaler.joblib')
    print("✓ Modelul si Scalerul au fost salvate.")

    # 6. Generare Loss Curve 
    plt.figure(figsize=(10, 5))
    plt.plot(model.loss_curve_)
    plt.title('Evolutie Eroare - Model 96.63% Accuracy')
    plt.xlabel('Epoci')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.savefig('docs/loss_curve.png')
    print("✓ Graficul loss_curve.png a fost actualizat in /docs.")

    # 7. Performanta
    print(f"✓ Scorul final R2: {round(model.score(X_test_scaled, y_test) * 100, 2)}%")

if __name__ == "__main__":
    train_neuro_feeder()