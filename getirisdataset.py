# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:31:47 2022

@author: KristineP
"""

from sklearn.datasets import load_iris # used to get data
data = load_iris()
print(data)

#how to create a dataset and get average for each variable 

import pandas as pd

df = pd.DataFrame(data.data)
df['species'] = data.target
print(df.groupby('species').mean())