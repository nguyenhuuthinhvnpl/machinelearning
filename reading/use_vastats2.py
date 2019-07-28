import urllib.request

url = "http://cs1110.cs.virginia.edu/files/vastats.csv"
stream = urllib.request.urlopen(url)
all_text = stream.read().decode('utf-8')
stream.close()
# print(all_text)

rows = all_text.strip().split('\n')
header = rows[0].split(',')
virginia = rows[1].split(',')

answer = []  # a list of all small (< 10,000 people) places
for row in rows[2:]:
    # print(row.split(','))
    cells = row.split(',')
    population = int(cells[2])
    if population < 10000:
        answer.append(cells[1])
print(answer)
# print(rows)
