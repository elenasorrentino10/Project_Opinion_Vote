def display_proposals(r):
    proposals = r.zrange('proposals', 0, -1, withscores=True)

    if not proposals:
        print("There are no proposals to vote yet.")
    else:
        print("Proposals to vote:")
        for index, proposal in enumerate(proposals):
            print(f"{index + 1}) {proposal[0].decode()} - {int(proposal[1])} votes")
