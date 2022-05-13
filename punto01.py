import csv

import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

# para no mostrar la advertencia de certificado no valido
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# url a analizar
url = 'https://www.fi.unju.edu.ar/'
listadosEnlacesNivel2=[]
listadoTotal=[]

def obtenerEnlaces(urlnivel, urlOriginal='https://www.fi.unju.edu.ar/', listaEnlaces=listadoTotal):
    '''
        Método que obtiene los enlaces de una pagina web
        parámetros: 
            urlnivel: str dirección de una página web
            urlOriginal: str dirección de la pagina que se está analizando
            listaEnlaces: list listado de enlaces 
        return: 
            list [] lista de enlaces
    '''    
    pagina = requests.get(urlnivel, verify=False)
    # print(pagina)
    # obtener el contenido de la pagina
    htmls = BeautifulSoup(pagina.content, 'html.parser')
    etiquetas = htmls('a')
    urlModificada = ''
    listadoUrl = []
    for etiqueta in etiquetas:
        enlace=etiqueta.get('href')
        if enlace != None:
            if len(enlace) > 1:
                if enlace[0] == '/':
                    urlModificada=urlOriginal[0:len(urlOriginal)-1]
                    enlace = urlModificada + enlace
                    # filtrar enlaces repetidos
                    if enlace not in listaEnlaces:
                        listadoUrl.append(enlace)
                        listaEnlaces.append(enlace)
                        print(enlace)
                else:
                    if enlace[0:5] == 'https':
                        if enlace not in listaEnlaces:
                            listadoUrl.append(enlace)
                            listaEnlaces.append(enlace)
                            print(enlace)
    return listadoUrl

# ---------------------------- principal ------------------------------------
print('-'*80)
print('Obteniendo los enlaces de nivel 1')
listadoNivel1 = obtenerEnlaces(url)
print(len(listadoNivel1),'Enlaces')
print('-'*80)
cont = 0

for enlace in listadoNivel1:
    cont += 1
    print('-'*70)
    print(cont,'- enlace:',enlace)
    print('Obteniendo enlace de nivel 2')
    try:
        listadoNivel2=obtenerEnlaces(enlace)
        print(len(listadoNivel2),'Enlaces de nivel 2')    
        listadosEnlacesNivel2.append(listadoNivel2)
    except requests.exceptions.ConnectionError:
        print('no se puede acceder')
    
print('\n\n')
print('-'*80)
print('terminó de procesar los',len(listadoNivel1),'enlaces')

print('Guardando en archivo salida.csv...')
encabezado1=['Nivel 1']
encabezado2=['Nivel 2']
with open('./salida.csv','w') as csv_file:
    csv_write = csv.writer(csv_file,dialect='excel')
    csv_write.writerows(zip(encabezado1,encabezado2))
    csv_write.writerows(zip(listadoNivel1,listadosEnlacesNivel2))
print('terminado')
