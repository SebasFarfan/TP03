# import moduloTP2
from package.moduloTP2 import hola
from nltk.corpus import stopwords
from colorama import Fore, Style, init
init(autoreset=True)
nombre = 'sebastián'
# print(moduloTP2.hola(nombre))
print(hola(nombre))

print('nombre',end=' ')
print(hola(nombre))
lista = [['ana','carolina','laura','maria','karen'],['mabel','valeria']]
# texto = ' '.join(lista)
# texto1=''
text2= ''
for elemento in lista:
    texto1=' '.join(elemento)
    text2+=texto1+' '

print(text2)
# print(set(stopwords.words('spanish')))

print(Style.BRIGHT + Fore.CYAN + 'Analia')
print('Django')