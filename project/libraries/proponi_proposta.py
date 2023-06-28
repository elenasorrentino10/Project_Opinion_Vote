import redis

def scrivi_proposta(r, user_id):
    messaggio = input("Inserisci un nuovo messaggio: ")

    # Controllo se il messaggio è già presente nel database
    if r.zrank("messaggi", messaggio) is not None:
        # Se il messaggio è già presente, aggiungo l'utente come propositore del messaggio
        r.sadd(f"propositori:{messaggio}", user_id)
    else:
        # Se il messaggio non è presente, lo inserisco nel database
        r.zadd("messaggi", {messaggio: 0})
        r.sadd(f"propositori:{messaggio}", user_id)

    print("Proposta salvata con successo!")