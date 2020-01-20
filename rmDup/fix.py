# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 07:33:33 2019

@author: wangjie
"""
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def combineAndRmDup(inf,outf):
    df = pd.read_csv(inf,header=0)

    print(df)
#    df['Pubmed_id'] = df['Pubmed_id'].astype(str)
#    d1 = df.groupby(['gene_a_id','gene_b_id'])
#    d2 = d1.apply(lambda x:','.join(x['Pubmed_id']))
    mask = df['gene_a_id']< df['gene_b_id']
    df['first'] = df['gene_a_id'].where(mask, df['gene_b_id']).map(lambda x:str(x))
    df['second'] = df['gene_b_id'].where(mask, df['gene_a_id']).map(lambda x:str(x))
    df['key'] = df['first'].str.cat(df['second'])
    df = df.drop_duplicates(subset=['key'],keep="last")
    print(df)
#    datalist = df.drop_dupilicates()
    df.to_csv(outf)
#for i in ['worm','yeast','human','fly','mouse']:
for i in ['human']:
    inf = 'd:/rmdup/new/'+i+'_new.csv'
    outf = 'd:/rmdup/new/'+i+'_newreal.csv'
    combineAndRmDup(inf,outf)