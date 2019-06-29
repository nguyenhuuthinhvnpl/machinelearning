plan = """
dict of results -- election
    keys: candidate
    values: number of votes
vote(candidate, election)
    get votes for this candidate
    add 1
    set votes for this candidate 
    
ballot = [
        "Luther Tychonievich",
        "Jame Cohoon",      
]
    
won(election)
"""
names = {"luther": "tychonievich",
         "jim": "cohoon",
         "james": "cohoon"}


def vote(candidate, election):
    """
    Record a vote for 111x professor of the semester
    :param candidate:
    :param election:
    :return:
    """
    candidate = candidate.lower().strip()
    if candidate in names:
        candidate = names[candidate]

    if candidate in election:
        votes = election[candidate]
        votes += 1
        election[candidate] = votes
    else:
        election[candidate] = 1  # this vote is only vote


def won(election):
    """return the list of candidates with the most votes"""
    best = []
    most_votes = max(election.values())
    # find candidate who won, by
    # look at  each key: key: value pair, for each
    # check which of pair  is the biggiest
    for item in election.items():
        candidate, votes = item
        if vote == most_votes:
            best.append(candidate)

    return best


# Check the result
best111x = {}
vote('tychonievich', best111x)
vote('tychonievich', best111x)
vote('brunelle', best111x)
vote('Luther', best111x)
vote('brunelle', best111x)
vote('brunelle', best111x)
print(best111x)
print(won(best111x))
