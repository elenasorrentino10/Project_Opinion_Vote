def vote_proposal(r, user_id):
    messaggio = input("Insert your proposal: ")

    # Controllo se l'utente ha già votato il messaggio
    if r.sismember(f"voti:{messaggio}", user_id):
        print("You've already voted this proposal!")
    else :
        # Incremento il numero di voti del messaggio nel database
         r.zincrby("messaggi", 1, messaggio)
        # Aggiungo l'utente ai votanti del messaggio
         r.sadd(f"voti:{messaggio}", user_id)

         print("Vote saved successfully!")
