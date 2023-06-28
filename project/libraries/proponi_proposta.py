import redis

def scrivi_proposta(nome_utente):
    messaggio = input("Inserisci un nuovo messaggio: ")

    # Controllo se il messaggio è già presente nel database
    if db.zrank("messaggi", messaggio) is not None:
        # Se il messaggio è già presente, aggiungo l'utente come propositore del messaggio
        db.sadd(f"propositori:{messaggio}", nome_utente)
    else:
        # Se il messaggio non è presente, lo inserisco nel database
        db.zadd("messaggi", {messaggio: 0})
        db.sadd(f"propositori:{messaggio}", nome_utente)

    print("Proposta salvato con successo!")