import os

def renombrar_imagenes(carpeta,jpg:bool,png:bool,bmp:bool,gif:bool):
    prefijo = os.path.basename(carpeta)
    n = 1
    tipos=[]
    if bmp==True:
        tipos.append(".bmp")
        tipos.append(".BMP")
    if jpg==True:
        tipos.append(".jpg")
        tipos.append(".JPG")
        tipos.append(".jpeg")
        tipos.append(".JPEG")
    if png==True:
        tipos.append(".png")
        tipos.append(".PNG")
    if gif==True:
        tipos.append(".gif")
        tipos.append(".GIF")

    for archivo in os.listdir(carpeta):
        if archivo.endswith(tuple(tipos)):
            # determinar la extensión del archivo
            extension = os.path.splitext(archivo)[-1]
            # renombrar las imágenes con el nombre de la carpeta y un número consecutivo
            ruta_archivo_inicial = os.path.join(carpeta, archivo)
            ruta_archivo_final = os.path.join(carpeta, prefijo) + str(n) + extension
            os.rename(ruta_archivo_inicial, ruta_archivo_final)
            n = n + 1