# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:15:53 2020

@author: SolovjevAV
"""

import pandas as pd
import numpy as np

file_name = "D:\Расчеты\Измерение ротора\Измерение ротора.xlsx"
df_fact = pd.read_excel(file_name, sheet_name=0)
df_nominal = pd.read_excel(file_name, sheet_name=1)
r_fact = df_fact['n']

draft = df_fact['Draft'][0]
d_opravki = df_fact['Diametr'][0]
r_fact = r_fact + d_opravki

#fi_fact = r_fact.index * (2*np.pi/(len(r_fact)-1))

x_fact = r_fact * np.cos((r_fact.index) * (2*np.pi/(len(r_fact)-1)))
y_fact = r_fact * np.sin((r_fact.index) * (2*np.pi/(len(r_fact)-1)))

fact = pd.DataFrame(data=(r_fact, x_fact, y_fact))