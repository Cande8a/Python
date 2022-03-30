from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
print("primer url",url)

position = input('Enter position - ')
pos_1 = int(position)
times = int(input('Enter times - '))

#index = 0


count_2 = 0 #Contador del ciclo for externo

lista_1 = list() #Lista que contiene los hmtl
lista_2 = list() #Lista que contiene los nombres dentro del html de lista_1

nombre = str()
next_link = str()

while count_2 < times:
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup('a')
        #print(tags)
        count_1 = 1 #Contador del ciclo for interno
        for tag in tags:
                links = tag.get('href', None)
                cut = links.split()
                print("count :",count_1, " post :", pos_1)
                if count_1 == pos_1:
                        next_link=cut[0]
                        nombre = tag.contents[0]
                        print("Link ",next_link)
                        print("Nombre",nombre)
                        lista_2.append(nombre)
                        break
                count_1 += 1
        print("valores", count_2 , " ", count_1, " ", times)
        url = next_link # Proximo html
        count_2 += 1
        print("proximo url", url)
print("Nombres :",lista_2)                
        
        
        #print(" Primer link :",lista_1[count_2]) 
         
        #url = lista_1[count_2] # Proximo html
        #print("proximo url", url)
        #count_2 += 1
        #lista_2.append(nombre) # nombre del extraido del html
        
        



#for link in lista_1:
        #print("Link :"+link)
        #


#for element in lista:
#        print("elemento de la lista : ",element)
#print("Tamaño de la lista 18: ",lista[18])     
        #stri = cut[0]
        #print("stri",stri)

        #cuts = re.findall('by_(.*).html',stri)
        #print("este es el corte---------------",cuts)

        #print('Contents:',tag.contents[0])






#count = 0
#position = 0
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
    #links = tag.get('href', None)
    #cut = links.split()
    #print("links-------------------",cut)
    
    #stri = cut[0]
    #print("stri",stri)

    #cuts = re.findall('by_(.*).html',stri)
    #print("este es el corte---------------",cuts)

    #hasta aca, me devuelve OK links y nombres
    
    #listas = lista.append(cut)
    #print("lista--------------", listas)

    #cuts = cut.contents[0]
    #print("este es el corte---------------",cuts)
    
    #print("tipo de cut",type(cut[0]))
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs