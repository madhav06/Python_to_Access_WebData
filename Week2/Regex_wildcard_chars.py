#python 3

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line)


#comments:
''' ^ - match the start of the line.
. - followed by any number of character
* - zero or more character '''
