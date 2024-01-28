#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


mylist = [1,2,3]


# In[3]:


type(mylist)


# In[4]:


np.array(mylist)


# In[5]:


mylist


# In[6]:


myarr = np.array(mylist)


# In[7]:


myarr


# In[8]:


type(myarr)


# In[9]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]


# In[11]:


my_matrix


# In[12]:


np.array(my_matrix)


# In[16]:


np.arange(0,101,20)


# In[15]:


np.zeros(5)


# In[17]:


np.zeros((2,5))


# In[18]:


np.ones(5)


# In[20]:


np.linspace(0,10,11)


# In[23]:


len(np.linspace(0,10,11))


# In[29]:


np.random.rand(5,2)


# In[30]:


np.random.randn(10)


# In[31]:


np.random.randn(2,3)


# In[34]:


np.random.randint(0,101,(4,5))


# In[35]:


np.random.seed(101)
np.random.rand(4)


# In[36]:


np.random.seed(101)
np.random.rand(4)


# In[37]:


np.random.rand(4)


# In[38]:


np.random.seed(101)
np.random.rand(4)


# In[39]:


arr= np.arange(0,25)


# In[42]:


arr.reshape(5,5)


# In[45]:


ranarr = np.random.randint(0,101,10)

ranarr
# In[46]:


ranarr


# In[47]:


ranarr.max()


# In[48]:


ranarr.min()


# In[49]:


ranarr.argmax()


# In[51]:


ranarr.argmin()


# In[53]:


ranarr.dtype


# In[54]:


arr


# In[55]:


arr.shape


# In[56]:


arr.reshape(5,5)


# In[57]:


arr.shape


# In[59]:


arr.reshape(1,25)


# In[ ]:




