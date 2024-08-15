import os
import sys

# como entrada del programa se necesita:
# ruta de carpeta con imágenes
# argv es una forma de recibir argumentos desde la consola

if (len(sys.argv) == 1):
    print("No se ha ingresado el nombre válido de una carpeta")
else:
    carpeta = sys.argv[1]   

n = 1
for archivo in os.listdir(carpeta):
    if archivo.endswith((".jpg",".JPG",".jpeg",".JPEG",".png",".PNG")):
        # determinar la extensión del archivo
        extension = os.path.splitext(archivo)
        # renombrar las imágenes con el nombre de la carpeta y un número consecutivo
        dir_ini = os.path.join(carpeta, archivo)
        dir_fin = (os.path.join(carpeta,carpeta) + str(n) + extension[-1])
        os.rename(dir_ini, dir_fin)
        n = n + 1


# encontrar las imágenes de la carpeta
# y guardarlas en una lista
"""
n = 1
for archivo in os.listdir(carpeta):
    if archivo.endswith((".jpg",".JPG",".jpeg",".JPEG",".png",".PNG")):
        # determinar la extensión del archivo
        extension = os.path.splitext(archivo)
        # renombrar las imágenes con el nombre de la carpeta y un número consecutivo
        os.path.join(carpeta, archivo)
        os.rename(carpeta + "/" + archivo, carpeta + "/" + carpeta + str(n) + extension[-1])
        n = n + 1
"""



