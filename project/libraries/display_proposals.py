import redis
from libraries.utils.scored_proposals import get_scored_proposals
from libraries.utils.proposal_voters import get_proposal_voters


def display_proposals(r: redis.Redis, get_proposals=False):
    print('=== Proposals ===')

    scored_proposals = get_scored_proposals(r)
    if not scored_proposals:
        print('No proposals found!')
        return

    print('Available proposals:')
    for index, proposal_tuple in enumerate(scored_proposals, start=1):
        proposal = proposal_tuple[0].decode('utf-8')
        _, proposer = get_proposal_voters(r, proposal, get_proposer=True)
        print(f'{index}. {proposal}({proposer}) - {int(proposal_tuple[1])} Votes')

    return scored_proposals if get_proposals else None
