#!/usr/bin/env python
# coding: utf-8

# In[37]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[41]:


company=['GOOGLE','AMZN','MSFT','FB']
revenue = [90,136,76,95]
profit = [31,26,44,56]


# In[42]:


xpos = np.arange(len(company))
xpos


# In[46]:


plt.xticks(ypos,company)
plt.xlabel("revenue(bln)")
plt.xlabel("Company Names")
plt.title("US Tech Stocks")
plt.bar(xpos-0.2,revenue,width=0.4,label="Revenue")
plt.bar(xpos+0.2,profit,width=0.4,label="profit")
plt.legend()


# In[ ]:





# In[ ]:




