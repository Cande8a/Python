import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0

url = input('Enter -')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print("data", data)
info = json.loads(data)

for i in range(50):
    dicc = info["comments"][i]['count']
    print("extract", dicc)
    i = i + 1 
    count += dicc
       
print("Este es el resultado:",count)