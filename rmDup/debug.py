# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:26:21 2019

@author: wangjie
"""



from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df = pd.read_csv('d:/test.csv',header=0)
mask = df['gene_a_id']< df['gene_b_id']