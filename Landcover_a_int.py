from PIL import Image
from os import chdir
import numpy as np


dir="D:\Prueba_SPHY_rio_cisnes_250m\InfoGeneral"
chdir(dir)

# Cargar el archivo TIFF
archivo_tif = 'Landcover.tif'
imagen_tif  = Image.open(archivo_tif)

# Convierte la imagen a un arreglo NumPy de punto flotante
imagen_np = np.array(imagen_tif, dtype=np.float32)

# Divide todos los valores por 100
imagen_np /= 100

# Redondea los valores decimales a enteros
imagen_np = np.round(imagen_np)

# Multiplica nuevamente por 100
imagen_np *= 100

# Convierte el arreglo NumPy de nuevo a una imagen PIL
imagen_tif_modificada = Image.fromarray(imagen_np.astype(np.uint16))

# Guarda la imagen resultante en un nuevo archivo TIFF
imagen_tif_modificada.save("archivo_modificado2.tif")

# Cierra la imagen original
imagen_tif.close()