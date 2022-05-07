# import csv
# lista1=['primero','segundo','tercero','cuarto']
# lista2=[['ana','analia','romina'],['belen','betsabe','carla'],['daniela','elisa','elda'],['judith','maria','mirian']]
# enc1=['Nivel 1']
# enc2=['Nivel 2']
# with open('./cursos.csv', 'w') as csv_file:
#     csv_write = csv.writer(csv_file, dialect='excel')
#     csv_write.writerows(zip(enc1,enc2))
#     csv_write.writerows(zip(lista1,lista2))
# print('terminado')
# nombre='sebastian/'
# apellido='/farfan'
lista99=['ana','carolina','julieta','eliana']
nombre='ana'
# print(nombre[0:len(nombre)-1]+apellido)
def filtrarEnlaces(listaEnlaces, enlace):
    '''
        Método que ingresa un enlace a una lista si esta no esta presente 
        en la lista
        parámetros: 
            listaEnlaces: list listado de enlaces
            enlace: str 
        return True si enlace  se almacena en la lista, de otro modo False
    '''
    salida = False
    if enlace not in listaEnlaces:
        listaEnlaces.append(enlace)
        salida = True
    return salida

if filtrarEnlaces(lista99,nombre):
    print(lista99)
else:
    print('no se pudo', lista99)