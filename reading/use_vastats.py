# read from the web
import urllib.request

url = "http://cs1110.cs.virginia.edu/files/vastats.csv"

# open
with urllib.request.urlopen(url)  as stream:
    # read
    # the first line with  .readline()
    # header = stream.readline().decode('utf-8').strip().split(',')
    # header_bytes = stream.readline()
    # header_text =  header_bytes.decode('utf-8')
    # no_newline = header_text.strip()
    # header  = no_newline.split(',')

    header = stream.readline().decode('utf-8').strip().split(',')
    print(header)
    ohui = header.index('Occupied Housing Units')
    print(ohui)
    virginia = stream.readline()
    # most_people = stream.readline().decode('utf-8').strip().split(',')[6]
    most_people = -1
    where_lived = 'nowhere '
    ohu_sum = 0
    ohu_total = 0
    ohu_count = 0
    # a line a  t a time with for
    for line in stream:
        row = line.decode('utf-8').strip().split(',')
        # only consider  rows that are not "N" type
        if row[0] == 'A':  # != 'N':
            # look for 5-9 age range
            five_to_nine = int(row[6])
            # print(five_to_nine)
            ohu = int(row[ohui])
            ohu_sum += five_to_nine / ohu
            ohu_count += 1
            print(five_to_nine / ohu)
            if five_to_nine > most_people:
                most_people = five_to_nine
                where_lived = row[1]

    print('up to', most_people, 'in', where_lived)
    print('There were', (ohu_sum / ohu_count), '5-9 year old per housing unit')
# decode
# process
# close

# csv with header row
