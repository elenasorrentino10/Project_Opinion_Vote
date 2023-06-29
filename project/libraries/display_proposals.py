import redis


def display_proposals(r: redis.Redis):
    proposals = r.keys('proposal:*')
    if not proposals:
        print('No proposals found!')
        return
    proposals = [r.hgetall(proposal) for proposal in proposals]
    proposals = [proposal[b'text'].decode('utf-8') for proposal in proposals]

    users = r.keys('user:*')
    if not users:
        print('No users found!')
        return
    users = [r.hgetall(user) for user in users]
    users = [user[b'username'].decode('utf-8') for user in users]

    votes = r.zrange('votes', 0, -1, withscores=True)
    if not votes:
        print('No votes found!')
        return

    for index, data in enumerate(zip(proposals, users, votes)):
        proposal, user, vote = data
        print(f'Proposal {index} | User: {user} | Votes: {vote} \n {proposal}')
