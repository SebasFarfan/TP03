import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from tp02 import modulos as procesoTexto
import matplotlib.pyplot as plt
from colorama import Fore, Style, init 

init(autoreset=True)

urlPrincipal = 'https://www.pagina12.com.ar'
urlBusqueda = 'https://www.pagina12.com.ar/secciones/ciencia'

def obtenerPeticionUrl(url):
    '''
    Método que realiza una petición Get para obtener la pagina. 
    Arg: 
    url: [str]
    Return:
    website: [requests.Response] 
    '''
    website = requests.get(url)
    return website

def obtenerTitulo(respPeticion):
    '''
        Método que obtiene el contenido de los titulos de esa página. 
        Arg: 
            respPeticion: [requests.Response]
        Return:
           listaTitulos: [list] 
    '''   
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
    '''
        Método que obtiene el enlace de la siguiente página.
        Args:
            respPeticion: [requests.Response]
            urlP: [str] url principal 
        Return: 
            enlace: [list] 
    '''
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

def listarNoticias(url, cantidad, urlP=urlPrincipal):
    '''
        Método que en base a una direccion web (url) va a obtener una determinada cantidad de
        títulos.\n
        Args: 
            url: [str] url donde buscar.
            cantidad: [int] cantidad de titulos a obtener.
            urlP: [str] url prinipal en caso que se tenga un paginador.
        Return:
           listaNoticias: [list] lista con los títulos obtenidos. 
    '''
    cont = 0
    listaNoticias = []
    web = obtenerPeticionUrl(url)
    enlace= ''
    while cont <= cantidad:
        if cont == 0:
            print(url)
            listaNoticias.extend(obtenerTitulo(web))
            enlace = obtenerEnlaceSigPagina(web)[0]
            # print(enlace)            
        else:
            print('sig pag ->',enlace)
            pagina = obtenerPeticionUrl(enlace)
            if pagina.status_code == 200:
                print(pagina.status_code)
                listaNoticias.extend(obtenerTitulo(pagina))
                enlace = obtenerEnlaceSigPagina(pagina)[0]
        cont=len(listaNoticias)
    return listaNoticias

def generarNubePalabras(texto):
    '''
        Método que genera una nube de palabras usando WordCloud, lo dibuja y lo muestra por pantalla.
        Arg: 
            texto: [str] 
    '''
    nubePalabra = WordCloud(height=800,width=800, 
                            background_color='white', 
                            max_words=100, min_font_size=5, 
                            collocation_threshold=10).generate(texto)
    nubePalabra.to_file('nube_palabra.png')
    # grafico
    plt.figure(figsize=(10,8))
    plt.imshow(nubePalabra)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()


# --------------------------------- principal ------------------------------------
lista100=[]
cantidadNoticias = 100
listaTotal = listarNoticias(urlBusqueda, cantidadNoticias)  # urlBusqueda = 'https://www.pagina12.com.ar/secciones/ciencia'
print(len(listaTotal))
for j in range(100):
    print(j+1,'-',listaTotal[j])
    lista100.append(listaTotal[j])

# unimos todo los títulos en un texto [str] 
textoTitulos=''
for titulo in lista100:
    textoTitulos += titulo +' '

# limpiamos texto signos de puntuacion
textoSinSignosPuntuacion = procesoTexto.eliminarSignosPuntuacion(textoTitulos)

# tokenizar texto
textoTokenizado = procesoTexto.tokenizar(textoSinSignosPuntuacion)

# poner en minuscula todas las palabras
textoEnMinuscula = procesoTexto.ponerMinuscula(textoTokenizado)

# eliminiacion stopwords
textoLimpio = procesoTexto.eliminarStopWords(textoEnMinuscula)

# convertimos en texto
textoProcesado = ' '.join(textoLimpio)

# generar nube de palabras
print('generando nube de palabras ...')
generarNubePalabras(textoProcesado)
