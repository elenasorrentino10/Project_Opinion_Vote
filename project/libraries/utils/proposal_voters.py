import redis
import json


def get_proposal_voters(r: redis.Redis, proposal: str, get_proposer: bool = False):
    voters_str = r.hget('proposals', proposal).decode('utf-8')
    # convert the JSON string to a dictionary
    voters_dict = json.loads(voters_str)
    # get the voters from the dictionary
    proposal_voters = voters_dict['voters'].split(',')
    # get the proposer from the dictionary
    if get_proposer:
        proposal_proposer = voters_dict['proposer']
    return proposal_voters if not get_proposer else (proposal_voters, proposal_proposer)


def set_proposal_voters(r: redis.Redis, proposal: str, voters: list):
    # Create a dictionary for the nested hash map
    data_dict_string = r.hget('proposals', proposal)  # return '{'proposer': 'username', 'voters': 'username'}'
    # Convert JSON string to a dictionary
    data_dict = json.loads(data_dict_string)
    # Get the proposer from the dictionary
    proposer = data_dict['proposer']
    # Create a dictionary for the nested hash map
    proposal_data = {
        'proposer': proposer,
        'voters': ','.join(voters)
    }

    # Convert the dictionary to a JSON string
    proposal_json = json.dumps(proposal_data)
    # Create a proposal, add it to the proposals hmap and set the proposer as the only voter for now
    r.hset('proposals', proposal, proposal_json)
