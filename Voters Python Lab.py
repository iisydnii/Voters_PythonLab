#!/usr/bin/env python
# coding: utf-8

# In[24]:

python
#import sys
#import scipy
import pandas as pd


# In[26]:


from pandas import read_csv
from pandas.plotting import scatter_matrix


# In[48]:


url = "https://raw.githubusercontent.com/iisydnii/Voters_PythonLab/main/20141218-dc_voters.csv"
dataset = pd.read_csv(url, error_bad_lines=False)
#print(dataset.head(20))
print(dataset.groupby(['RES_ZIP','PARTY']).size())
dataset['PARTY'].value_counts()[:20].plot(kind='barh')
pyplot.show()






