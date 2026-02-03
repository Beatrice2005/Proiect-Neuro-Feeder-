import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DATA_PATH = os.path.join(ROOT_DIR, 'data', 'raw', 'raw_data.csv')
OUTPUT_PLOT_PATH = os.path.join(ROOT_DIR, 'docs', 'simulated_distribution.png')

def generate_plot():
    try:
        df = pd.read_csv(RAW_DATA_PATH)
        
    except FileNotFoundError:
        print(f"EROARE: Nu s-a gasit fisierul {RAW_DATA_PATH}.")
        print("Asigurati-va ca ati rulat generate_raw_data.py inainte.")
        return
    plt.figure(figsize=(10, 6))
    sns.histplot(
        df['grame_hrana_necesare'], 
        bins=30, 
        kde=True, 
        color='#4e342e', 
        edgecolor='black'
    )
    
    median = df['grame_hrana_necesare'].median()
    mean = df['grame_hrana_necesare'].mean()
    
    plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Media: {mean:.1f} grame')
    plt.axvline(median, color='black', linestyle='dashed', linewidth=2, label=f'Mediana: {median:.1f} grame')

    # 3. Personalizarea Vizuala
    plt.title('Distributia Portiei de Hrana (Variabila Tinta)', fontsize=16)
    plt.xlabel('Cantitate Hrana Necesara (Grame)', fontsize=12)
    plt.ylabel('Frecventa Observatiilor', fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    plt.savefig(OUTPUT_PLOT_PATH)
    plt.close()
    
    print(f"✅ Graficul de distributie a fost salvat in: {OUTPUT_PLOT_PATH}")

if __name__ == '__main__':
    generate_plot()