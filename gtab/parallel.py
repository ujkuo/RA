#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gtab


# In[3]:


t = gtab.GTAB()
t.set_active_gtab('google_anchorbank_geo=_timeframe=2017-10-01 2019-10-31.tsv')


# In[4]:


def calibrate(nameList, result, outputFileName):
    idx = 0
    for name in nameList['name']:
        query = t.new_query(name).rename(columns={"max_ratio": name}).drop(['max_ratio_hi', 'max_ratio_lo'], axis=1)
        result.append(query)
        #result[idx] = result[idx].rename(columns={"max_ratio": name})
        #result[ = tmp.drop(['max_ratio_hi', 'max_ratio_lo'], axis=1)
    tmp = result[0]
    for i in range(len(result)):
        if i != 0:
            tmp = pd.concat([tmp, result[i]], axis=1)
    tmp.to_csv(outputFileName)
    return tmp


# In[ ]:


import pandas as pd
nameList = pd.read_csv('MeToo_excel_cleaned.csv')
result = []
output1 = calibrate(nameList, result, 'cleanedTrend.csv')


# In[ ]:




