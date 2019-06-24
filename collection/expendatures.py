d = {}
d['apple'] = 0.9
d['bread'] = 1.2
d['milk'] = 3.0
d['steak'] = 400

purchases = ['apple', 'steak', 'milk', 'apple', 'milk']

# for each of my purchases, look up its cost, and add all those together
cost = 0
for item in purchases:
    cost += d[item]

print(cost)
