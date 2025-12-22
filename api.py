from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

MODEL_PATH = os.path.join("models", "rn_model_untrained.joblib")
SCALER_PATH = os.path.join("models", "scaler.joblib")

app = FastAPI(title="Neuro-Feeder SIA - Etapa 4 Schelet")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("INFO: Modelul si Scaler-ul au fost incarcate cu succes.")
except FileNotFoundError:
    print(f"EROARE: Nu s-a gasit modelul sau scaler-ul. Verificati caile: {MODEL_PATH} si {SCALER_PATH}")
    model = None
    scaler = None

class AnimalData(BaseModel):
    greutate_curenta: float
    varsta_animalului: float  
    orele_de_activitate: float

@app.post("/predict_portie")
def predict_portie(data: AnimalData):
    if model is None or scaler is None:
        return {"eroare": "Modelul SIA nu a fost incarcat. Verificati log-ul serverului."}

    input_data = np.array([
        data.greutate_curenta,
        data.varsta_animalului,
        data.orele_de_activitate
    ]).reshape(1, -1)

    scaled_data = scaler.transform(input_data)

    predicted_grams = model.predict(scaled_data)[0]

    return {"portie_grame": float(predicted_grams)}
@app.get("/")
def home():
    return {"status": "Serverul Neuro-Feeder ruleaza! (Verificati /predict_portie pentru inferenta)"}