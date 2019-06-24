#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:27:14 2019

@author: malaikaandrade
"""

import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_excel('tabla5.xlsx', 'Hoja 1' )
print(df)

#conocer datos de una sola columna
aux = df['Numero']
aux2 = df['Edad']


plt.plot(aux, aux2, 'ro')
plt.show()