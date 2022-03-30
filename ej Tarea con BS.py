from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
count = 0
lista = list()
tags = soup('span')
#print(tags)
for tag in tags:
    cut = tag.contents[0]
    cuts = re.findall('[0-9]+',cut)
    if len(cuts) == 0 : continue    
    
    for num in cuts:
        nums = int(num)
        #print("esto es nums",nums)
        lista.append(nums)
        count = sum(lista)
        
print("Este es el resultado:",count)