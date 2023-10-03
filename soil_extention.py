from osgeo import gdal,gdalconst
from os import chdir
import os

def ConvertToPCRaster (src_fname,dst_fname,ot,VS):
    src_ds = gdal.Open(src_fname)
    dst_ds = gdal.Translate(dst_fname, src_ds, format="PCRaster", outputType=ot, metadataOptions=VS)
    src_ds = None
    dst_ds = None

#Definir directorio de trabajo
dir="D:\Prueba_SPHY_rio_cisnes_250m\Suelo\Ksat"
chdir(dir)

extension = '.tif'  # Extensión archivos a recorrer
long1=-76.0
long2=-70.0
lat1=-43.0
lat2=-46.0
x1=625000.0
y1=4988840.0
x2=811000.0
y2=5088840.0
tam_pixel=250
syst_orig="EPSG:4326"
syst_final="EPSG:32718"

# Itera sobre todos los archivos en la carpeta tipo .map
for archivo in os.listdir(dir):
    if archivo.endswith(extension):
        nuevo_nombre = f'{archivo[:-8]}_Aysen.tif' #con el -4 le eliminamos los últimos 4 caracteres : .map
        comando=f'gdal_translate -projwin {long1} {lat1} {long2} {lat2} -of GTiff  {archivo} {nuevo_nombre}' #TOMAMOS UN GRAN ESPACIO EN COORDENADAS DEL ARCHIVO, EN ESTE CASO EPSG:4326
        os.system('C:\\Users\maary\\anaconda3\Scripts\conda.exe run -n PCRASTER_nueva_version '+comando) #PCRASTER_nueva_version corresponde al entorno de anaconda a utilizar
        nombre_2=f'{nuevo_nombre[:-4]}32718.tif'
        comando_2=f'gdalwarp -s_srs {syst_orig} -t_srs {syst_final} {nuevo_nombre} {nombre_2}'
        os.system('C:\\Users\maary\\anaconda3\Scripts\conda.exe run -n PCRASTER_nueva_version '+comando_2) #PCRASTER_nueva_version corresponde al entorno de anaconda a utilizar
        nombre_3 = f'{nombre_2[:-4]}_ext.tif'
        comando_3 = f'gdalwarp -te {x1} {y1} {x2} {y2} -tr {tam_pixel} {tam_pixel} -of GTiff {nombre_2} {nombre_3}'
        os.system('C:\\Users\maary\\anaconda3\Scripts\conda.exe run -n PCRASTER_nueva_version ' + comando_3)  # PCRASTER_nueva_version corresponde al entorno de anaconda a utilizar
        nombre_4= f'{nombre_2[:-4]}_ext.map'

        ConvertToPCRaster(nombre_3, nombre_4, gdalconst.GDT_Float32, "VS_SCALAR")
#esto me entrega todos los archivos.map con la nueva extensión y crs