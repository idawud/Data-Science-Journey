#!/usr/bin/env python
# coding: utf-8

# # The Pandas Notebook

# In[3]:


import pandas as pd


# In[12]:


data = pd.read_csv('health-facilities-gh.csv')


# In[17]:


data.head()


# In[15]:


data


# In[22]:


#return the data type of all colums
data.dtypes


# pd.to_datatime(data.Timestamp, unit='s')
# to convert a Timestamp int64 column to date

# In[44]:


accra = data[data['Region'] == 'Greater Accra' ]


# In[45]:


accra


# In[78]:


data[data['Town'] == 'Madina']


# In[49]:


data.iloc[200:500]


# In[54]:


data.iloc[1854]


# In[63]:


data[data['Ownership'] == 'Government'].count()


# In[62]:


data.count()


# In[65]:


sofar = data.count().Region - data[data['Ownership'] == 'Government'].count().Region
sofar


# In[72]:


sofar - data[data['Ownership'] == 'Private'].count().Region - data[data['Ownership'] == 'CHAG'].count().Region


# In[94]:


owners = list(data['Ownership'].unique())
sorted(owners)


# In[88]:


for owner in owners:
    print(owner, " ==> ", data[data['Ownership'] == owner].count().Region)


# In[89]:


data[data['Type'] == 'Clinic'].count()


# In[90]:


data[data['Ownership'] == 'Muslim']


# In[100]:


data[data['Town'] == 'Adenta']


# In[106]:


len(data['District'].unique())


# In[108]:


len(data[data['FacilityName'] =='Swan Clinic'])


# In[109]:


x = data[data['FacilityName'] =='Swan Clinic']
print(x)


# In[ ]:




