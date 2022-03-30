import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
lista = list()

url = input('Enter -')
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

tags = tree.findall('comments/comment')
#print("count",len(tree.findall('comments/comment')))
for elem in tags:
        tag = elem.find('count').text
        #print("tag:",tag)

        nums = int(tag)
        #lista.append(nums)
        count += nums
       
print("Este es el resultado:",count)



#results = tree.findall('result')
#contar = tree.find('count').text
#print("contar",contar)
#lng = results[0].find('geometry').find('location').find('lng').text
#location = results[0].find('formatted_address').text

#print('contar', contar)
#print(location)