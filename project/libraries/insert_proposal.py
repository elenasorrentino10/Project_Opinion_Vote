import redis
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json


def insert_proposal(r: redis.Redis, username: str):
    proposal = input('Insert your proposal: ').lower().strip()

    # if find_similarity(r, proposal):
    #     print('This proposal is very similar to another one.')
    #     choice = input('Do you want to save it anyway? (y/n) ').lower().strip()

    #     if choice != 'y':
    #         print('Proposal not saved!')
    #         return

    if r.hexists('proposals', proposal):
        print('This proposal already exists!')
        print('Maybe you want to vote for it instead?')
        return

    # Create a dictionary for the nested hash map
    proposal_data = {
        'proposer': username,
        'voters': username
    }
    # Convert the dictionary to a JSON string
    proposal_json = json.dumps(proposal_data)
    # Create a proposal, add it to the proposals hmap and set the proposer as the only voter for now
    r.hset('proposals', proposal, proposal_json)
    # Create an entry for the proposal in the votes sorted set and set the score to 1
    r.zadd('votes', {proposal: 1})

    print('Proposal added successfully!')


def find_similarity(r: redis.Redis, proposal: str) -> bool:
    # Get all the proposals from the proposals hmap
    proposals = r.hgetall('proposals').keys()
    proposals = [proposal.decode() for proposal in proposals]
    proposals.append(proposal)

    if len(proposals) != 1:
        vectorizer = CountVectorizer().fit_transform(proposals)
        similarity = cosine_similarity(vectorizer[-1], vectorizer[:-1])

        return similarity[0][0] > 0.2
    return False
