# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:34:38 2024

@author: ar_fe
"""

import pandas as pd
#renombrar imagenes, por si tengo algunas con los mismos nombres
import os
path = 'C:/Users/ar_fe/Documents/PhD Computación/AprendizajeAutomatico/Tarea 2/operadores/multiplicacion'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(['multi'+str(index), '.jpg'])))
    
#Generar data labels.csv
path = 'C:/Users/ar_fe/Documents/PhD Computación/AprendizajeAutomatico/Tarea 2/operadores'
folderNames = ['division', 'mas','menos', 'multiplicacion']
    
labels = []
c=0
for folder in folderNames:
  for i in os.listdir(os.path.join(path, folder)):
    labels.append([i,c]) #labels en numerados de 0 a 3.
  c=c+1
labels = pd.DataFrame(labels, columns=['img','label'])
labels.to_csv('labels.csv', index=False) #lo guardamos