import redis
from libraries.utils.proposal_voters import get_proposal_voters, set_proposal_voters
from libraries.utils.scored_proposals import get_scored_proposals
from libraries.display_proposals import display_proposals


def vote_proposal(r: redis.Redis, username: str):
    print('=== Vote a proposal ===')
    
    proposals = display_proposals(r, get_proposals=True)

    while True:
        try:
            proposal_index = int(input('Enter the index of the proposal you want to vote: ')) - 1  # -1 because the index starts from 1
            if not 0 <= proposal_index < len(proposals):  # if the index is not in the range of the proposals list
                raise IndexError
            proposal = proposals[proposal_index][0].decode('utf-8')
            break
        except ValueError:
            print('Invalid proposal!')
        except IndexError:
            print('Invalid proposal index!')

    proposal_names = [proposal[0].decode('utf-8') for proposal in proposals]
    if proposal not in proposal_names:
        print('Invalid proposal!')
        return
    
    proposal_voters = get_proposal_voters(r, proposal)
    if username in proposal_voters:
        print('You already voted this proposal!')
        return
    
    r.zincrby('votes', 1, proposal)
    proposal_voters.append(username)
    set_proposal_voters(r, proposal, proposal_voters)
    print('Vote submitted successfully!')
