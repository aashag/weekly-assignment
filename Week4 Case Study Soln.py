#!/usr/bin/env python
# coding: utf-8

# # Case Study on presentation of data

# **I. Do the following operations on cars_data dataset**

# **Solution.**

# In[36]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# **1.To read the dataset to the python environment**

# In[4]:


dataset=pd.read_csv("cars_data (1).csv")


# In[5]:


dataset.head()


# In[35]:


dataset.columns


# **2. To check the null values in the dataset.**

# In[6]:


dataset.isnull().sum()


# **3. To plot a bargraph on male vs female buyers participated in the sales.**

# In[37]:


import warnings
warnings.filterwarnings("ignore")


# In[38]:


sns.countplot(dataset['Buyer Gender'])
plt.grid()


# **Inference:Number of female buyers of different models of cars in the given dataset is slightly more than that of male buyers**

#  **4. To find the top 5 cars based on their sales price**

# In[17]:


data_top5=dataset.nlargest(5,'Sale Price')


# In[18]:


data_top5


# In[31]:


data_top5[['Model','Sale Price']]


# **5. To find the least 5 cars based on their Resell price.**

# In[32]:


data_last5=dataset.nsmallest(5,'Resell Price')


# In[33]:


data_last5


# In[34]:


data_last5[['Model','Resell Price']]


# In[ ]:




