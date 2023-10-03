from os import chdir
import netCDF4 as nc
import numpy as np
import netCDF4 as nc
import rasterio
from rasterio.transform import from_origin
from rasterio import Affine
import numpy as np

#Definir directorio de trabajo
dir="D:\Rasters\Variables_climaticas_raster\\tmax\prueba_dias"
chdir(dir)

# Ruta al archivo NetCDF
ruta_archivo_nc = "prueba_120_dias.nc"

# Abre el archivo NetCDF en modo de solo lectura
archivo_nc  = nc.Dataset(ruta_archivo_nc, 'r')

# Genera los nombres de las bandas que te interesan
nombres_bandas_interes = ['Band{}'.format(i) for i in range(1, 121)]

# Define la extensión y el tamaño de píxel
extension_x_min = 645000
extension_x_max = 811000
extension_y_min = 4988840
extension_y_max = 5088840

extension = (extension_x_min, extension_x_max, extension_y_min, extension_y_max)

# Calcular la resolución espacial en X
tamanio_pixel_x = 250#4347.83
tamanio_pixel_y = 250#4368.42

# Itera a través de las bandas de interés
for nombre_banda in nombres_bandas_interes:
    # Accede a cada banda por su nombre
    if nombre_banda in archivo_nc.variables:
        banda = archivo_nc.variables[nombre_banda]

        # Accede a los valores de la banda (datos)
        valores = banda[:]

        # Define la transformación Affine con la extensión y el tamaño de píxel
        transformacion_geoespacial = from_origin(extension[0], extension[3], tamanio_pixel_x, tamanio_pixel_y)

        # Define la ruta de salida para el archivo GeoTIFF
        ruta_salida = nombre_banda + '.tif'

        # Crea el archivo GeoTIFF y escribe los valores de la banda
        with rasterio.open(ruta_salida, 'w', driver='GTiff', height=valores.shape[0], width=valores.shape[1], count=1,
                           dtype=np.float32, crs='EPSG:32718', transform=transformacion_geoespacial) as dst:
            dst.write(valores, 1)

# Cierra el archivo NetCDF cuando hayas terminado
archivo_nc.close()