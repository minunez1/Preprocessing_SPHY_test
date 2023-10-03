import pcraster as pcr
import numpy as np
from os import chdir
import os

#Definir directorio de trabajo
dir="D:\Prueba_SPHY_rio_cisnes_250m\Suelo\Ksat\ext_crs_correcto"
chdir(dir)

# Cargar los tres mapas de suelo
suelo1 = pcr.readmap("Ksat_0-5cm_M__Aysen32718_ext.map")
suelo2 = pcr.readmap("Ksat_5-15cm_M__Aysen32718_ext.map")
suelo3 = pcr.readmap("Ksat_15-30cm_M__Aysen32718_ext.map")

# Sumar los valores de los mapas
altura_suelo1=5
altura_suelo2=10
altura_suelo3=15

suma_suelo = (suelo1*altura_suelo1 + suelo2*altura_suelo2 + suelo3*altura_suelo3)/(altura_suelo1+altura_suelo2+altura_suelo3)
pcr.report(suma_suelo, "Ksat_rootzone.map")
