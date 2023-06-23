## APPLICAZIONE PER IL VOTO DI PROPOSTE DA PARTE DI STUDENTI - "StudentProposalVote"
L'applicazione CLI Python gestisce il processo di votazione di proposte da parte degli studenti.
Utilizza Redis come database e ha come focus principale quello dell'efficienza - eccetto per la parte opzionale di gestione delle proposte simili.

L’app PERMETTE di:
1. Caricare le proposte
   - Ogni proposta ha uno o più proponenti, i quali saranno identificati con un username univoco
   - Inoltre, ogni proposta non avrà duplicati
   - Quindi, se un utente dovesse proporre idee simili ad altre già esistenti, l'app lo segnalerà e suggerirà l'opzione simile, che l'utente potrà decidere se 
     votare oppure creare comunque una nuova proposta. [da rivedere]
2. Ogni studente può votare tutte le proposte che vuole, ma al massimo un voto per proposta
3. In ogni momento l’applicazione può mostrare la lista delle proposte ordinate per numero di voti

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Per semplificare, ecco un ESEMPIO di come potrebbe essere l'output:

-> Proposte attuali:
1. Macchina del caffè gratis (Gino): 123 voti
2. Valutazione dei prof (Michela, Marco): 110 voti
3. Campo Basket aperto di notte (Gino, Pino): 34 voti

-> Scegli:
n. Nuova proposta
v. Vota una proposta
n
- Descrivi la proposta:
Vacanze di classe
- Chi sono i proponenti?:
Maria, Mario, Susanna

-> Chi sei?:
Francesco
- Che proposta voti?: 
2
