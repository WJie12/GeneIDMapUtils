# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 02:36:42 2019

@author: wangjie
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def combineAndRmDup(old, inf,outf):
    olddf = pd.read_csv(old,header=0)
    infdf = pd.read_csv(inf,header=0)
    df = olddf.append(infdf,sort=False)
    df=df.reset_index()
    print(olddf)
    print(infdf)
    print(df)
#    df['Pubmed_id'] = df['Pubmed_id'].astype(str)
#    d1 = df.groupby(['gene_a_id','gene_b_id'])
#    d2 = d1.apply(lambda x:','.join(x['Pubmed_id']))
    mask = df['gene_a_id']< df['gene_b_id']
    df['first'] = df['gene_a_id'].where(mask, df['gene_b_id']).map(lambda x:str(x))
    df['second'] = df['gene_b_id'].where(mask, df['gene_a_id']).map(lambda x:str(x))
    df['key'] = df['first'].str.cat(df['second'])
    df = df.drop_duplicates(subset=['key'],keep='last')
    print(df)
#    datalist = df.drop_dupilicates()
    df.to_csv(outf)

def analysisNew(old, new, uninew):
    olddf = pd.read_csv(old,header=0)
    newdf = pd.read_csv(new,header=0)
    df = olddf.append(newdf,sort=False)
    df=df.reset_index(drop=True)
#    print(olddf)
#    print(newdf)
#    print(df)
#    df['gene_a_id'],df['gene_b_id'],df['gene_a_name'],df['gene_b_name'] = np.where(df['gene_a_id'] > df['gene_b_id'],
#      [df['gene_b_id'],df['gene_a_id'],df['gene_b_name'],df['gene_a_name']],
#      [df['gene_a_id'],df['gene_b_id'],df['gene_a_name'],df['gene_b_name']])
    a=(df['gene_a_id']).map(lambda x:int(x))
    b=(df['gene_b_id']).map(lambda x:int(x))
    mask = a < b
    df['first'] = df['gene_a_id'].where(mask, df['gene_b_id']).map(lambda x:str(x))
    df['second'] = df['gene_b_id'].where(mask, df['gene_a_id']).map(lambda x:str(x))
    df['key'] = df['first'].str.cat(df['second'])
    dp = df.drop_duplicates(subset=['key'],keep=False)
    print(dp)
##    datalist = df.drop_dupilicates()
    df.to_csv('d:/rmdup/new/why.csv')
    dp.to_csv(uninew)
   
#for i in ['worm','yeast','human','fly','mouse']:
for i in ['human']:
    old = 'd:/rmdup/old/sl_'+i+'.csv'
    inf = 'd:/rmdup/'+i+'.csv'
    outf = 'd:/rmdup/new/'+i+'.csv'
    uninew = 'd:/rmdup/new/'+i+'_new.csv'
    print(old+','+inf+','+outf)
    combineAndRmDup(old, inf,outf)
    analysisNew(old, outf, uninew)




    
#rmDup('d:/rmdup/old/sl_fly.csv','d:/rmdup/fly.csv','d:/rmdup/new/defly.csv')
#rmDup('d:/rmdup/old/sl_human.csv','d:/rmdup/fly.csv','d:/rmdup/new/defly.csv')
#rmDup('d:/rmdup/old/sl_fly.csv','d:/rmdup/fly.csv','d:/rmdup/new/defly.csv')
#rmDup('d:/rmdup/old/sl_fly.csv','d:/rmdup/fly.csv','d:/rmdup/new/defly.csv')
#rmDup('d:/rmdup/old/sl_fly.csv','d:/rmdup/fly.csv','d:/rmdup/new/defly.csv')