import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('docs/optimization', exist_ok=True)
os.makedirs('docs/results', exist_ok=True)

# 1. Grafic comparativ experimente
df_exp = pd.read_csv('results/optimization_experiments.csv')
plt.figure(figsize=(10, 5))
plt.bar(df_exp['Exp#'], df_exp['Accuracy (R2)'], color='skyblue')
plt.axhline(y=0.70, color='r', linestyle='--', label='Target 70%')
plt.title('Comparatie Accuracy (R2) pe Experimente')
plt.ylabel('Scor R2')
plt.savefig('docs/optimization/accuracy_comparison.png')

# 2. Evolutia metricilor Etapa 4 -> 5 -> 6
etaper = ['Etapa 4 (Netratat)', 'Etapa 5 (Antrenat)', 'Etapa 6 (Optimizat)']
accuracy_evol = [0.15, 0.9663, 0.9961] 
plt.figure(figsize=(10, 5))
plt.plot(etaper, accuracy_evol, marker='o', linestyle='-', color='green')
plt.title('Evolutia Performantei Sistemului Neuro-Feeder')
plt.grid(True)
plt.savefig('docs/results/metrics_evolution.png')

print("✓ Graficele comparative au fost salvate in docs/optimization/ si docs/results/")