def apply_inflation(my_dict):
    ''''increase the price of each item in dictionary by 10%
    '''

    for item in my_dict.keys():
        my_dict[item] *= 1.1


def print_items(my_dict):
    inventory = []
    for pair in my_dict.items():
        print(pair)
        inventory.append(pair[0])
    return inventory


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

apply_inflation(d)
cost = 0
for item in purchases:
    cost += d[item]

print(cost)
print_items(d)
print(print_items(d))
