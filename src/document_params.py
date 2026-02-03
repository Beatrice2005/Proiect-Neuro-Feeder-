import pandas as pd
import os

def generate_parameter_csv():
    parameters = {
        'Parametru': [
            'NUMAR_OBSERVATII_FINALE',
            'GREUTATE_MINIMA',
            'GREUTATE_MAXIMA',
            'VARSTA_MINIMA',
            'VARSTA_MAXIMA',
            'ACTIVITATE_MINIMA',
            'ACTIVITATE_MAXIMA',
            'Zgomot_Aleatoriu_Max',
            'Factor_Ajustare_Pui (Varsta < 1.0)',
            'Factor_Ajustare_Senior (Varsta > 8.0)',
            'Constanta_Baza_RMR'
        ],
        'Valoare': [
            15000,
            5.0,
            30.0,
            0.5,
            12.0,
            0.5,
            12.0,
            15.0,
            1.5,
            0.9,
            80 
        ],
        'Unitate': [
            'observatii',
            'kg',
            'kg',
            'ani',
            'ani',
            'ore',
            'ore',
            'grame',
            'multiplicator',
            'multiplicator',
            'grame_baza'
        ],
        'Explicatie': [
            'Totalul de inregistrari generate.',
            'Limita fizica inferioara a greutatii.',
            'Limita fizica superioara a greutatii.',
            'Varsta minima de inregistrare.',
            'Varsta maxima de inregistrare.',
            'Activitate minima zilnica.',
            'Activitate maxima zilnica.',
            'Eroarea maxima adaugata la portia tinta.',
            'Factor energetic aplicat animalelor tinere (crestere).',
            'Factor energetic aplicat animalelor batrane (metabolism scazut).',
            'Cantitatea de baza necesara, independenta de parametri.'
        ]
    }

    df_params = pd.DataFrame(parameters)
    OUTPUT_PATH = 'docs/data_sim_parameters.csv'
    
    df_params.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Documentatia parametrilor de simulare a fost salvata ca CSV: {OUTPUT_PATH}")

if __name__ == '__main__':
    generate_parameter_csv()