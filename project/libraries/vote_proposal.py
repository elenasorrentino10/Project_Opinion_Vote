def vote_proposal(r, user_id):
    proposal = input("Insert your proposal: ")

    # Check if the message is already present in the database
    if r.sismember(f"votes:{proposal}", user_id):
        print("You've already voted this proposal!")
    else :
        # Increment the score of the message
         r.zincrby("proposals", 1, proposal)
        # Add the user to the list of voters
         r.sadd(f"votes:{proposal}", user_id)

         print("Vote saved successfully!")
