import sys
import os

# argv es una forma de recibir argumentos desde la consola
if (len(sys.argv) == 1):
    print("No se ha ingresado una carpeta, se usará valor por defecto")
    carpeta = "BIMBO"
else:
    carpeta = sys.argv[1]

for archivo in os.listdir(carpeta):
    if (archivo.endswith(".jpg")):
        print(archivo)