import re

# split a list that uses ,  and "and"
ex1 = "red, green, yellow, blue"
ex2 = "vanilla, chocolate, and blueberry"
ex3 = "vanilla, chocolate and blueberry"

# re for the delimeter
between = re.compile(r", |, and | and")
# for m in between.finditer(ex1 + ex2 + ex3):
#   print(m)

for text in ex1, ex2, ex3:
    print(text, between.split(text))
