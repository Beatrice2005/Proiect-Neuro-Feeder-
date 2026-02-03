from sklearn.neural_network import MLPRegressor

def get_nn_model():
    return MLPRegressor(
        hidden_layer_sizes=(128, 64, 32), 
        max_iter=500, 
        activation='relu', 
        solver='adam', 
        early_stopping=True, 
        validation_fraction=0.15, 
        random_state=42
    )