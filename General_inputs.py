from os import chdir
from pcraster import *
import os

dir="D:\Prueba_SPHY_rio_cisnes_250m\InfoGeneral"
chdir(dir)

#Leemos DEM y definimos nombres archivos
DEM=readmap("dem_crs.map")
nombre_a_dem_corr='dem_corr_250.map' #definimos nombre archivo con dem corregido
nombre_slope='slope_250.map' #definimos nombre archivo con pendientes
flowdir='flowdir250.map' #definimos nombre archivo con sentido de flujo
nombre_flujo_acumulado='accuflux250m.map' #definimos nombre archivo con acumulación de flujo

#CORRECCIÓN DEM: lddcreatedem llena los pozos y deja un dem hidrologicamente corregido
DEM_corregido=lddcreatedem(DEM, 1e31, 1e31, 1e31, 1e31)
report(DEM_corregido,f'{nombre_a_dem_corr}')

#PENDIENTE DEM CORREGIDO
slope_dem=slope(DEM_corregido)
report(slope_dem,f'{nombre_slope}')

#CALCULO DIRECCIÓN DE FLUJO: ldd llena los posibles "pozos" y genera la dirección de flujo
Direccion_flujo = lddcreate(DEM,1e31,1e31,1e31,1e31)
report(Direccion_flujo,f'{flowdir}')
aguila(Direccion_flujo)

#PRESENTACIÓN DE ACUMULACIÓN DE FLUJO
Acumulacion_flujo = accuflux(Direccion_flujo,1)
report(Acumulacion_flujo,f'{nombre_flujo_acumulado}')

