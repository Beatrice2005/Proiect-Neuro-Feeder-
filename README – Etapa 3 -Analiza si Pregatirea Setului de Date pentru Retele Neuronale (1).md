# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Debruyker Ioana-Beatrice 
**Data:** 

---

## Introducere

Acest document descrie activitatile realizate in **Etapa 3**, in care se analizeaza si se preproceseaza setul de date necesar proiectului „Retele Neuronale". Scopul etapei este pregatirea corecta a datelor pentru instruirea modelului RN, respectand bunele practici privind calitatea, consistenta si reproductibilitatea datelor.

---

##  1. Structura Repository-ului Github (versiunea Etapei 3)

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Generarea programatica bazata pe cunostinte din nutritia animala si profilul de activitate
* **Modul de achiziție:** generare programatica
* **Perioada / condițiile colectării:** Date simulate, generate pentru a reprezenta o monitorizare pe termen lung

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 15,000
* **Număr de caracteristici (features):** 3 inputuri si un target
* **Tipuri de date:** Numerice 
* **Format fișiere:** CSV 

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
| nume_caine | string | n\a | Numele animalului inregistrat |  |
| greutatea_curenta | numeric | kg | Greutatea animalului inregistrata la momentul hranirii | 5.0-30.0 |
| varsta_animalului | numeric | ani | Varsta animalului | 0.5-12.0 |
| orele_de_activitate | numeric | ore | Orele de activitate inregistrate de colier in ultimele 24 de ore | 0.5-12.0 |
| grame_hrana_necesare | numeric | grame | Cantitatea optima de hrana calculata de variabila tinta | 10-500 |

**Fișier recomandat:**  `data/README.md`

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

* **Medie, mediană, deviație standard**
---greutatea_curenta: Media este de aproximativ 15.0 kg, reflectand populatia majoritar de talie medie. Deviatia standard (aprox. 5.0 kg) indica o dispersie rezonabila a masuratorilor.
---orele_de_activitate: Media este de circa 4.0 ore/zi, cu o deviatie standard care arata variatii tipice in regimul zilnic de miscare.
---varsta_animalului: Media este situata in jurul a 6.0 ani, in functie de distributia uniforma aplicata in simulare.
---grame_hrana_necesare: Media portiei este de aprox. 200–250 de grame. Deviatia standard este mare, deoarece modelul include atat nevoile calorice minime ale unui senior, cat si nevoile maxime ale unui pui.
* **Min–max și quartile**
Valorile Min-Max sunt confirmate conform domeniilor specificate in Sectiunea 2.3: greutatea_curenta [5.0, 30.0], varsta_animalului [0.5, 12.0], orele_de_activitate [0.5, 12.0], si grame_hrana_necesare [10, 500].

Analiza cuartilelor (25%, 50%, 75%) confirma ca majoritatea observatiilor se incadreaza in intervalele normale, dar variatia este mare in variabila tinta.
* **Distribuții pe caracteristici** (histograme)
Histogramele variabilelor de intrare (greutatea_curenta, orele_de_activitate) prezinta distributii similare cu cele normale (Gaussiene).

Distributia grame_hrana_necesare este usor asimetrica, avand o coada mai lunga spre valorile mari, din cauza factorului biologic al puilor.
* **Identificarea outlierilor** (IQR / percentile)
Diagramele Box-Plot indica prezenta de outlieri in grame_hrana_necesare.

Acesti outlieri nu sunt erori de masurare, ci valori legitime corespunzatoare animalelor tinere (sub 1 an) sau foarte grele si active. 

### 3.2 Analiza calității datelor

* **Detectarea valorilor lipsă** (% pe coloană) - Setul de date este complet (0% valori lipsa), fiind generat programatic.
* **Detectarea valorilor inconsistente sau eronate** - Nu au fost detectate valori eronate.
* **Identificarea caracteristicilor redundante sau puternic corelate** - S-a confirmat o corelatie pozitiva puternica intre:   greutatea_curenta si grame_hrana_necesare
                           orele_de_activitate si grame_hrana_necesare

### 3.3 Probleme identificate
Problema principala- Variatie de Scala: Variabilele de intrare se afla pe scale numerice extrem de diferite (ex: Varsta vs. Greutatea).

Impact: Diferenta de scala ar influenta negativ antrenarea Retelei Neuronale.
Solutie: Standardizarea este obligatorie, transformand toate datele de intrare pentru a avea medie zero si deviatie standard egala cu unu.

Problema Secundara- Distributie neuniforma: Variabila tinta este influentata de factorii de varsta (pui) si poate fi usor asimetrica.

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

* **Eliminare duplicatelor** -Se elimina randurile complet duplicate.
* **Tratarea valorilor lipsă:** -Nu se aplica, setul de date fiind complet.
* **Tratarea outlierilor:** -Se aplica capping bazat pe percentile extreme (ex: 99.9%) in variabila tinta pentru a limita valorile potential nerealiste, pastrand in acelasi timp outlierii legitimi.

### 4.2 Transformarea caracteristicilor

* **Normalizare:** -Se aplica Standardizarea pe caracteristicile de intrare (greutatea_curenta, varsta_animalului, orele_de_activitate).
* **Encoding pentru variabile categoriale** -Nu este necesar.
* **Ajustarea dezechilibrului de clasă** -Nu este necesar, deoarece proiectul este o problema de regresie, nu de clasificare.

### 4.3 Structurarea seturilor de date

**Împărțire recomandată:** Setul de date este impartit folosind train_test_split:
*  80% – train
*  10% – validation
*  10% – test

**Principii respectate:**
* Fără scurgere de informație (data leakage)
* Statisticiile de standardizare sunt calculate DOAR pe setul de Training si aplicate pe Validation si Test

### 4.4 Salvarea rezultatelor preprocesării

* Date preprocesate in: `data/train/` , `data/validation/` , `data/test/`
* Parametrii de preprocesare: Transformatorul StandardScaler antrenat este salvat ca fisier StandardScaler.joblib in directorul `config/`.

##  5. Fișiere Generate în Această Etapă

* `data/raw/` – `raw_data.csv` date brute
* `data/train/`, `data/validation/` ,`data/test/` – Seturile finale de date preprocesate si impartite.
* `src/preprocessing` -– Scriptul preprocess_data.py (Codul de preprocesare)
* `config/` – Fisierul `StandardScaler.joblib` (Transformatorul antrenat)
* `data/README.md` – Descrierea dataset-ului

---  

##  6. Stare Etapă (de completat de student)

- [X] Structură repository configurată
- [X] Dataset analizat (EDA realizată)
- [X] Date preprocesate
- [X] Seturi train/val/test generate
- [X] Documentație actualizată în README + `data/README.md`

---
