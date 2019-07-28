a = '1,2,ye,why?'
b = a.split(',')
print(a, b)
c = ';'.join(b)
print(c)

# for i in range(len(a)-1,0, -1):
#     letter = a[i]
#     print(letter)
#
# for i in reversed(range(len(a)-1,0, -1)):
#     letter = a[i]
#     print(letter)

for i in reversed(range(len(a) - 1, -1, -1)):
    letter = a[i]
    print(letter)

i = len(a) - 1
while i >= 0:
    print(a[i])
    i -= 1

x = '  this is a text.   '
print(x.strip())
print(x)
y = x.replace(' ', '')
print(y)

x = [1, 2, 4, 8, 16]
print(x)
x_popped = x.pop(2)
print(x_popped)

dic_x = {'x': 1, 'y': 2, 'z': 3}
print(dic_x)
z = dic_x.pop('z')
print(z)
print(dic_x)

# check a string
x_string = "this is a test"
print(x_string)

# x_string.pop(2) # error
print(x_string)

questions = """when to tuple
        never (almost)
        + key of a dict to be a collection, use a tuple
        + if a built-in function  returns one, use it
        
        """

x_list = [1, 2, 4, 8, 16]
print(x_list)
x_list.append(32)
print(x_list)
dic_x["This is new key"] = 123456789
print(dic_x)
