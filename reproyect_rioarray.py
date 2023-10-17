import xarray as xr
import rioxarray
from os import chdir
import netCDF4 as nc

#Definir directorio de trabajo
dir="D:\Rasters\Variables_climaticas_raster\\tmax"
chdir(dir)

# Especifica la proyección de destino (EPSG:32718, por ejemplo)
crs_origen= "epsg:4326"
crs_destino = "epsg:32718"

# Otras opciones de reproyección (por ejemplo, resolución)

ds = xr.open_dataset("tmax_proj_4326_2005a2010.nc")
variable="tmax"
# Define el CRS para la variable 'tmax'
ds.rio.write_crs(crs_origen, inplace=True)

# Reproyecta el conjunto de datos al nuevo sistema de coordenadas
ds_reproyectado = ds.rio.reproject(dst_crs=crs_destino)

# Resamplea el conjunto de datos a la nueva resolución (250x250 metros)
ds_ext=ds_reproyectado.rio.clip_box(minx=645000.0,miny=4988840.0,maxx=811000.0,maxy=5088840.0,crs=crs_destino)
#ds_resampleado = ds_ext.rio.reproject(dst_crs=crs_destino)
print(ds_ext.rio.crs)

# # Guarda el conjunto de datos reproyectado en un nuevo archivo NetCDF
ds_ext.to_netcdf("archivo_reproyectado-corte2.nc",format="NETCDF4",engine="netcdf4",encoding={f'{variable}': {"zlib": True}})
#
# print("Coordenadas de límites espaciales:")
# print(ds_ext.rio.bounds())
#
# print("Sistema de Coordenadas de Referencia (CRS):")


# Cierra los conjuntos de datos
ds.close()
ds_reproyectado.close()