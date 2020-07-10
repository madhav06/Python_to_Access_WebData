#python 3

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print(line)


#comments:
''' ^ - match the start of the line.
\S - Match any non-whitespace character
+ - one or more times '''
