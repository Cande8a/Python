from bs4 import BeautifulSoup
import re

file = input('Enter - ')
html = open(file)
soup = BeautifulSoup(html, "html.parser")
#print("soup---------------------",soup)
# Retrieve all of the anchor tags
#count = 0
#lista = list()
tags = soup('br')
#print(tags)

for tag in tags:
    #print('Contents:',tag.contents[0])
    #print('Attrs:',tag.attrs)
    cut = tag.contents[0].split()
    print("linea",cut)
    #stuff = re.findall('^M.*',cut)
    #print("stuff", stuff)
    #cuts = re.findall('^M',tag)
    
    #cut = tag.contents[0]

#print("cut",cuts)
    #if len(cuts) == 0 : continue    
           
#print("Este es el resultado:",count)