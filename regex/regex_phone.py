import re

text = '''The following are extracts from http://en.wikipedia.org

For example, 234-235-5678 or (234) 235-5678 or (234)235-5678
is a valid telephone number with area code 234,
central office prefix (exchange) 235, and line number 5678.
The number 234-911-5678 is invalid, because the central office code
must not be in the form N11. 314-159-2653 is invalid, because the office code
must not begin with 1. 123-234-5678 is invalid, because the NPA must not begin 
with 0 or 1.

The country calling code for all countries participating in the NANP is 1.
In international format, an NANP number should be listed as +1 301 555 0100,
where 301 is an area code (Maryland).'''

phone = r'[2-9][0-9]{2}\-([2-9][0-9]{2}\-)?[0-9]{4}|\([2-9][0-9]{2}\) ?[2-9][0-9]{2}\-[0-9]{4}'

phone_finder = re.compile(phone)
for match in phone_finder.finditer(text):
    print(match.group())
