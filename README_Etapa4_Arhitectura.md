# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Debruyker Ioana-Beatrice
**Link Repository GitHub** https://github.com/Beatrice2005/Proiect-Neuro-Feeder-
**Data:** [Data]  

### 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software (max ½ pagină)
Completați in acest readme tabelul următor cu **minimum 2-3 rânduri** care leagă nevoia identificată în Etapa 1-2 cu modulele software pe care le construiți (metrici măsurabile obligatoriu):

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |

| Risc de Obezitate din cauza regimului alimentar fix si rigid, care ignora variatia metabolica zilnica | Predictie de Regresie bazata pe activitatea animalului -> Mentinere greutate optima cu eroare sub 5% MSE media patratelor erorilor pe test set | RN (MLPRegressor)+ Web Service |

| Dozare manuala sau bazata pe temporizatoare incapabila sa se adapteze la efortul fizic | Calcul automat al portiei (ajustat in functie de orele de activitate) -> Timp de inferenta al portiei sub 500 ms, eliminand complet interventia umana la fiecare masa. | Web Service (FastAPI)+ RN Module|

| Date de intrare (Varsta, Greutate, Activitate) | Standardizare obligatorie in Backend -> Datele de intrare sunt transformate si normalizate inainte de inferenta, asigurand stabilitatea si viteza de calcul a Retelei Neuronale | Preprocessing Module |

### 2. Contribuția Voastră Originală la Setul de Date – MINIM 40% din Totalul Observațiilor Finale

**Regula generală:** Din totalul de **N observații finale** în `data/processed/`, **minimum 40%** trebuie să fie **contribuția voastră originală**.

Proiectul "Neuro-Feeder", utilizeaza o metoda de generare a datelor bazata pe simulare fizica (logica calorica/BMI), nu pe un dataset public.

### Contribuția originală la setul de date:

**Total observații finale:** 15.000 (după Etapa 3 + Etapa 4)
**Observații originale:** 15.000 ([100]%)

**Tipul contribuției:**
[X] Date generate prin simulare fizică  
[ ] Date achiziționate cu senzori proprii  
[ ] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**
Setul de date Neuro-Feeder este integral original (100%), generat prin simulare in Python, respectand cerinta de a avea minimum 40% contributie proprie.
Metoda de Generare: Generarea datelor se bazeaza pe o simulare a nevoilor calorice, utilizand o formula cunoscuta in nutritia veterinara (Calorii zilnice necesare  =aproximativ RMR * Factor de activitate) ce modeleaza Rata Metabolica de Repaus (RMR) si factori biologici.

Functia de simulare inlocuieste un simplu calcul cu o logica non-lineara care include:
Factori de Intrarea RN: greutatea, varsta si orele de activitate.
Factori Biologici: S-au aplicat factori de ajustare specifici (ex: factor de 1.5x pentru pui sub 1 an si 0.9x pentru seniori) in formula de calcul a portiei, asigurand astfel ca datele reflecta realitatea biologica a nevoii calorice dinamice.

Zgomot Aleatoriu: S-a introdus zgomot in variabila tinta pentru a simula erorile de masurare sau variabilitatea metabolica individuala, facand setul de date mai robust si mai realist pentru antrenarea Retelei Neuronale.

Reteaua Neuronala (MLPRegressor) are ca sarcina sa invete exact acea functie matematica complexa care a fost folosita pentru generare (greutate - activitate - varsta).

**Locația codului:** `src/preprocessing/generate_raw_data.py`
Codul sursa functional care implementeaza formula RMR si factorii biologici de ajustare.
**Locația datelor:** `data/raw/raw_data.csv`
Setul de date brut cu 15.000 de observatii, continand coloanele `animal_id`, `greutatea_curenta`, `varsta_animalului`, `orele_de_activitate`, si `grame_hrana_necesare`.

**Dovezi:**
- Grafic comparativ: `docs/simulated_distribution.png`
- Tabel statistici: `docs/data_statistics.csv`
- Documentare parmetri: `docs/data_sim_parameters.csv`

#### Exemple pentru "contribuție originală":
-Simulări fizice realiste cu ecuații și parametri justificați:
S-a folosit meodelarea calorica bazata pe Rata metabolica de Repaus (RMR) si factori biologici ( spre exemplu: pui/senior, activitate) pentru a genera variabila tinta. 

### 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)
- **Minimum 4-6 stări clare** cu tranziții între ele

Starile principale sunt:
1.Idle/Wait User: Starea initiala, asteptand introducerea datelor de catre utilizator.
2.Preprocess/Scale Data: Starea critica unde datele sunt normalizate utilizand `scaler.joblib`.
3.MLP Predict: Starea unde calculeaza cantitatea de grame necesara.
4.Display Result: Rezultatul final este trimis inapoi catre interfata web.

Tranzitiile critice sunt:
1.Input Validat: De la Idle la Preprocess, declansat de un input care a trecut de validarea initiala.
2.Error State: Starea de eroare este esentiala pentru a gestiona fie datele de intrare nevalide, fie esecul de incarcare a modelului/scaler-ului.
Bucla de feedback este simpla: Dupa Display Result, sistemul revine in starea Wait User gata sa proceseze urmatoarea cerere de hranire.

- **Formate acceptate:** 
Am folosit formatul Draw.io.
- **Locație:** 
Diagrama a fost salvata in directorul `docs/state_machine.drawio`
- **Legendă obligatorie:** 
Am ales arhitectura de tip Web Service/Predictie la cerere deoarece proiectul meu necesita un calcul precis si rapid la momentul hranirii, activat de o cerere de interfata web. Fluxul este strict secvential: pleaca din starea de Idle, intra in Preprocess pentru normalizare cu `scaler.joblib`, trece la MLP Predict pentru interfata propriu-zisa, iar apoi ajunge la Display Result. 
Starea de Error State este vitala pentru a gestiona esecurile, precum neincarcarea scheletului modelului sau validarea datelor, asigurand ca sistemul nu se blocheaza si revine la starea Idle/Wait User dupa finalizare, indiferent de rezultat (eroare sau succes).

### 4. Scheletul Complet al celor 3 Module Cerute la Curs (slide 7)

| **Modul** | **Python (exemple tehnologii)** | **LabVIEW** | **Cerință minimă funcțională (la predare)** |
| **1. Data Logging** | `src/preproccessing/` | Produce `raw_data.csv` si `scaler.joblib` |
| **2. Neural Network** | `models/`| Model RN definit si salvat ca `rn_model_untrained.joblib` |
| **3. Web Service** | FastAPI | Serverul api.py ruleaza si returneaza output numeric |

#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition**
Generare originala: 15.000 de esantioane create integral prin scriptul `generate_raw_data.py`.
Standardizare: Salvarea obiectului `scaler.joblib` pentru prelucrarea automata a datelor de intrare.
Validare: Documentarea parametriilor si a statisticilor in fisiere CSV dedicate in folderul `docs/`.

#### **Modul 2: Neural Network Module**
Definirea: Arhitectura MLPRegressor configurata pentru regresie si salvata in `models/`
Compilare: Modelul este gata pentru antrenare, avand toate straturile neuronale definite.
Incarcare: Verificarea  integritatii prin incarcarea automata a fisierului `joblib` in serverul API.

#### **Modul 3: Web Service / UI**
Serverul activ: Implementarea logicii de backend folosind FastAPI in fisierul `api.py`.
Endpoint predicst: Creearea rutei `/predict_portie` care leaga interfata de modelul RN.
Demo functional: Screenshot din `docs/screenshot/` demonstreaza comunicarea end-to-end fara erori.

**Verificare consistență cu Etapa 3:**
proiect-rn-[Debruyker-Ioana-Beatrice]/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── generated/  # Date originale
│   ├── train/
│   ├── validation/
│   └── test/
├── src/
│   ├── data_acquisition/
│   ├── preprocessing/  # Din Etapa 3
│   ├── neural_network/
│   └── app/  # UI schelet
├── docs/
│   ├── state_machine.*           #(state_machine.png sau state_machine.pptx sau state_machine.drawio)
│   └── [alte dovezi]
├── models/  # Untrained model
├── config/
├── README.md
├── README_Etapa3.md              # (deja existent)
├── README_Etapa4_Arhitectura_SIA.md              # ← acest fișier completat (în rădăcină)
└── requirements.txt  # Sau .lvproj

### Documentație și Structură
- [x] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [x] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [x] Cod generare/achiziție date funcțional și documentat
- [x] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [x] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [x] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [x] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [x] Cod rulează fără erori `python src/preprocessing/generate_raw_data.py`
- [x] Produce minimum 40% date originale din dataset-ul final
- [x] CSV generat în format compatibil cu preprocesarea din Etapa 3
- [x] Documentație în cod si in folderul `docs/`:
  - [x] Metodă de generare/achiziție explicată (Simulare RMR)
  - [x] Parametri folosiți si justificare relevanta date
- [x] Fișiere în `data/raw/` conform structurii

### Modul 2: Neural Network
- [x] Arhitectură RN definită și documentată în cod `models/rn_models_untrained.joblib`
- [x] README în `src/neural_network/` cu detalii arhitectură curentă - Am lucrat direct in fiserul api.py si in folderul `models/`

### Modul 3: Web Service / UI
- [x] Propunere Interfață ce pornește fără erori (FastAPI ruleaza pe portul 8000)
- [x] Screenshot demonstrativ în `docs/screenshots/ui_demo.jpg`
- [x] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)
