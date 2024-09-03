import os

def renombrar_imagenes(carpeta):
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