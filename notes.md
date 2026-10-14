## sys

sys modulo che permette di conoscere caratteristiche e interagire con l'interprete

sys.executable:
    quale python sto utilizzando?
    print() restituisce path dell'interprete utilizzato

sys.prefix prefisso dell'inetrprete corrente

sys.base_prefix prefisso dell'interprete dell'installazione base

sys.path :
     contiene i percorsi nei quali python cerca moduli e package durante gli import

## os

os permette di interagire con funzionalità del sistema operativo, come percorsi, directory e variabili d'ambiente

os.getcw(): get current working direcotry (tipo pwd)
la directory di lavoro non deve coincidere necessariamente con la dir che contiene il file python

os.path:
basename() restituisce l'ultimo componente del percorso

Funzione	Significato
os.path.basename(path)	Ultimo componente
os.path.dirname(path)	Directory che contiene il percorso
os.path.exists(path)	Verifica se il percorso esiste
os.path.join(a, b)	Unisce componenti di un percorso
EX:
import os

folder = "/home/user"
name = "matrix_env"

path = os.path.join(folder, name)

print(path)

os.environ:
    le variabili d'ambiente


## site

dove sono installati i package
si occupa della configurazione dei percorsi dei package python
import site

print(site.getsitepackages())
può mostrare una lista di directory nelle quali l'interprete cerca pacchetti installati per l'ambiente correnet 



import sys
import os
import site

print("Python executable:")
print(sys.executable)

print("Current directory:")
print(os.getcwd())

print("Python environment:")
print(sys.prefix)

print("Base Python:")
print(sys.base_prefix)

print("Package directories:")
print(site.getsitepackages())

1. Quale espressione useresti per sapere se sei dentro un normale ambiente virtuale venv?

sys.prefix != sys.base_prefix

Il confronto fra sys.prefix e sys.base_prefix permette di riconoscere se l'interprete è in un normale ambiente venv.