#python 3

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)


#comments:
''' ^ - match the start of the line. '''
