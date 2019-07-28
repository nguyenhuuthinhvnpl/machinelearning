import re

text = """Regular expressions match strings left-to-right. They can be effectively built in that way. The basic questions are

What set of characters or substrings could come first? How do I write those down?
What set of characters or substrings could after the part I’ve already written? How do I write those down?
It can be helpful to write down a few examples and cross them off as you go. We’ll do examples of this later on on this page."""

# the_res = r"[Th]e"
the_res = r"[Th]e"
matcher = re.compile(the_res)
print(matcher)

match = matcher.search(text)
print(match)

for m in matcher.finditer(text):
    print(m, m.groups(), m.group(2))

# InstructorTip\('([^']*)'\)
# [^'] - not a quote
# [^']* - any numer of
# ([^']*) -  as a group
# '\) -- followed by ' and)
# InstructorTip\(' -- preceded by InstructorTip)
