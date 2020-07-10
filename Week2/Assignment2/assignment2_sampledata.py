#python 3

import re

handle = open('regex_sum_42.txt')
l = []
for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    l.extend(x)

j = [int(i) for i in l]
add = sum(j)
print(add)
