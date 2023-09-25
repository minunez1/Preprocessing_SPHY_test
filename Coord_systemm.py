import os
from os import chdir
import os

#Definir directorio de trabajo
dir="D:\PuertoCisnes_prueba\\250m_pixel"
chdir(dir)

extension = '.map'  # Extensión archivos a recorrer

syst_ref="EPSG:32718"

# Itera sobre todos los archivos en la carpeta tipo .map
for archivo in os.listdir(dir):
    if archivo.endswith(extension):
        nuevo_nombre = f'input_{archivo[:-4]}_noclean.map' #con el -4 le eliminamos los últimos 4 caracteres : .map
        comando=f'gdal_translate -a_srs {syst_ref} {archivo} {nuevo_nombre}'
        os.system('C:\\Users\maary\\anaconda3\Scripts\conda.exe run -n PCRASTER_nueva_version '+comando) #PCRASTER_nueva_version corresponde al entorno de anaconda a utilizar


#esto me entrega todos los archivos.map con la nueva referencia