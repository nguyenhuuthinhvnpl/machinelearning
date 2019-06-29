brunelle = 0
cohoon = 0
dill = 0
praphamontripong = 0
tychonievich = 0
other = 0


def vote(candidate):
    """Record a vote for 111x professor of the semester
    """
    global brunelle, cohoon, dill, praphamontripong, tychonievich, other

    if candidate.lower() in ['nathan', 'nate', 'brunelle', 'nathan brunelle']:
        brunelle += 1
    elif candidate.lower() in ['jim', 'james', 'cohoon', 'jim cohoon']:
        cohoon += 1
    elif candidate.lower() in ['craig', 'dill', 'craig dill']:
        dill += 1
    elif candidate.lower() in ['upsorn', 'praphamontripong', 'upsorn praphamontripong']:
        praphamontripong += 1
    elif candidate.lower() in ['luther', 'tychonievich', 'luther tychonievich']:
        tychonievich += 1
    else:
        other += 1


def winner():
    best = []
    if brunelle == max([brunelle, cohoon, dill, praphamontripong, tychonievich]):
        best.append('brunelle')
    if cohoon == max([brunelle, cohoon, dill, praphamontripong, tychonievich]):
        best.append('cohoon')
    if dill == max([brunelle, cohoon, dill, praphamontripong, tychonievich]):
        best.append('dill')
    if praphamontripong == max([brunelle, cohoon, dill, praphamontripong, tychonievich]):
        best.append('praphamontripong')
    if tychonievich == max([brunelle, cohoon, dill, praphamontripong, tychonievich]):
        best.append('tychonievich')
    return best


vote('tychonievich')
vote('tychonievich')
vote('tychonievich')
vote('brunelle')
vote('brunelle')
vote('brunelle')

print(winner())
