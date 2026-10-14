loading.py deve generare dati simulati con NumPY, analizzarli con pandas, creare un grafico con matplotlib e controllare che le librerie necessarie siano installate

dimostrate la differenza tra la gestione delle dipendenze con pip e Poetry e gestire il caso in cui manchino alcune librerie

# Come funziona l'installazione dei package:

import: 
    non installa, chiede a Python di trovare e caricare il package
    se non installato ottieni ModuleNotFoundError

pip:
    è il gestore di pacchetti
    installa, aggiorna e disintalla distribuzione Python
    è un modulo, posso utilizzarlo come modulo, utilizzando pip attraverso quello specifico interprete python, riducendo il rischio di installare una liberia in un ambiente diverso da quello che userai per eseguire il programma:
    python -m pip install numpy

    funziona anche pip, utilizzando il comando pip dalla shell


# Cosa sono le dipendenze?

se nel mio porgramma per es. ho :

import numpy
import pandas

il programma ha bisogno di queste librerie per funzionare: si dice quindi che numpy e pandas sono dipendenze del progetto. queste sono dipendenze dirette. A loro volta le dipendenze possono richiedere altri pacakge, che saranno dipendenze *transitive*.


# requirements.txt:

è un file di testo che elenca le dipendenze da installare con pip.
serve a far sapere ad altre persone che usano il tuo programma quali librerie devono avere installate.
es puo contenere:
numpy
pandas

chi riceve il progetto può eseguire:

python3 -m pip install -r requirements.txt

la -r dice a pip di __*leggere*__ i requisiti dal file specificato

puoi anche indicare le versioni esatte:
numpy==2.1.3
oppure intervallu
numpt>=2.0,<3.0


# Cos'è Poetry

Poetry è uno strumento di gestione dei progetti Python che integra diverse funzionalità.
Puoi gestire in maniera integrata:
-le dipendenze del progetto
-le versioni compatibili
-un file di configurazione che utilizza:
                            pyproject.toml
-un file di lock per registrare le versioni risolte:
                            poetry.lock
-gli ambienti virtuali associati al progetto

requirements.txt e pyproject.toml permettono di ricostruire l'ambiente di lavoro senza doverlo caricare su Git

# pyproject.toml

.toml estensione indica un formato di configurazione chiamato TOML. è un formato testuale progettato per rappresentare dati strutturati in modo leggibile

es:

name = "matrix"
version = "1.0.0"

si definiscono coppie chiave = valore
In TOML si possono anche creare sezioni,, la sezione [project] raggruppa informazioni relative al progetto:

[project]
name = "matrix"
version = "1.0.0"

(version contiene la versione del progetto)


# Configurazione Poetry per questo progetto

[tool.poetry]
name = "matrix-loading"
version = "0.1.0"
description = "Matrix data analysis exercise"
authors = ["Student"]

package-mode = false

[tool.poetry.dependencies]
python = ">=3.10,<4.0"
numpy = "*"
pandas = "*"
matplotlib = "*"

tool.poetry contiene le informazioni del progetto gestito da Poetry
name identifica il progetto
version è la versione del progetto stesso
package-mode = false indica che vogliamo utilizzare Poetry per gestire le dipendenze senza necessariamente creare un package Python distribuibile. Appropriato perchè stiamo costruendo uno script.
tool.poetry.dependecies elenca le dipendenze necessarie
python = ...  indica delle versioni Pyhton supportate dalla configurazione
Il simbolo * per ora indica che non stiamo imponendo un vincolo di versione specifico per queste librerie. Nei progetti reali è generalmente preferibile definire vincoli compatibili e verificati


# Come funziona poetry install

quando esegui:
    poetry install

Poetry legge il file pyproject.toml, individua le dipendenze dichiarate, risolve le versioni compatibili e le installa nell'ambiente python gestito per il progetto.
Normalmente genera anche un file poetry.lock
è un file che registra informazioni dettagliate sulle dipendeze risolte, comprese quelle indirette

pyproject.toml	
        Dichiara quali dipendenze richiede il progetto
poetry.lock	
        Registra le versioni e le dipendenze risolte
requirements.txt	
        Fornisce a pip l'elenco dei requisiti da installare

Caricamento dei messaggi meno recenti…
mostrami la versione correttta dell'esercizio constryct.py

Ecco la versione completa e corretta di ex0/construct.py, basata sul tuo codice e sui requisiti dell'Exercise 0 del subject The Matrix.

Ho mantenuto le tre funzioni che avevi creato, migliorato i messaggi e aggiunto le istruzioni per attivare l'ambiente virtuale su Linux e Windows.
Codice completo — construct.py

import os
import site
import sys


def is_virtual_environment() -> bool:
    """Check whether Python is running inside a virtual environment."""
    return sys.prefix != sys.base_prefix


def show_environment_info() -> None:
    """Display information about the current Python environment."""
    print("Current Python:", sys.executable)
    print("Environment path:", sys.prefix)
    print("Base Python path:", sys.base_prefix)

    print("\nPackage installation paths:")
    for path in site.getsitepackages():
        print(path)


def main() -> None:
    """Display virtual environment status and setup instructions."""
    if is_virtual_environment():
        print("MATRIX STATUS: Welcome to the construct\n")

        show_environment_info()

        env_name = os.path.basename(sys.prefix)
        print("\nVirtual Environment:", env_name)
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

    else:
        print("MATRIX STATUS: You're still plugged in\n")
Perché questa versione è corretta?

Requisito del subject
	

Come viene soddisfatto

Rilevare il virtual environment
	

sys.prefix != sys.base_prefix

Visualizzare l'interprete
	

sys.executable

Mostrare il percorso dell'ambiente
	

sys.prefix

Mostrare l'installazione di base
	

sys.base_prefix

Mostrare il nome del virtual environment
	

os.path.basename()

Individuare i percorsi dei package
	

site.getsitepackages()

Fornire istruzioni di attivazione
	

Ramo else

Mostrare comportamenti diversi
	

Rami if ed else

Utilizzare soltanto moduli autorizzati
	

sys, os, site

Type hints
	

Tutte le funzioni sono annotate

Una precisazione: il codice mostra i percorsi dei package dell'ambiente corrente e il percorso dell'installazione Python di base. Per dimostrare esplicitamente la differenza tra le directory dei package globali e virtuali, come richiesto dal subject, è opportuno confrontare gli output ottenuti eseguendolo in entrambi gli ambienti.
Come verificare il risultato

Dalla directory principale del progetto:

python3 -m flake8 ex0/construct.py
python3 -m mypy ex0/construct.py

Poi prova l'esecuzione fuori e dentro l'ambiente virtuale.

# Fuori dall'ambiente virtuale
python3 ex0/construct.py

# Dentro l'ambiente virtuale, senza attivarlo
./matrix_env/bin/python ex0/construct.py

Il secondo comando presuppone che matrix_env sia nella directory principale del progetto.

Una cosa da ricordare per la peer evaluation: site.getsitepackages() restituisce una lista, non una stringa. Il ciclo for serve a mostrare tutti i percorsi, anche se sul tuo computer ne viene restituito soltanto uno.

Con questa versione hai un'implementazione sostanzialmente completa dell'Exercise 0. Prima di consegnarlo, controlla l'output in entrambe le condizioni e verifica flake8 e mypy.
e la directroy ex0 deve star edentro o fuori la cartella matrix_env?

La cartella ex0 deve stare FUORI da matrix_env.

Le due cartelle devono essere separate, allo stesso livello, all'interno della directory principale del progetto.

La struttura corretta è:
the_matrix/
│
├── ex0/
│   └── construct.py
│
├── ex1/
│   ├── loading.py
│   ├── requirements.txt
│   └── pyproject.toml
│
├── ex2/
│   ├── oracle.py
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
│
├── matrix_env/           ← Ambiente virtuale
│   ├── bin/
│   ├── lib/
│   └── pyvenv.cfg
│
└── .gitignore

Perché devono essere separate?

    ex0 contiene il codice sorgente che devi consegnare.

    matrix_env contiene l'ambiente virtuale, cioè l'interprete Python e i package installati per il progetto.

La cosa fondamentale è che matrix_env non deve essere caricata su Git, come specificato dal subject.

Nel .gitignore della directory principale puoi quindi inserire:
matrix_env/
Come eseguire il tuo programma

Se ti trovi dentro the_matrix, per eseguire il programma senza ambiente virtuale:

python3 ex0/construct.py

Per eseguirlo dentro l'ambiente virtuale:

source matrix_env/bin/activate
python3 ex0/construct.py

E per uscire:

deactivate

Nota importante: nel repository Git consegnerai le cartelle ex0, ex1 ed ex2, ma non matrix_env. Durante la peer evaluation dovrai essere in grado di ricreare l'ambiente virtuale da zero.
proseguiamo

Perfetto! Passiamo all'Exercise 1 – Loading Programs, che si trova alle pagine 9–11 del subject The Matrix.

Questo esercizio è più articolato del precedente perché introduce strumenti fondamentali nello sviluppo Python: pip, Poetry, gestione delle dipendenze, NumPy, pandas e Matplotlib.

Continuiamo con lo stesso metodo: prima capiamo i concetti, poi scriviamo il codice insieme.
1. Cosa ci chiede l'Exercise 1?

Dovremo creare tre file:
ex1/
├── loading.py
├── requirements.txt
└── pyproject.toml

Il programma loading.py dovrà generare dati simulati con NumPy, analizzarli con pandas, creare un grafico con Matplotlib e controllare che le librerie necessarie siano installate.

Dovremo inoltre dimostrare la differenza tra la gestione delle dipendenze con pip e Poetry e gestire il caso in cui manchino alcune librerie.

Ma prima dobbiamo capire bene come funziona l'installazione dei package.
2. Che cos'è pip?

Hai già visto che Python permette di utilizzare librerie esterne tramite import.

Per esempio:
import numpy

Ma import numpy non installa NumPy: chiede a Python di trovare e caricare il package.

Se non è installato nell'ambiente che stai utilizzando, normalmente ottieni:
ModuleNotFoundError: No module named 'numpy'

Ed è qui che entra in gioco pip.

pip è il gestore di pacchetti utilizzato per installare, aggiornare e disinstallare distribuzioni Python.

Immagina tre elementi:
Schema semplificato: pip scarica il package da PyPI (o da un'altra fonte configurata) e lo installa nell'ambiente Python selezionato.

Quando digiti:

python -m pip install numpy

succedono diversi passaggi:

    Avvii l'interprete python.

    Con -m pip chiedi a Python di eseguire il modulo pip.

    Con install numpy chiedi a pip di installare NumPy.

    pip individua una versione compatibile, risolve le dipendenze necessarie e installa i file nell'ambiente Python selezionato.

Perché uso python -m pip anziché semplicemente pip?

Entrambi possono funzionare, ma:

pip install numpy

utilizza il comando pip trovato dalla shell.

Invece:

python -m pip install numpy

utilizza pip attraverso quello specifico interprete Python.

Questo riduce il rischio di installare una libreria in un ambiente diverso da quello che userai per eseguire il programma.
3. Che cosa sono le dipendenze?

Immagina che tu stia costruendo il programma loading.py.

Il tuo codice contiene:
import numpy
import pandas
import matplotlib

Il programma ha bisogno di queste librerie per funzionare.

Si dice quindi che NumPy, pandas e Matplotlib sono dipendenze del progetto.

E le dipendenze possono avere altre dipendenze.

Per esempio, pandas utilizza NumPy per molte operazioni numeriche.

Queste sono le dipendenze dirette. Le librerie possono a loro volta richiedere altri package, chiamati dipendenze transitive.

Perché è importante? Perché non basta sempre installare una singola libreria: bisogna ottenere un insieme di versioni compatibili.
4. Che cos'è requirements.txt?

Supponiamo che tu installi tutte le librerie necessarie nel tuo ambiente virtuale.

Il programma funziona.

Poi però un'altra persona scarica il tuo progetto da Git.

Quella persona non ha necessariamente le stesse librerie installate.

Come fa a sapere cosa deve installare?

È qui che entra in gioco requirements.txt.

È un file di testo che elenca le dipendenze da installare con pip.

Per esempio:
numpy
pandas
matplotlib

Chi riceve il progetto può eseguire:

python -m pip install -r requirements.txt

La -r dice a pip di leggere i requisiti dal file specificato.

Puoi anche indicare versioni esatte:
numpy==2.1.3
pandas==2.2.3
matplotlib==3.9.2

Queste sono versioni illustrative, non necessariamente quelle che sceglieremo per il tuo progetto.

Oppure intervalli:
numpy>=2.0,<3.0

Che significa: una versione di NumPy almeno 2.0, ma inferiore a 3.0.
Una distinzione importante

Il file requirements.txt non contiene le librerie, contiene le istruzioni per installarle.

È un po' come una lista della spesa: non contiene il cibo, ma indica cosa comprare.
5. Che cos'è Poetry?

Il subject ti chiede di utilizzare anche Poetry.

Poetry è uno strumento di gestione dei progetti Python che integra diverse funzionalità.

Mentre con pip puoi installare pacchetti, con Poetry puoi gestire in maniera integrata:

    Le dipendenze del progetto.

    Le versioni compatibili.

    Un file di configurazione pyproject.toml.

    Un file di lock per registrare le versioni risolte.

    Gli ambienti virtuali associati al progetto.

Nel tuo esercizio la differenza principale sarà questa:

pip
	

Poetry

Installa package Python
	

Gestisce dipendenze e progetto

Può leggere requirements.txt
	

Utilizza pyproject.toml

Può usare un ambiente venv creato separatamente
	

Può creare e gestire un ambiente virtuale

Non crea automaticamente un lockfile standard per il progetto
	

Produce normalmente poetry.lock

Poetry non sostituisce l'interprete Python: lo utilizza.
6. Fermiamoci su un esempio concreto

Immagina questa situazione.

Hai creato:
the_matrix/
├── matrix_env/
└── ex1/
    └── loading.py

Attivi l'ambiente:

source matrix_env/bin/activate

Poi installi NumPy:

python -m pip install numpy

A questo punto il tuo programma loading.py può importare NumPy, purché venga eseguito con l'interprete del medesimo ambiente.

Se però elimini matrix_env, scompaiono anche i package che vi avevi installato.

Il codice sorgente del progetto rimane, ma dovrai reinstallare le dipendenze.

Ecco perché i file requirements.txt e pyproject.toml sono importanti: permettono di ricostruire l'ambiente di lavoro senza doverlo caricare su Git.
7. Verifichiamo se hai capito prima di continuare

1. Qual è la differenza tra import numpy e python -m pip install numpy?
Entrambi installano NumPy
Il primo importa NumPy nel programma, il secondo lo installa
Il primo crea un virtual environment

import carica il modulo per utilizzarlo nel programma; pip install mette a disposizione la distribuzione nell'ambiente Python.

2. Se elimini matrix_env, cosa succede?
Perdi anche loading.py
Perdi le librerie installate in quell'ambiente, ma non il codice fuori da esso
Elimini Python dal computer

L'ambiente virtuale contiene la propria installazione dei package. Il codice conservato fuori dall'ambiente rimane.

3. A cosa serve requirements.txt?
A contenere il codice delle librerie
A specificare dipendenze installabili con pip
A indicare dove si trova l'interprete Python

È un file di requisiti per pip, utile per ricostruire le dipendenze necessarie.

4. Perché utilizzare python -m pip invece di pip?
Per associare pip all'interprete Python selezionato
Per evitare completamente gli ambienti virtuali
Per installare sempre globalmente

Il comando esegue pip attraverso l'interprete indicato da python.

Risposte corrette: 4 su 4

Una volta che questi concetti sono chiari, il passo successivo sarà creare davvero requirements.txt, capire la struttura di pyproject.toml e provare pip e Poetry, prima di iniziare l'analisi dei dati con NumPy e pandas.

Per ora non installerei tutte le librerie: prima voglio che tu capisca esattamente cosa stiamo configurando e perché.
vai proseguiamo

Proseguiamo con l'Exercise 1 – Loading Programs. Adesso impariamo a creare e utilizzare i due file richiesti dal subject: requirements.txt e pyproject.toml.

Ti guiderò anche nell'installazione delle dipendenze con pip e Poetry, ma soprattutto voglio che tu capisca cosa succede realmente quando esegui i comandi.
1. Prepariamo la directory ex1

Dalla directory principale del tuo repository, esegui:

mkdir -p ex1
cd ex1

Creiamo i tre file richiesti:

touch loading.py requirements.txt pyproject.toml

La struttura sarà:
the_matrix/
├── ex0/
│   └── construct.py
├── ex1/
│   ├── loading.py
│   ├── requirements.txt
│   └── pyproject.toml
└── matrix_env/

Per ora loading.py rimarrà vuoto.
2. Creiamo requirements.txt

Nel file inserisci:
numpy
pandas
matplotlib

Il subject autorizza anche requests, ma specifica che è facoltativo: serve soltanto se decidi di recuperare dati da un'API esterna. Noi utilizzeremo dati simulati generati con NumPy, quindi non ci serve.

Ora puoi installare tutte e tre le librerie con un solo comando:

python -m pip install -r requirements.txt

Ma attenzione: in quale ambiente vengono installate?

Dipende dall'interprete python utilizzato.

Se hai attivato matrix_env, l'installazione avverrà normalmente lì. Se non l'hai attivato, python potrebbe riferirsi a un altro interprete.

Per verificare:

python -c "import sys; print(sys.executable)"

Se il percorso termina con matrix_env/bin/python, sai che stai utilizzando l'ambiente previsto.
3. Che cos'è davvero pyproject.toml?

Questo file merita una spiegazione perché è utilizzato in moltissimi progetti Python moderni.

L'estensione .toml indica un formato di configurazione chiamato TOML.

È un formato testuale progettato per rappresentare dati strutturati in modo leggibile.

Un esempio semplice:
name = "matrix"
version = "1.0.0"

Qui non stai scrivendo istruzioni Python.

Stai definendo delle coppie chiave = valore.

In TOML puoi anche creare sezioni:
[project]
name = "matrix"
version = "1.0.0"

La sezione [project] raggruppa le informazioni relative al progetto.

Come leggere un file TOML

[project]

Nome della sezione

name = "matrix"

La chiave name contiene la stringa "matrix".

version = "1.0.0"

La chiave version contiene la versione del progetto, non quella di Python.
4. Configuriamo Poetry

Per questo esercizio possiamo utilizzare un pyproject.toml con una configurazione Poetry come questa:
[tool.poetry]
name = "matrix-loading"
version = "0.1.0"
description = "Matrix data analysis exercise"
authors = ["Student"]

package-mode = false

[tool.poetry.dependencies]
python = ">=3.10,<4.0"
numpy = "*"
pandas = "*"
matplotlib = "*"

Vediamo ogni parte.

[tool.poetry] contiene le informazioni del progetto gestito da Poetry.

name identifica il progetto.

version è la versione del progetto stesso.

package-mode = false indica che vogliamo utilizzare Poetry per gestire le dipendenze senza necessariamente creare un package Python distribuibile. È appropriato perché stiamo sviluppando uno script.

[tool.poetry.dependencies] elenca le dipendenze necessarie.

Infine:
python = ">=3.10,<4.0"

dichiara l'intervallo delle versioni Python supportate dalla configurazione.

Il simbolo *, per ora, indica che non stiamo imponendo un vincolo di versione specifico per quelle librerie. In progetti reali è generalmente preferibile definire vincoli compatibili e verificati.

Nota: questo è un esempio di configurazione Poetry, non un contenuto imposto parola per parola dal subject. Il PDF richiede il file pyproject.toml, ma lascia a te la sua configurazione.
5. Come funziona poetry install?

Quando esegui:

poetry install

Poetry legge il file pyproject.toml, individua le dipendenze dichiarate, risolve le versioni compatibili e le installa nell'ambiente Python gestito per il progetto.

Normalmente genera anche:
poetry.lock

Che cos'è?

È un file che registra informazioni dettagliate sulle dipendenze risolte, comprese quelle indirette.

La differenza è importante:

File
	

Scopo

pyproject.toml
	

Dichiara quali dipendenze richiede il progetto

poetry.lock

contiene anche le dipendenze transitiv
	

Registra le versioni e le dipendenze risolte

requirements.txt
	

Fornisce a pip l'elenco dei requisiti da installare

Il lockfile serve a rendere le installazioni successive più riproducibili.

Poetry può creare o utilizzare un ambiente virtuale diverso da matrix_env. Per questo, quando proveremo pip e Poetry, verificheremo quale interprete viene effettivamente utilizzato

# Succo: Sia pip sia Poetry permettono di installare i pacchetti di cui un programma Python ha bisogno per funzionare.
C'è però una differenza importante: pip si occupa principalmente dell'installazione dei pacchetti, mentre Poetry gestisce le dipendenze e l'ambiente del progetto in maniera più completa.