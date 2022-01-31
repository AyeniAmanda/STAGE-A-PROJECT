#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#STAGE A PROJECT SOLUTIONS


# In[1]:


import numpy as np 


# In[2]:


import pandas as pd 


# In[9]:


food_data=pd.read_excel(r"C:\Users\dell\Documents\FoodBalanceSheets_E_Africa_NOFLAG.xlsx")  #load the dataset 


# In[10]:


food_data.head()   


# In[23]:


food_data.groupby('Item')['Y2014'].sum()     #the total sum of animal fat produced in 2014


# In[25]:


food_data.groupby('Item')['Y2017'].sum() #the total sum of animal fat produced in 2017


# In[44]:


food_data.mean()  #the mean of the whole dataset in 2015 is 135.236


# In[43]:


food_data.std() #the standard deviation of the whole dataset in 2015 is 1603.404


# In[45]:


food_data.isnull().sum()   #the total sum of the missing values in 2016 is 1535


# In[91]:


c=food_data.isnull().sum()
c['Y2016']/len(food_data)*100  #the pecentage of the missing data in 2016 is 2.52%


# In[67]:


food_data.corr()    #2014 has the highest correlation  


# In[49]:


food_data.groupby('Element').sum()   #2017 has the highest import quantity 


# In[51]:


food_data.groupby('Element')['Y2018'].sum()  #DOMESTIC SUPPLY HAS THE HIGHEST SUM IN 2018 


# In[52]:


food_data.groupby('Element')['Y2018'].sum() #SEED IS THETHRID LOWEST 


# In[111]:


food_data2=food_data[['Area','Element','Y2018']]
food_data3=food_data2.groupby(['Element','Area'])['Y2018'].sum()
food_data3['Import Quantity']    # THE TOTAL IMPORT QUANTITY IN ALGERIA IS 36238.29


# In[97]:


food_data.nunique()   #the total number of unigue is 49 


# In[ ]:




