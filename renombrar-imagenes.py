import os

# como entrada del programa se necesita:
# ruta de carpeta con imágenes
carpeta = "BIMBO"

# encontrar las imágenes de la carpeta
# y guardarlas en una lista
n = 1
for archivo in os.listdir(carpeta):
    if archivo.endswith((".jpg")):
        # renombrar las imágenes con el nombre de la carpeta y un número consecutivo
        os.path.join(carpeta, archivo)
        os.rename(carpeta + "/" + archivo, carpeta + str(n) + ".jpg")
        n = n + 1