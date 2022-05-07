# from urllib.request import urlopen
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


# import urllib
from bs4 import BeautifulSoup
import csv

# import ssl
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://www.fi.unju.edu.ar/'
# url = 'http://www-math.mit.edu/~gs/'
# url = 'https://www.macro.com.ar/home-page'


# html = urllib.request.urlopen(url)

# print(html)
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('a')
# # print(tags)
# print('Enlaces en la página principal: \r\n')

# for tag in tags:
# 	print(tag.contents, tag.get('href'))

pagina = requests.get(url, verify=False)
print(pagina)
# obtener el contenido de la pagina
htmls = BeautifulSoup(pagina.content, 'html.parser')
# print(htmls)
etiquetas = htmls('a')
urlModificada = ''
listadoUrl = []
for etiqueta in etiquetas:
    url2 = etiqueta.get('href')
    # print(url2)
    if url2 != None:        
        if len(url2) > 1:            
            if url2[0] == '/':
                urlModificada = url.replace(url[-1], '')  # reemplaza el ultimo caracter '/' por un vacio vacio
                url2 = urlModificada+url2                
                # filtrar urls repetidas
                if url2 not in listadoUrl:
                    listadoUrl.append(url2)                
            else:
                if url2[0:5] == 'https':
                    if url2 not in listadoUrl:
                        listadoUrl.append(url2)
for enlace in listadoUrl:
    print(enlace)
