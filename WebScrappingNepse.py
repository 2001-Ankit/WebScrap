#!/usr/bin/env python
# coding: utf-8

# In[39]:


from bs4 import BeautifulSoup
import requests
url = BeautifulSoup("https://merolagani.com/StockQuote.aspx", "html.parser")
soup = requests.get(url)
soup


# In[3]:


code  = BeautifulSoup(soup.text,"lxml")
code


# In[4]:


table_code = code.table
table_code


# In[25]:


row_data=[]
for row in table_code.find_all('tr'):
  col = row.find_all('td')
  col = [ele.text.strip() for ele in col]
  row_data.append(col)
row_data


# In[6]:


import pandas as pd
df = pd.DataFrame(row_data)
df


# In[22]:


header =[]
for i in table_code.find_all('th'):
    col_name = i.text.strip()
    header.append(col_name)

header


# In[35]:


row_data=[]
for row in table_code.find_all('tr'):
  col = row.find_all('td')
  col = [ele.text.strip() for ele in col]
  row_data.append(col)
row_data.insert(1,header)
row_data


# In[36]:


import csv
with open('nep.csv','w')as file:
    x = csv.writer(file)
    for i in row_data:
        x.writerow(i)
    
    
        


# In[37]:


import pandas as pd
df =pd.read_csv('nep.csv')
df


# In[ ]:




