import requests
from bs4 import BeautifulSoup

url = 'https://www.eltribuno.com/jujuy/seccion/tecnologia'
urlPrincipal = 'https://www.eltribuno.com'
# website = requests.get(url)
# print(website)

# soup = BeautifulSoup(website.content, 'html.parser')
# print(soup.prettify())

# def obtenerTitulo(bloque):
#     listaTitulos=[]
#     for elemento in bloque:
#         titulo = elemento.find('h1').getText()
#         listaTitulos.append(titulo)
#     return listaTitulos

# bloqueHeader=soup('div',{'class':'nota_ item-pack minuto_foto'})
# # print(bloqueHeader)
# listado=obtenerTitulo(bloqueHeader)
# for titulo in listado:
#     print(titulo)
def obtenerEnlaceNoticia(enlacePrincipal=urlPrincipal, enlaceBusqueda=url):
    listadoEnlaces = []
    website = requests.get(enlaceBusqueda)
    print(website.status_code)
    if  website.status_code == 200:
        pagina = BeautifulSoup(website.content, 'html.parser')
        bloqueNoticias = pagina('div',{'class':'nota_ item-pack minuto_foto'})
        for elemento in bloqueNoticias:
            enlace = elemento.find('h1').find('a', href=True)['href']
            if enlace[0] == '/':
                enlace = enlacePrincipal+enlace
            listadoEnlaces.append(enlace)
    return listadoEnlaces

# print(obtenerEnlaceNoticia())

def obtenerHeader(bloque):
    listaHeader = []
    titulo = bloque.find('h1',{'class':'title newDetailTextChange'}).getText()
    resumen = bloque.find('p', {'class':'preview newDetailTextChange'}).getText()
    listaHeader.append(titulo)
    listaHeader.append(resumen)
    return listaHeader

def obtenerImagen(bloque):
    listaImg = []
    imagen = bloque.find('img').get('data-src')
    return imagen

def obtenerCuerpoNoticia(bloque):
    texto = bloque.find_all('p')
    cuerpo=''
    for p in texto:
        cuerpo+=p.text+'\n'
    return cuerpo

def obtenerPagina(enlace):
    website = requests.get(enlace)
    print(website.status_code)
    if website.status_code == 200:
        pagina = BeautifulSoup(website.content, 'html.parser')
        
    return pagina


    


# -------------------------------------------------

listaEnlaces = obtenerEnlaceNoticia()
listaContenidoPagina= []
listado=[]
print(len(listaEnlaces),'enlaces')
cont = 0
for enlace in listaEnlaces:
    cont+=1
    if cont<=20:
        laPagina = obtenerPagina(enlace)
        bloqueHeader=laPagina.find('div',{'class':'article-info-wrapper'})        
        listaContenidoPagina = obtenerHeader(bloqueHeader)
        # print(listaContenidoPagina)
        bloque = laPagina.find('article',{'class':'note-detail notapage_minuto'})
        # print(obtenerImagen(bloque))
        imagen=obtenerImagen(bloque)
        listaContenidoPagina.append(imagen)
        contenido = laPagina.find('div', {'class':'note-body newDetailTextChange clearfix'})
        # print(obtenerCuerpoNoticia(contenido))
        cuerpo = obtenerCuerpoNoticia(contenido)
        listaContenidoPagina.append(cuerpo)
        listado.append(listaContenidoPagina)
        
    else:
        break
print(listado)