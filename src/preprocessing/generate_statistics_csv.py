import pandas as pd
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(current_dir, '..', '..') 

RAW_DATA_PATH = os.path.join(ROOT_DIR, 'data', 'raw', 'raw_data.csv')
OUTPUT_STATS_PATH = os.path.join(ROOT_DIR, 'docs', 'data_statistics.csv')

def generate_statistics():
    try:
        df = pd.read_csv(RAW_DATA_PATH)
        
    except FileNotFoundError:
        print(f"EROARE: Nu s-a gasit fisierul {RAW_DATA_PATH}.")
        print("Asigurati-va ca ati rulat generate_raw_data.py inainte.")
        return
    stats = df.drop(columns=['animal_id']).describe().transpose()
    
    stats = stats.reset_index().rename(columns={'index': 'Caracteristica'})
    stats.to_csv(OUTPUT_STATS_PATH, index=False, float_format='%.3f')
    
    print(f" Tabelul de statistici descriptive a fost salvat in: {OUTPUT_STATS_PATH}")

if __name__ == '__main__':
    generate_statistics()