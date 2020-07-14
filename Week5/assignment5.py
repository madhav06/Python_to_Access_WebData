#Python3
# We test it with sameple data: http://py4e-data.dr-chuck.net/comments_42.xml
# And we test it again with actual data: http://py4e-data.dr-chuck.net/comments_772916.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter location: ')
html = urllib.request.urlopen(link).read().decode()

print('Retriving', link)
print('Retrieved', len(html), 'characters')

#data calculation
count = 0
sum = 0

data = ET.fromstring(html)
tags = data.findall('comments/comment')

for tag in tags:
    count += 1
    sum += int(tag.find('count').text)

print('Counting:', count)
print('Sum:', sum)
