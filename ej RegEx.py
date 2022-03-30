#In this assignment you will read through and
# parse a file with text and numbers. You will
# extract all the numbers in the file and compute
# the sum of the numbers.

import re

name = input("Enter file:")
if len(name) < 1:
    name = "RegEx Assignment.txt"
handle = open(name)
count = 0
lista = list()
for line in handle:
    search = re.findall('[0-9]+',line)
    if len(search) == 0 : continue
    #print(search)

    
    
    for num in search:
        nums = int(num)
        #print("esto es nums",nums)
        lista.append(nums)
        count = sum(lista)
        
print("Este es el resultado:",count)
        






