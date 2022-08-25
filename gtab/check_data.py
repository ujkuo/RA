#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('number_calibrate.csv')
df2 = pd.read_csv('clean_calibrate.csv')


# In[3]:


df2 = df2.set_index('date')


# In[4]:


df = df.set_index('date')


# In[5]:


df


# In[6]:


nameList = []
for name in df.columns:
    #print(name)
    #print(df[name].max(), df[name].min())
    if df[name].max() - df[name].min() >= 20:
        nameList.append(name)


# In[7]:


nameList2 = []
for name in df2.columns:
    #print(name)
    #print(df[name].max(), df[name].min())
    if df2[name].max() - df2[name].min() >= 20:
        nameList2.append(name)


# In[8]:


df2[nameList2]


# In[9]:


df[nameList].plot()


# In[41]:


period = (df.index > '2017-10-01') & (df.index < '2018-03-01')
period


# In[10]:


df[['Harvey Weinstein', 'Kevin Spacey', 'Matt Lauer', 'Sylvester Stallone', 'Al Franken']].plot()


# In[37]:


clean_origin[clean_origin['name'].isin(['Harvey Weinstein', 'Kevin Spacey', 'Matt Lauer', 'Sylvester Stallone', 'Al Franken'])]


# In[42]:


df[['Harvey Weinstein', 'Kevin Spacey', 'Matt Lauer', 'Sylvester Stallone', 'Al Franken']].loc[period].plot()


# In[11]:


df[['Al Franken', 'Larry Nassar', 'Roy Moore']].plot()


# In[28]:


clean_origin = pd.read_csv('GoogleTrends/MeToo_20210302.csv')
clean_origin[clean_origin['name'].isin(['Al Franken', 'Larry Nassar', 'Roy Moore'])]
#df[['Al Franken', 'Larry Nassar', 'Roy Moore']].plot()


# In[43]:


df[['Al Franken', 'Larry Nassar', 'Roy Moore']].loc[period].plot()
"""
Nassar was sentenced to 60 years in federal prison on December 7, 2017,
after pleading guilty to child pornography and tampering with evidence charges on July 11, 2017. 
On January 24, 2018, 
Nassar was sentenced to an additional 40 to 175 years in Michigan State prison after pleading guilty in Ingham County to seven counts of sexual assault of minors
"""


# In[36]:


df['Larry Nassar'].idxmax()


# In[12]:


df2[nameList2].plot()


# ## Regression
# - How to select $\tau$?
# - Use the maximun likelihood to eslimate?
# - Estimate $\alpha$ or use the same $\alpha$ for regression 2
# - MLE for regression 2

# In[ ]:




