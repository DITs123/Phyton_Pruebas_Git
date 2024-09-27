# Práctica Módulo Collections 1
# Aplica un Counter (contador) sobre la lista de números entregada a continuación, y almacénalo en una variable llamada contador
print("Práctica 1 Módulo Collections 2")
from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)

print("Práctica 2 Módulo Collections 2")
# Práctica Módulo Collections 2
# Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, se cargue con el string "Valor no hallado".
#
# Carga el diccionario, al menos, con el siguiente par de datos:
#
# palabra clave = edad
#
# valor = 44
#
# Utiliza el método defaultdict del módulo Collections.

from collections import defaultdict

mi_diccionario = defaultdict(lambda:"Valor no hallado")

mi_diccionario["palabra clave"] = "edad"
mi_diccionario["edad"] = 44
print(mi_diccionario["valora"])

#print("Práctica 3 Módulo Collections ")
# Práctica Módulo Collections 3
# Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite insertar y eliminar elementos por ambos extremos.
#
# Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir del módulo collections. Los elementos iniciales de la lista se brindan a continuación.
#
# ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
#
# La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.

from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)


#####################################################333
print("\n PARTE DE EXPLICACIONES DE LOS VIDEOS")
import os
print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('Texto de prueba.')
archivo.close()

print(os.listdir())

import shutil
#import send2trash
#shutil.move('curso.txt', "C:\\Users\\ivnim\\Desktop\\Python\\pythonProject")

ruta = "C:\\Users\\ivnim\\Desktop\\Python\\pythonProject\\Día9\\CarpetaDePruebas"
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta }')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        if arch.startswith('2015'):
            print(f'\t{arch}')
    print('\n')


from datetime import datetime


mi_fecha = datetime(2025,5,15,22,10,15,2500)
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

from datetime import date

nacimiento = date(1995,3,5)
defuncion = date(2095,6,19)

vida = defuncion - nacimiento

print(vida)
#
# Práctica Módulo Datetime 2
# Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
from datetime import date

hoy = date.today()

print("\nFecha de hoy",hoy)

from datetime import datetime


minutos = datetime.now().minute
print(minutos)




