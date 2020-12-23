#!/usr/bin/env python
# coding: utf-8

# # Test for book

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x = np.random.randn(50)
y = np.random.randn(50)


# In[3]:


plt.plot(x, y, "o");


# In[4]:


plt.plot(y, x, "o");

