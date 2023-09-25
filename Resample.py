import os
from os import chdir

#Definir directorio de trabajo
dir="D:\PuertoCisnes_prueba\\250m_pixel"
chdir(dir)

#El presente código resamplea los rasters deseados.
#Trabaja con PCRaster y es necesario dar el tipo de dato que se está resampleando.

new_pixel_size= 250 #nuevo tamaño de pixel
file_to_resample= "dem.map"
resample_file= "dem250.map"
method_of_resample="bilinear"
syst_coord='EPSG:32718'

comando=f'gdalwarp -tr {new_pixel_size} {new_pixel_size} -r {method_of_resample} -of PCRaster -co "PCRASTER_VALUESCALE=VS_SCALAR" {file_to_resample} {resample_file}'
os.system('C:\\Users\maary\\anaconda3\Scripts\conda.exe run -n PCRASTER_nueva_version '+comando)

comando2=f'gdal_translate -a_srs {syst_coord} {resample_file} dem_250_crs.map'
os.system('C:\\Users\maary\\anaconda3\Scripts\conda.exe run -n PCRASTER_nueva_version '+comando2)