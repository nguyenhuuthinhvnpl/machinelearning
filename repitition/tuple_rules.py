# tuple is not mutable: we can't change anything inside it
t = [1.5, 'yes', 5, 'thing', 281, True]
print(t)
print(" This tuple contains ", len(t), "elements")
print("Element at index [0]", t[0])
print(t + t)
print(t * 4)
print("The elements of tuple between index [3] and [5]", t[3:5])
t[0] = "changed"
print(t)
