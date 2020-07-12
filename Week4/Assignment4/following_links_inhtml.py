#Python3
#Following Links in HTML using BeautifulSoup
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Access website
url = "http://py4e-data.dr-chuck.net/known_by_Rahma.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
all_num_list = list()
link_position = 18
Process_repeat = 7

#Retrieve all anchor tags
tags = soup('a')
while Process_repeat - 1 >= 0:
    print("Process round", Process_repeat)
    target = tags[link_position - 1]
    print("target:", target)
    url = target.get('href', 2)
    print("Current url", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    Process_repeat = Process_repeat - 1
