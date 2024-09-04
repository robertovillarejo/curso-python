import sys
import renombrar_imagenes

# como entrada del programa se necesita:
# ruta de carpeta con imágenes
# argv es una forma de recibir argumentos desde la consola

carpeta = None
if (len(sys.argv) == 1):
    print("No se ha ingresado el nombre válido de una carpeta")
else:
    carpeta = sys.argv[1]   

renombrar_imagenes.renombrar_imagenes(carpeta)