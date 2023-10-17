import rasterio
from os import chdir
from pcraster import *
from osgeo import gdal, gdalconst
import matplotlib.pyplot as plt

dir="D:\Rasters\Variables_climaticas_raster\\tavg\\bandas"
chdir(dir)

extension = '.tif'  # Extensión archivos a recorrer

forzante='tavg' #forzante a analizar, dar nombre de 4 letras

syst_ref="EPSG:32718"


#Create function to convert from tif to map
def ConvertToPCRaster (src_fname,dst_fname,ot,VS):
    src_ds = gdal.Open(src_fname)
    dst_ds = gdal.Translate(dst_fname, src_ds, format="PCRaster", outputType=ot, metadataOptions=VS)
    src_ds = None
    dst_ds = None

# Itera sobre todos los archivos en la carpeta tipo .map

numero_archivo=1

for archivo in os.listdir(dir):
    if archivo.endswith(extension):
        if numero_archivo>999:
            str_archivo=str(numero_archivo)
            parte_final=int(str_archivo[-3:])
            primera_parte=int(str_archivo[:-3])
            nombre_archivo=f'{forzante}{primera_parte:04d}.{parte_final:03d}'
        else:
            nombre_archivo = f'{forzante}0000.{numero_archivo:03d}'
        ConvertToPCRaster(archivo, nombre_archivo, gdalconst.GDT_Float32, "VS_SCALAR")
        numero_archivo=numero_archivo+1
