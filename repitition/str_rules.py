s = "this is some text"
#     0123456789

print(s)
print("This string contains", len(s), "characters.")
print("The character at index 0 was", s[0])
print("The character at index 1 was", s[1])
print("The last character is", s[16])
print("The last character is", s[len(s) - 1])
print("The last character is", s[-1])
print("The last character is", s[-2])
# print("The last character is", s[17])

s1 = "this is "
s2 = " this is"
s3 = s1 + s2
print(s3)
print(s1 * 4)
print("The characters between index 3 and 6 of s1 are", s[3:6])
print("The characters between index 3 and 6 of s1 are", s[:6])
print("The characters between index 3 and 6 of s1 are", s[:-6])
print("The characters between index 3 and 6 of s1 are", s[3:-6])
