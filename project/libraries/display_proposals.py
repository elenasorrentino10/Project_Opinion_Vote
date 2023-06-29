import redis
import json


def display_proposals(r: redis.Redis):
    proposal_keys = r.keys('proposal:*')
    proposal_keys.reverse()

    if proposal_keys:

        proposals = [r.hgetall(proposal) for proposal in proposal_keys]
        print(proposals)

        #proposals = [proposal[b'text'].decode('utf-8') for proposal in proposals]

        #proposals = [f'{index + 1}) {proposal} ' for index, proposal in enumerate(proposals)]

        #print('Proposals:')
        #print('\n'.join(proposals))
    else:
        print('No proposals found!')
