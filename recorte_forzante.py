import os
from os import chdir
from netCDF4 import Dataset

#Definir directorio de trabajo
dir="D:\Rasters\Variables_climaticas_raster\\tmax"
chdir(dir)

#PRIMERO AJUSTAMOS A COORDENADAS CORRECTAS EL ARCHIVO
coordenadas_destino="EPSG:32718"
archivo_a_cambiar="archivo_reproyectado-corte2.nc"
nombre_archivo_crs_correcto="tmax_32718.nc"
comando=f'gdalwarp -t_srs {coordenadas_destino} -overwrite -dstnodata -9999 -of netCDF {archivo_a_cambiar} {nombre_archivo_crs_correcto}'
os.system(comando)

# Ruta al archivo NetCDF con los subdatasets
input_nc_file = nombre_archivo_crs_correcto

# Obtén la lista de subdatasets (bandas) utilizando netCDF4
nc_file = Dataset(input_nc_file, "r")
subdatasets = nc_file.variables.keys()
nc_file.close()

# Definir la ventana y resolución deseadas
resolution = "250 250"
projwin = "645000 4988840 811000 5088840"

# Procesar cada subdataset
for subdataset in subdatasets:
    output_tif_file = f"{subdataset}_1.tif"
    print(subdataset)
    gdal_translate_command = f"gdal_translate -tr {resolution} NETCDF:{input_nc_file}:{subdataset} {output_tif_file}"
    os.system(gdal_translate_command)
    output_tif_file_2=f"bandas\{subdataset}.tif"
    gdalwarp_command = f"gdalwarp -te {projwin} {output_tif_file} {output_tif_file_2}"
    os.system(gdalwarp_command)

print("Proceso completado.")