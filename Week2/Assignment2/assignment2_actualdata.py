#python 3

import re

handle = open('regex_sum_772912.txt')
new_list = []
for line in handle:
    x = re.findall('[0-9]+', line)
    new_list.extend(x)

#this code should be used:

# some_list = [int(i) for i in new_list]
# add = sum(some_list)
#
# print(add)

# we can also code like this:

k = [int(i) for i in new_list]
add = sum(k)
print(add)
