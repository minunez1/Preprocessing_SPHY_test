from os import chdir
from pcraster import *
import os

dir="D:\Puerto Cisnes_prueba\\50m_pixel"
chdir(dir)

#Leemos DEM y definimos nombres archivos
DEM=readmap("dem50.map")
nombre_a_dem_corr='dem_corr_50.map' #definimos nombre archivo con dem corregido
nombre_slope='slope_50.map' #definimos nombre archivo con pendientes
flowdir='flowdir50.map' #definimos nombre archivo con sentido de flujo
nombre_flujo_acumulado='accuflux.map' #definimos nombre archivo con acumulación de flujo
nombre_clone='clone50.map' #definimos nombre archivo clone.map

#CORRECCIÓN DEM: lddcreatedem llena los pozos y deja un dem hidrologicamente corregido
DEM_corregido=lddcreatedem(DEM, 1e31, 1e31, 1e31, 1e31)
report(DEM_corregido,f'{nombre_a_dem_corr}')

#PENDIENTE DEM CORREGIDO
slope_dem=slope(DEM_corregido)
report(slope_dem,f'{nombre_slope}')

#CALCULO DIRECCIÓN DE FLUJO: ldd llena los posibles "pozos" y genera la dirección de flujo
Direccion_flujo = lddcreate(DEM,1e31,1e31,1e31,1e31)
report(Direccion_flujo,f'{flowdir}')
#aguila(FlowDirection)

#PRESENTACIÓN DE ACUMULACIÓN DE FLUJO
Acumulacion_flujo = accuflux(Direccion_flujo,1)
report(Acumulacion_flujo,f'{nombre_flujo_acumulado}')

