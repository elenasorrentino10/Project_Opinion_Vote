import redis


def get_scored_proposals(r: redis.Redis):
    proposals = [proposal_tuple for proposal_tuple in r.zrevrange('votes', 0, -1, withscores=True)]
    return proposals
