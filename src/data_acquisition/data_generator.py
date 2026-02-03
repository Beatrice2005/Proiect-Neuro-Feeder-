import pandas as pd
import numpy as np
import os

def generate_pet_data(num_records=400): # 400 de inregistrari = 40% din 1000
    np.random.seed(42)
    
    data = []
    for _ in range(num_records):
        # Tip Animal: 0 pentru Caine, 1 pentru Pisica
        animal_type = np.random.choice(['Caine', 'Pisica'])
        
        # Greutate: intre 2kg si 50kg
        weight = round(np.random.uniform(2, 50), 1)
        
        # Varsta: intre 1 si 15 ani
        age = np.random.randint(1, 16)
        
        # Activitate: intre 0.5 si 5 ore pe zi
        activity = round(np.random.uniform(0.5, 5), 1)
        # Formula simplificata: (Greutate * 15) + (Activitate * 10) - (Age * 2)
        if animal_type == 'Caine':
            base_portion = (weight * 18) + (activity * 12) - (age * 1.5)
        else:
            base_portion = (weight * 12) + (activity * 8) - (age * 1.2)
        portion = round(base_portion + np.random.normal(0, 5), 1)
        
        data.append([animal_type, weight, age, activity, portion])

    df = pd.DataFrame(data, columns=['tip_animal', 'greutate', 'varsta', 'activitate', 'portie_recomandata'])
    output_path = 'data/generated/original_contribution_400.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Succes! S-au generat {num_records} inregistrari in {output_path}")

if __name__ == "__main__":
    generate_pet_data()