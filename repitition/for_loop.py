s = "hello"
i = 0
while i < len(s):
    print(s[i])
    i += 1

collection = range(len(s))
print(collection)
for i in collection:
    print(s[i])
