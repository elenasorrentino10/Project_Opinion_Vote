def insert_proposal(r, user_id):
    proposal = input("Insert your proposal: ")

    # Check if the message is already present in the database
    if r.zrank("proposals", proposal) is not None:
        # If the message is already present, add the user to the list of proposers
        r.sadd(f"proposer(s):{proposal}", user_id)
    else:
        # If the message is not present, add it to the database
        r.zadd("proposals", {proposal: 0})
        r.sadd(f"proposer(s):{proposal}", user_id)

    print("Proposal inserted successfully!")
