import os
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np

#DIRECTORIO A TRABAJAR
os.chdir('D:\CIREN\SPHY - ejemplos\Trisuli\output_test')

#DEFINIMOS VARIABLES
tss_files = ['QAllDTS.tss']
ngauges = 2
ngaugesdisp = 2
data = {}  # Un diccionario para almacenar los datos
# csvfilepath = '/Users/felipearrospide/Documents/GitHub/lisflood-usecases/LF_lat_lon_UseCase/streamflow_simulated_best.csv'

for files in tss_files:
    with open(files, 'r') as f: # se utiliza para abrir un archivo llamado files en modo de lectura ('r') en Python y lo almacena en la variable f
        lines = f.readlines()
        xrun = np.array([line.split()[0] for line in lines[(3 + ngauges):]], dtype=float)
        #3 + ngauges dice cuantas lineas debemos saltarnos para comenzar la lectura del archivo
        #con lines[] se genera la sublista que comienza desde ese valor
        #line.split() divide cada línea de la sublista en palabras o elementos utilizando el espacio en blanco como separador.
        #Esto devuelve una lista de palabras en cada línea. (es [0] porque considera el primer elemento, es decir, el paso de tiempo)
        #np.array(..., dtype=float) crea un array NumPy a partir de la lista resultante de palabras. Además, se especifica dtype=float para asegurarse de que los valores se interpreten como números decimales
        data['xrun'] = xrun  # Agrega xrun al diccionario
        for k in np.arange(1, ngaugesdisp + 1): #va a recorrer las columnas (las distintas estaciones)
            yrun = np.array([line.split()[k] for line in lines[(3 + ngauges):]], dtype=float)
            data[f'yrun_{k}'] = yrun  # Agrega yrun al diccionario
            plt.plot(xrun, yrun, label='Gauge ' + str(k))  # marker = 'o', linestyle = 'None')


#GRAFICAMOS
plt.title('Trisuli results')
plt.xlabel('time (days)')
plt.ylabel('discharge at outlet ' + r'($m^3/s$)')
plt.legend()
#plt.yscale('log')
#plt.axis()
plt.show()

# Crea un DataFrame de pandas desde el diccionario de datos
df = pd.DataFrame(data)

# Reemplaza comas por puntos en una columna específica
df['yrun_1'] = df['yrun_1'].str.replace(',', '.', regex=True)
df['yrun_2'] = df['yrun_2'].str.replace(',', '.', regex=True)

# Convierte la columna en números de punto flotante
df['yrun_1'] = df['yrun_1'].astype(float)
df['yrun_2'] = df['yrun_2'].astype(float)

# Guarda el DataFrame en un archivo CSV
df.to_csv('output.csv', index=False)