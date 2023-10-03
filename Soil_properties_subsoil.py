import pcraster as pcr
import numpy as np
from os import chdir
import os

#Definir directorio de trabajo
dir="D:\Prueba_SPHY_rio_cisnes_250m\Suelo\Ksat\ext_crs_correcto"
chdir(dir)

# Cargar los tres mapas de suelo
suelo1 = pcr.readmap("Ksat_30-60cm_M__Aysen32718_ext.map")
suelo2 = pcr.readmap("Ksat_60-100cm_M__Aysen32718_ext.map")
suelo3 = pcr.readmap("Ksat_100-200cm_M__Aysen32718_ext.map")

# Sumar los valores de los mapas
altura_suelo1=30
altura_suelo2=40
altura_suelo3=100
total_ponderacion=altura_suelo1+altura_suelo2+altura_suelo3
suma_suelo = (suelo1*altura_suelo1 + suelo2*altura_suelo2 + suelo3*altura_suelo3)/(total_ponderacion)
pcr.report(suma_suelo, "Ksat_subsoil.map")
