# .env

Un file .env è un semplice file di testo che contiene variabili di configurazione utilizzate da un programma

usato per separare il codice dalla configurazione. Protegge dati e varibaili che contengono dati che vogliamo tenere nascosti.

Contiene i valori di alcune variabili, da solo non modifica le variabili d'ambiente, serve un programma che lo legga e carichi quei valori, di solito snza sovrascrivere quelle gia esistenti (quando faccio load_env). Pe osvrascrivere aggiugere opzione override=True

è un file nascosto per convenzione. 
Ma il punto non attribuisce alcun potere speciale al file.
Potresti chiamarlo file.env, config.env o settings.env: il contenuto avrebbe lo stesso significato se letto da python-dotenv.
La differenza è che load_dotenv() senza argomenti cerca per convenzione un file chiamato .env. Per gli altri nomi devi specificare il percorso.


from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")
print(url)

l file .env può contenere password in chiaro. Chi riesce a leggerlo può conoscere quelle password.
Per questo, normalmente, si inserisce nel .gitignore per evitare di pubblicarlo accidentalmente nel repository.
Nel tuo Exercise 2 il subject chiede infatti di consegnare un .env.example, contenente valori fittizi, ma non il .env reale.

accadono tre cose:
1. load_dotenv() cerca un file chiamato .env e ne legge il contenuto.
2. I valori vengono caricati nelle variabili d'ambiente del processo Python, normalmente senza sovrascrivere quelle già esistenti.
3. os.getenv("URL") recupera il valore della variabile d'ambiente URL

# variabile d'ambiente

Una coppia chiave valore disponibile a un processo