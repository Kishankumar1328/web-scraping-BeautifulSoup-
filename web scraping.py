#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[73]:


url="https://www.flipkart.com/redmi-note-13-pro-plus-coming-soon-store?param=3673"


# In[74]:


http=requests.get(url)


# In[75]:


http


# In[76]:


soup=BeautifulSoup(http.content,"html.parser")


# In[77]:


soup


# In[78]:


soup.p


# In[79]:


soup.title


# In[80]:


soup.title.name


# In[81]:


soup.a


# In[82]:


print(soup.get_text())


# In[ ]:





# In[ ]:




