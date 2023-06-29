import redis


def vote_proposal(r: redis.Redis, user_id: int):
    proposal_index = r.zcard('votes')
    if proposal_index == 0:
        print('No proposals found!')
        return

    while True:
        proposal_id = int(input(f'Insert the ID of the proposal you want to vote for (1 - {proposal_index}): '))
        if 1 <= proposal_id <= proposal_index:
            break
        else:
            print('Invalid proposal ID. Please try again.')

    users = r.lrange(f'proposal_votes-{proposal_id}', 0, -1)
    users = [int(user.decode('utf-8')) for user in users]

    if user_id in users:
        print('You have already voted for this proposal!')

    else:
        r.lpush(f'proposal_votes-{proposal_id}', user_id)
        print('Your vote has been recorded successfully!')
