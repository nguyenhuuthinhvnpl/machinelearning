chipotle = 0
rev_soup = 0
mellow = 0
lemongrass = 0
other = 0


def vote(restaurant):
    """tabulates one vote for a lunch place"""
    global rev_soup, chipotle, mellow, lemongrass, other
    if restaurant.lower() in ["chipotle", "burrito"]:
        chipotle += 1
    elif restaurant.lower() in ["rev soup", "revolutionary soup", "soup"]:
        rev_soup += 1
    elif restaurant.lower() in ["mellow mushroom", "mellow", "pizza"]:
        mellow += 1
    elif restaurant.lower() in ["lemongrass", "thai"]:
        lemongrass += 1
    else:
        other += 1


def winner():
    """Determines where we will be going to lunch, gives multiple in a list if a tie"""
    max_votes = max(chipotle, rev_soup, mellow, lemongrass, other)
    winners = []
    if chipotle == max_votes:
        winners.append("Chipotle")
    if rev_soup == max_votes:
        winners.append("Revolutionary Soup")
    if mellow == max_votes:
        winners.append("Mellow Mushroom")
    if lemongrass == max_votes:
        winners.append("Lemongrass")
    if other == max_votes:
        winners.append("other")
    return winners


vote("chipotle")
vote("chipotle")
vote("chipotle")
vote("chipotle")
vote("Mellow")
vote("Mellow")
vote("Mellow")
vote("Mellow")
vote("soup")
vote("LeMoNGRASs")
print(chipotle, mellow, rev_soup, lemongrass)
print(winner())
