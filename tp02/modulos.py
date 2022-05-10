import operator
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

def eliminarSignosPuntuacion(texto):
    '''
    función que elimina los signos de puntuación de un texto.

    Args:
    texto:[str]

    return: [str]
    '''
    textoLimpio=''
    signosAgregados = '¿¡'
    signosPuntuacion = string.punctuation + signosAgregados
    for palabra in texto:
        if palabra not in signosPuntuacion:
            textoLimpio+=palabra
    return textoLimpio


def eliminarStopWords(listaPalabra):
    '''
    Función que elimina los stopwords en español de una lista de palabras.

    Args:
    listaPalabra: list [] 

    return: list [] 
    '''
    stop_words=stopwords.words('spanish')
    stopWordsAgregados=['podría','ser','cómo','según','pueden']
    stop_words.extend(stopWordsAgregados)

    listaSinStopWords=[]
    for palabra  in listaPalabra:
        if palabra not in stop_words:
            listaSinStopWords.append(palabra)
    return listaSinStopWords

def tokenizar(texto):
    '''
    Función que Tokeniza en español un texto. 

    Args:
    texto: str

    return: List []
    '''
    tokens = nltk.word_tokenize(texto,'spanish')
    return tokens

def obtenerFrecuencias(listaPalabras):
    '''
    Función que obtiene las frecuencias de las palabras de la lista.

    Args:
    listaPalabras: [list]

    Return: [list]
    '''
    listadoFrec = [['Palabra\t','Frecuencia']]
    frecuencias = nltk.FreqDist(listaPalabras)
    # ordenar las frecuencias
    frec_ordenada_valor = sorted(frecuencias.items(), key=operator.itemgetter(1), reverse=True)
    for palabra in enumerate(frec_ordenada_valor):
        frec = [palabra[1][0], frecuencias[palabra[1][0]]]
        listadoFrec.append(frec)
    return listadoFrec

def stemmingSnowBall(datos):
    '''
    Función que obtiene los stem de las palabras de la lista

    Args:
        datos: [str]
    
    Return: 
        listado [list] 
    '''
    listado = []
    palabras =[]
    stems = []
    espaniolStemmer = SnowballStemmer('spanish')
    for palabra in datos:
        palabras.append(palabra)        
        stem = espaniolStemmer.stem(palabra)
        stems.append(stem)
    listado.append(palabras)
    listado.append(stems)        
    return listado

def ponerMinuscula(listaPalabras):
    '''
    Método que pone en minusculas las palabras de una lista. 
    arg:
        listaPalabras: [list] 
    Return:
        listaMinuscula = [list]
    '''
    listaMinuscula = []
    for palabra in listaPalabras:
        listaMinuscula.append(palabra.lower())
    return listaMinuscula

def ponerMayuscula(listaPalabras):
    '''
    Método que pone en mayúscula las palabras de una lista. 
    arg:
        listaPalabras: [list] 
    Return:
        listaMayuscula = [list]
    '''
    listaMayuscula = []
    for palabra in listaPalabras:
        listaMayuscula.append(palabra.lower())
    return listaMayuscula