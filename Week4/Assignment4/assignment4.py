#Python3
# Scraping Numbers from HTML using Beautiful Soup

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('span')
numlist = list()
for tag in tags:
    #Look at parts of tag
    y = str(tag)
    num = re.findall('[0-9]+', y)
    numlist = numlist+num

sum = 0
for i in numlist:
    sum = sum + int(i)

print(sum)
