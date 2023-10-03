import os
from osgeo import gdal
import numpy as np
from os import chdir

dir="D:\Prueba_SPHY_rio_cisnes_250m"
chdir(dir)

mask_tif='DEM_250_grande.tif'
mask_tif_latlon='DEM_latlon.tif'
crs_origen='EPSG:32718'
crs_final='EPSG:4326'

comando_1=f'gdalwarp -s_srs {crs_origen} -t_srs {crs_final} -of GTiff {mask_tif} {mask_tif_latlon}'
os.system('C:\\Users\maary\\anaconda3\Scripts\conda.exe run -n PCRASTER_nueva_version '+comando_1)


ds  = gdal.Open(mask_tif_latlon)
band = ds.GetRasterBand(1)
transform = ds.GetGeoTransform()
data = band.ReadAsArray()

# Obtiene el tamaño de píxel en grados (en EPSG 4326, un grado de latitud es aproximadamente 111 km)
pixel_height = abs(transform[5])  # Valor absoluto en caso de orientación negativa

# Crea una matriz vacía para almacenar las latitudes
latitudes = np.zeros(data.shape, dtype=float)

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        latitudes[i][j] = transform[3] - i * pixel_height


# Crea un nuevo archivo GeoTIFF para almacenar las latitudes (en EPSG 4326)
archivo_salida = 'latitudes_raster.tif'
driver = gdal.GetDriverByName('GTiff')
nuevo_ds = driver.Create(archivo_salida, data.shape[1], data.shape[0], 1, gdal.GDT_Float32)
nuevo_ds.GetRasterBand(1).WriteArray(latitudes)
nuevo_ds.SetGeoTransform(transform)
nuevo_ds.SetProjection(ds.GetProjection())

# Cierra los archivos
nuevo_ds = None
ds = None

