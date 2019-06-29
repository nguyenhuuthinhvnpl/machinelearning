costs = {
    'apple': 0.80,
    'car': 20000,
    'missing car': 2000, }

purchases = ['apple', 'apple', 'car', ]

spent = 0
for item in purchases:
    spent += costs[item]

print('I spent ', spent)
