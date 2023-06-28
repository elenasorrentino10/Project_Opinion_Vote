import redis

def vota_proposta(r, user_id):
    messaggio = input("Inserisci la proposta che vuoi votare o, se non c'è, una nuova: ")

    # Controllo se l'utente ha già votato il messaggio
    if r.sismember(f"voti:{messaggio}", user_id):
        print("Hai già votato questa proposta")
    else :
        # Incremento il numero di voti del messaggio nel database
         r.zincrby("messaggi", 1, messaggio)
        # Aggiungo l'utente ai votanti del messaggio
         r.sadd(f"voti:{messaggio}", user_id)

         print("Messaggio votato con doppio successo!")