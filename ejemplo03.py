import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from tp02 import modulos as procesoTexto
import matplotlib.pyplot as plt


urlPrincipal = 'https://www.pagina12.com.ar'
urlBusqueda = 'https://www.pagina12.com.ar/secciones/ciencia'

def obtenerPeticionUrl(url):
    website = requests.get(url)
    return website

def obtenerTitulo(respPeticion):    
    if respPeticion.status_code == 200:
        pagina = BeautifulSoup(respPeticion.content, 'html.parser')
    ListaNoticias = pagina(
        'article', {'class': 'article-item article-item--teaser'})
    listaTitulos = []
    for noticia in ListaNoticias:
        titulo = noticia.find('h4').find('a').getText()
        listaTitulos.append(titulo)
    return listaTitulos

def obtenerEnlaceSigPagina(respPeticion, urlP=urlPrincipal):
    enlace = []
    if respPeticion.status_code == 200:
        pagina = BeautifulSoup(respPeticion.content, 'html.parser')
        bloqueEnlace = pagina('div', {'class':'articles-list-pager'})
        for elemento in bloqueEnlace:
            e = elemento.find('a',{'class':'next'})['href']
            if e[0] == '/':
                e = urlP + e
            enlace.append(e)
    return enlace

def listarNoticias(url, urlP=urlPrincipal):
    cont = 0
    listaNoticias = []
    web = obtenerPeticionUrl(url)
    enlace= ''
    while cont <= 100:
        if cont == 0:
            listaNoticias.extend(obtenerTitulo(web))
            enlace = obtenerEnlaceSigPagina(web)[0]
            print(enlace)            
        else:
            print('sig pag',enlace)
            pagina = obtenerPeticionUrl(enlace)
            if pagina.status_code == 200:
                print(pagina.status_code)
                listaNoticias.extend(obtenerTitulo(pagina))
                enlace = obtenerEnlaceSigPagina(pagina)[0]
        cont=len(listaNoticias)
    return listaNoticias

# web = obtenerPeticionUrl(urlBusqueda)
# print(web.status_code)
lista100=[]
listaTotal = listarNoticias(urlBusqueda)
print(len(listaTotal))
i = 1
for j in range(100):
    print(j+1,listaTotal[j])
    lista100.append(listaTotal[j])

# unimos todo el texto 
textoTitulos=''
for t in lista100:    
    textoTitulos += t +' '
# print(texto12)
# limpiamos texto signos de puntuacion
textoSinSignosPuntuacion = procesoTexto.eliminarSignosPuntuacion(textoTitulos)
# print(textoSinSignosPuntuacion)
# tokenizar texto
textoTokenizado = procesoTexto.tokenizar(textoSinSignosPuntuacion)
# print(textoTokenizado)
# poner en minuscula todas las palabras
textoEnMinuscula = procesoTexto.ponerMinuscula(textoTokenizado)
# eliminiacion stopwords
textoLimpio = procesoTexto.eliminarStopWords(textoEnMinuscula)
# print(textoLimpio)
# convertimos en texto
textoProcesado = ' '.join(textoLimpio)
print(textoProcesado)
# generar nube de palabras
print('generando nube de palabras ...')
nubePalabra = WordCloud(height=800,width=800, background_color='white', max_words=100, min_font_size=5, collocation_threshold=10).generate(textoProcesado)
nubePalabra.to_file('nube_palabra.png')

plt.figure(figsize=(10,8))
plt.imshow(nubePalabra)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
