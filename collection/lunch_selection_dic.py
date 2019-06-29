votes = {"chipotle": 0,
         "rev_soup": 0,
         "mellow": 0,
         "lemongrass": 0,
         "other": 0
         }


def vote(restaurant, votes):
    """tabulates one vote for a lunc    h place"""
    strategy = """Add restaurants to the votes dict
               and add one to the values associated with the key in restautant 
               """
    votes[restaurant.lower()] += 1


def winner():
    """Determines where we are going to lunch, give a multiple in a list if a tie"""
    plan = """find how many votes was the max among all give a list  of all restaurants 
    tied for first place."""
    max_votes = max(votes.values())
    winners = []
    for restaurant in votes:
        if votes[restaurant] == max_votes:
            winners.append(restaurant)


vote("chipoletle", votes)
vote("chipoletle", votes)
vote("chipoletle", votes)
vote("chipoletle", votes)

print(votes)
