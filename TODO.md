## Exercise 0 — Entering the Matrix

Devi creare construct.py, che riconosca se viene eseguito dentro o fuori un ambiente virtuale, mostri i percorsi Python e dei pacchetti e spieghi come creare un ambiente virtuale se necessario.

## Exercise 1 — Loading Programs

Devi creare loading.py, generare dati con NumPy, analizzarli con pandas, produrre un grafico con Matplotlib, controllare le dipendenze installate e presentare le differenze tra pip e Poetry. Devi fornire entrambi i file di configurazione delle dipendenze.

## Exercise 2 — Accessing the Mainframe

Devi creare oracle.py, che carichi le cinque variabili richieste (MATRIX_MODE, DATABASE_URL, API_KEY, LOG_LEVEL, ZION_ENDPOINT), gestisca configurazioni incomplete e mostri un comportamento diverso tra development e production.

the_matrix/
├── ex0/
│   └── construct.py
│
├── ex1/
│   ├── loading.py
│   ├── requirements.txt
│   └── pyproject.toml
│
└── ex2/
    ├── oracle.py
    ├── requirements.txt
    ├── .env.example
    └── .gitignore