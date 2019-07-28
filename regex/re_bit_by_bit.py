import re

# goal:match money, like $23 and $45.34 and $5,799,999.99
text = '''match money, like $23 and $45.34 and $5,799,999.99 but not to match 1.234 or $12234345235435 ' \
         or $.45 or $0.456'''

dollar = r'\$'
cents = r'\.[0-9][0-9]\b'
number1 = r'[0-9][0-9]?[0-9]?'
number2 = r',[0-9][0-9]?[0-9]?'
combined = '(' + dollar + ')' + number1 + '(' + number2 + ')*' + '(' + cents + ')?'

money = re.compile(combined)
for thing in money.finditer(text):
    print(thing)
