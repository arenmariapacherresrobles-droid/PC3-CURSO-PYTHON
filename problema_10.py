import zipfile
import os

# ----------------- Comprimir imagen -----------------
def comprimir_imagen(ruta_imagen, nombre_zip):
    if not os.path.isfile(ruta_imagen):
        print(f"No se encontró el archivo: {ruta_imagen}")
        return
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(ruta_imagen, arcname=os.path.basename(ruta_imagen))
        print(f"Imagen '{ruta_imagen}' comprimida correctamente en '{nombre_zip}'")
    except Exception as e:
        print(f"Ocurrió un error al comprimir: {e}")

# ----------------- Descomprimir imagen -----------------
def descomprimir_imagen(nombre_zip, carpeta_destino):
    if not os.path.isfile(nombre_zip):
        print(f"No se encontró el archivo: {nombre_zip}")
        return
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(carpeta_destino)
        print(f"Archivo '{nombre_zip}' descomprimido en la carpeta '{carpeta_destino}'")
    except Exception as e:
        print(f"Ocurrió un error al descomprimir: {e}")

# ----------------- Programa principal -----------------
if __name__ == "__main__":
    # Ruta de la imagen ya definida
    ruta_imagen = r"C:\Users\Aren\Descargas\foto_perrito.jpg"
    nombre_zip = "archivo_imagen.zip"
    carpeta_destino = "descomprimido"

    # Comprimir la imagen
    comprimir_imagen(ruta_imagen, nombre_zip)

    # Crear carpeta destino si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Descomprimir la imagen
    descomprimir_imagen(nombre_zip, carpeta_destino)
