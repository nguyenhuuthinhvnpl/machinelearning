d = {}

to_remember = input("What shall I remember for you ?")
what_about_it = input(" What shall I remind you about ?")
d[to_remember] = what_about_it

print(d)

reminder = input("Tell me what you want to be remind: ")
print(d[reminder])
print(d)
