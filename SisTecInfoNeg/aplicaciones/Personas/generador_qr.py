import qrcode
from PIL import Image

cadena = input("Introduzca el texto para el codigo qr: ")
Imagen = qrcode.make(cadena)

nombre_imagen = input("Introduzca el nombre de la imagen: ")+'.png'
archivo_imagen = open(nombre_imagen,'wb')
Imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = './'+nombre_imagen
Image.open(ruta_imagen).show()