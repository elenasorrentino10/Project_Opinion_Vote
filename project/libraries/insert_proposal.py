import redis
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def insert_proposal(r: redis.Redis, user_id: int):
    proposal_id = r.zcard('votes') + 1
    proposal = input('Insert your proposal: ').lower().strip()

    if find_similarity(r, proposal):
        print('This proposal is too similar to another one. Please try again.')
        choice = input('Do you want to save it anyway? (y/n) ').lower().strip()

        if choice != 'y':
            print('Proposal not saved!')
            return

    r.hset(f'proposal:{proposal_id}', 'user', user_id)
    r.hset(f'proposal:{proposal_id}', 'text', proposal)
    r.zincrby('votes', 1, proposal_id)
    r.lpush(f'proposal_votes-{proposal_id}', user_id)
    print('Proposal saved successfully!')


def find_similarity(r: redis.Redis, proposal: str) -> bool:
    proposals = r.keys('proposal:*')
    proposals = [r.hgetall(proposal) for proposal in proposals]
    proposals = [proposal[b'text'].decode('utf-8') for proposal in proposals]
    proposals.append(proposal)

    if len(proposals) == 1:
        return False
    else:
        vectorizer = CountVectorizer().fit_transform(proposals)
        similarity = cosine_similarity(vectorizer[-1], vectorizer[:-1])

        return similarity[0][0] > 0.2
