# progetto-sicurezza
progetto per l'esame di sicurezza dell'informazione M

# Secure Communication

Questo progetto è stato realizzato per il corso di Sicurezza Informatica (LM), Unibo. L'obiettivo è simulare uno scenario di comunicazione tra dispositivi soggetto ad attacchi *Man-In-The-Middle (MITM)*, confrontando l'efficacia della cifratura TLS rispetto a una connessione TCP non cifrata.

## 🔧 Architettura del progetto

Il sistema è composto da due versioni indipendenti:

- **TCP (non sicura)**
  - `client-tcp`: invia messaggi in chiaro
  - `mitm-tcp`: intercetta e inoltra i messaggi al server TCP
  - `server-tcp`: riceve i messaggi e invia una risposta

- **TLS (sicura)**
  - `client-tls`: comunica tramite TLS
  - `mitm-tls`: tenta di intercettare la comunicazione cifrata
  - `server-tls`: accetta connessioni TLS e risponde

Tutti i componenti sono containerizzati tramite **Docker**.

## ▶️ Esecuzione
Clonare il repository, spostarsi nella cartella e lanciare:
```bash
docker-compose up --build
```
Per rendere visibile il contrasto tra comunicazione in chiaro e cifrata, i client e server TLS vengono avviati qualche secondo dopo quelli TCP.

#📄Certificati TLS
I certificati autofirmati cert.pem e key.pem sono generati tramite OpenSSL e montati nei container TLS.

# Obiettivi dimostrati
-La comunicazione TCP può essere facilmente letta e modificata da un attaccante MITM.
-La comunicazione TLS, pur passando dallo stesso MITM, è completamente protetta: l’attaccante non può né leggere né alterare i dati.
-L'eventuale modifica dei dati cifrati da parte del MITM porta al fallimento del controllo d'integrità e all'interruzione della connessione.
