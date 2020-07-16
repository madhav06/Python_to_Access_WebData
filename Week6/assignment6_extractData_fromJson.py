#Python3
# This assignemt is about: Extracting Data from JSON

import urllib.request, urllib.parse, urllib.error
import json

#Data collection
link = input('Enter location: ')
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

_count = 0
_sum = 0

for item in js['comments']:
    _count += 1
    _sum += int(item['count'])

print('Count:',  _count)
print('Sum:', _sum)
