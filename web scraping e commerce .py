#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests


# In[6]:


url="https://www.flipkart.com/laptops-store?otracker=nmenu_sub_Electronics_0_Laptops"


# In[7]:


http=requests.get(url)


# In[8]:


http.content


# In[9]:


soup=BeautifulSoup(http.content,"html.parser")


# In[10]:


soup


# In[11]:


soup.title


# In[12]:


soup.p


# In[13]:


soup.a


# In[14]:


kkk=soup.find(id="link3")


# In[15]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[16]:


soup.find_all('a')


# In[17]:


print(soup.get_text())


# In[ ]:




