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
    for palabra in texto:
        if palabra not in string.punctuation:
            textoLimpio+=palabra
    return textoLimpio


def eliminarStopWords(listaPalabra):
    '''
    Función que elimina los stopwords en español de una lista de palabras.

    Args:
    listaPalabra: list [] 

    return: list [] 
    '''
    stop_words=set(stopwords.words('spanish'))
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