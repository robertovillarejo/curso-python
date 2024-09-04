import os

def renombrar_imagenes(carpeta):
    prefijo = os.path.basename(carpeta)
    n = 1
    for archivo in os.listdir(carpeta):
        if archivo.endswith((".jpg",".JPG",".jpeg",".JPEG",".png",".PNG")):
            # determinar la extensión del archivo
            extension = os.path.splitext(archivo)[-1]
            # renombrar las imágenes con el nombre de la carpeta y un número consecutivo
            ruta_archivo_inicial = os.path.join(carpeta, archivo)
            ruta_archivo_final = os.path.join(carpeta, prefijo) + str(n) + extension
            os.rename(ruta_archivo_inicial, ruta_archivo_final)
            n = n + 1