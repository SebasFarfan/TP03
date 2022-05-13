import requests
from bs4 import BeautifulSoup
from tp02 import modulos as operacionTexto
from colorama import Fore, Style, init

init(autoreset=True)
url = 'https://www.eltribuno.com/jujuy/seccion/tecnologia'
urlPrincipal = 'https://www.eltribuno.com'


def obtenerEnlaceNoticia(enlacePrincipal=urlPrincipal, enlaceBusqueda=url):
    '''
    Método que obtiene todos los enlaces de un determiando bloque html de una página.
    parámetros:
        enlacePrincipal: [str] dirección url principal 'https://www.eltribuno.com'.
        enlaceBusqueda: [str] dirección url en la cual se va a buscar las url.
    return: listadoEnlaces [list]
    '''
    listadoEnlaces = []
    website = requests.get(enlaceBusqueda)
    print(website.status_code)
    if website.status_code == 200:
        pagina = BeautifulSoup(website.content, 'html.parser')
        bloqueNoticias = pagina(
            'div', {'class': 'nota_ item-pack minuto_foto'})
        for elemento in bloqueNoticias:
            enlace = elemento.find('h1').find('a', href=True)['href']
            if enlace[0] == '/':
                enlace = enlacePrincipal+enlace
            listadoEnlaces.append(enlace)
        print('Acceso Satisfactorio!!')
    return listadoEnlaces

# print(obtenerEnlaceNoticia())


def obtenerHeader(bloque):
    '''
    Método que obtiene el título y resumen de la noticia. 
    Parámetros: 
        bloque: [bs4.element.Tag | bs4.element.NavigableString] bloque html. 
    Return: listaHeader [list] lista cuyos elementos son el título y resumen 
    '''
    listaHeader = []
    titulo = bloque.find(
        'h1', {'class': 'title newDetailTextChange'}).getText()
    resumen = bloque.find(
        'p', {'class': 'preview newDetailTextChange'}).getText()
    listaHeader.append(titulo)
    listaHeader.append(resumen)
    return listaHeader


def obtenerImagen(bloque):
    '''
    Método que obtiene la direccion de archivo de imagen.
    Parámetro: bloque [bs4.element.Tag | bs4.element.NavigableString] bloque html. 
    Return: [str] imagen: dirección url de la imagen
    '''
    listaImg = []
    imagen = bloque.find('img').get('data-src')
    return imagen


def obtenerCuerpoNoticia(bloque):
    '''
    Método que obtiene el cuerpo de la noticia.
    Parámetro: bloque [bs4.element.Tag | bs4.element.NavigableString] bloque html. 
    Return: [str] cuerpo: texto que es el cuerpo de la noticia.
    '''
    texto = bloque.find_all('p')
    cuerpo = ''
    for p in texto:
        cuerpo += p.text+'\n'
    return cuerpo


def obtenerPagina(enlace):
    '''
    Método que obtiene la estructura html de una página web. 
    Parámetro: [str] enlace: que es la url a analizar.
    Return: [BeautifulSoup] pagina: estructura html de la página.
    '''
    website = requests.get(enlace)
    print(website.status_code)
    if website.status_code == 200:
        pagina = BeautifulSoup(website.content, 'html.parser')
        print('Acceso Satisfactorio !!')
    return pagina


def obtenerDatosPagina(enlace):
    '''
    Método que obtiene los datos de una página (título, resumen, imagen, cuerpo de la noticia)
    Parámetro: [str] enlace: url de la página. 
    Return: [list] listadoContenidoPagina, que es la lista cuyos elementos son título, resumen, imagen y cuerpo de una noticia. 
    '''
    listadoContenidoPagina = []
    estructuraHTML = obtenerPagina(enlace)
    print('-'*10, 'obteniendo datos de página', '-'*10)
    bloqueHeader = estructuraHTML.find(
        'div', {'class': 'article-info-wrapper'})
    listadoContenidoPagina = obtenerHeader(bloqueHeader)
    bloque = estructuraHTML.find(
        'article', {'class': 'note-detail notapage_minuto'})
    imagen = obtenerImagen(bloque)
    listadoContenidoPagina.append(imagen)
    contenido = estructuraHTML.find(
        'div', {'class': 'note-body newDetailTextChange clearfix'})
    cuerpo = obtenerCuerpoNoticia(contenido)
    listadoContenidoPagina.append(cuerpo)
    print('-'*10, 'Terminado', '-'*10)
    return listadoContenidoPagina


# -------------------------------------------------
listaEnlaces = obtenerEnlaceNoticia()
listaContenidoPagina = []
listado20Paginas = []
print('-'*30, len(listaEnlaces), 'Enlaces', '-'*50)
for i in range(0, 20):
    print('-'*100)
    print('-'*40, 'procesando enlace n°:', i+1, '-'*40)
    listaContenidoPagina = obtenerDatosPagina(listaEnlaces[i])
    print('-'*45, 'Datos de páginas', '-'*45)
    print(Style.BRIGHT + Fore.CYAN + 'Título:', listaContenidoPagina[0])
    print(Style.BRIGHT + Fore.CYAN + 'Resumen:', listaContenidoPagina[1])
    print(Style.BRIGHT + Fore.CYAN + 'Imagen:', end=' ')
    print(listaContenidoPagina[2])
    print(Style.BRIGHT + Fore.CYAN + 'Cuerpo:', listaContenidoPagina[3])
    listado20Paginas.append(listaContenidoPagina)

# print(listado20Paginas)

# ---------- análisis de texto ----------------------
texto = '' # toda la información de las 20 pag.
for dato in listado20Paginas:
    pagina = ' '.join(dato)
    texto += pagina + ' '

#eliminar los signos de puntuacion
textoLimpio = operacionTexto.eliminarSignosPuntuacion(texto)
#--tokenizacion y eliminacion de stopword
textoTokenizado = operacionTexto.tokenizar(textoLimpio)
# print(textoTokenizado)
# poner en minuscula 
textoMinuscula = operacionTexto.ponerMinuscula(textoTokenizado)
textoSinStopwords = operacionTexto.eliminarStopWords(textoMinuscula)
# obtener los terminso mas frecuentes
frecuenciasTerminos = operacionTexto.obtenerFrecuencias(textoSinStopwords)
for i in range(100):
    if i == 0:
        print(Style.BRIGHT + Fore.GREEN + '{:<20} {:>10}'.format(frecuenciasTerminos[i][0],frecuenciasTerminos[i][1]))
    else:
        print('{:<20} {:>10}'.format(frecuenciasTerminos[i][0],frecuenciasTerminos[i][1]))
print("\n\n")
#-- stemming----
listadoStemming = operacionTexto.stemmingSnowBall(textoSinStopwords)
print(Style.BRIGHT + Fore.GREEN + '{:<20} {:>10}'.format("Palabra","Stem"))
for i in range(100):
    print("{:<20} {:>10}".format(listadoStemming[0][i],listadoStemming[1][i]))
print("\n\n")
frecuenciasStem = operacionTexto.obtenerFrecuencias(listadoStemming[1])
for i in range(100):
    if i == 0:
        print(Style.BRIGHT + Fore.GREEN +'{:<20} {:>10}'.format(frecuenciasStem[i][0],frecuenciasStem[i][1]))
    else:
        print('{:<20} {:>10}'.format(frecuenciasStem[i][0],frecuenciasStem[i][1]))
