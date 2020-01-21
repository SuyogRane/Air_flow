
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv(r'new.csv')


# In[3]:


import networkx as nx
df = nx.from_pandas_edgelist(data, source='ORIGIN', target='DEST', edge_attr=True)


# In[4]:


a=input("Enter The Origin :")


# In[5]:


b=input("Enter The Destination : ")


# In[ ]:


print("The Most Shortest Past Is")


# In[10]:


shortest_path_dist = nx.dijkstra_path(df, source=a, target=b, weight='DISTANCE')
print(shortest_path_dist)

