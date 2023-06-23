## Applicazione Votazione Comune
Scopo del progetto è quello di realizzare un’applicazione CLI Python che gestisca il processo di votazione di proposte da parte degli studenti. 
Il tutto utilizzando Redis come database. 

L’app Python permette di:
- Caricare le proposte - ogni proposta ha uno o più proponenti
- Ogni studente può votare tutte le proposte che vuole, ma al massimo un voto per proposta
- In ogni momento l’applicazione può mostrare la lista delle proposte ordinate per numero di voti

#Questo è un esempio di come potrebbe essere l'output:

Proposte attuali:
1. Macchina del caffè gratis (Gino): 123 voti
2. Valutazione dei prof (Michela, Marco): 110 voti
3. Campo Basket aperto di notte (Gino, Pino): 34 voti

Scegli
n. Nuova proposta
v. Vota una proposta
n
Descrivi la proposta
Vacanze di classe
Chi sono i proponenti?
Maria, Mario, Susanna
...
Chi sei
Francesco
Che proposta voti? 
2
