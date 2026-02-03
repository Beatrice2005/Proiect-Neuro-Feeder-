from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd  
import yaml
import os
import smtplib
from email.message import EmailMessage

app = FastAPI()
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL = "beatrixioana@gmail.com" 
SENDER_PASSWORD = "zdbzrogcucigqiro" 

def send_email_notification(recipient_email: str, gramaj: float):
    if not recipient_email:
        return
        
    msg = EmailMessage()
    msg.set_content(f"Buna! Sistemul Neuro-Feeder a calculat portia ideala pentru animalutul tau: {gramaj} grame.")
    msg["Subject"] = "Rezultat Calcul Portie Neuro-Feeder"
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"✓ Email trimis cu succes catre {recipient_email}")
    except Exception as e:
        print(f"X Eroare la trimitere email: {e}")

def load_app_config():
    config_path = "config/optimized_config.yaml"
    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Eroare la incarcarea configuratiei: {e}")
        return {
            "model": {"path": "models/optimized_model.joblib", "scaler_path": "models/scaler.joblib"},
            "logic": {"low_confidence": 0.60}
        }

config = load_app_config()
app.mount("/static", StaticFiles(directory="src/app/static"), name="static")

try:
    model_path = config['model']['path']
    scaler_path = config['model']['scaler_path']
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    print(f"✓ Modelul {model_path} a fost incarcat!")
except Exception as e:
    print(f"Eroare la incarcarea modelelor: {e}")

class InputData(BaseModel):
    tip_animal: str
    greutate: float
    varsta: float
    activitate: float
    email: str = None  

@app.post("/predict")
async def predict(data: InputData, background_tasks: BackgroundTasks):
    try:
        animal_val = 0 if data.tip_animal == 'Caine' else 1
        features = pd.DataFrame([[animal_val, data.greutate, data.varsta, data.activitate]], 
                               columns=['tip_animal', 'greutate', 'varsta', 'activitate'])
        
        # 3. Scalare si Predictie
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)
        gramaj_final = round(float(prediction[0]), 1)
        
        # 4. Validare logica
        if gramaj_final <= 0:
            raise HTTPException(status_code=400, detail="Eroare: Predictie invalida.")
            
        # 5. Trimitere email in fundal
        if data.email and "@" in data.email:
            background_tasks.add_task(send_email_notification, data.email, gramaj_final)
            
        return {
            "portie_recomandata": gramaj_final,
            "status": "success",
            "email_status": "sent" if data.email else "none"
        }
        
    except Exception as e:
        print(f"Eroare inferenta: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_index():
    return FileResponse('src/app/static/Calculate_BMI.html')