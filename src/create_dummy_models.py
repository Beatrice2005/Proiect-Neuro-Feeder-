import joblib
import os
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np

MODEL_PATH = os.path.join("models", "rn_model_untrained.joblib")
SCALER_PATH = os.path.join("models", "scaler.joblib")

os.makedirs("models", exist_ok=True)

dummy_model = MLPRegressor(hidden_layer_sizes=(10, 5), random_state=42, max_iter=1) 
joblib.dump(dummy_model, MODEL_PATH) 
print(f"✅ Scheletul Modelului salvat: {MODEL_PATH}")
dummy_data = np.array([[10, 5, 2], [20, 10, 8]])
scaler = StandardScaler()
scaler.fit(dummy_data) 
joblib.dump(scaler, SCALER_PATH)
print(f"✅ Scheletul Scaler-ului salvat: {SCALER_PATH}")