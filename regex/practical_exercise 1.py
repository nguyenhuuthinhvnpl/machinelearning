import re

fh = open("C:\Users\hp\PycharmProjects\cs1110virginia\simpsons_phone_book.txt")
for line in fh:
    if re.search(r"J.*Neu", line):
        print(line.rstrip())

fh.close()
