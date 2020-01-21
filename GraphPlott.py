
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import ipython as get_ipython
data = pd.read_csv(r'new.csv')


# In[2]:


import networkx as nx
df = nx.from_pandas_edgelist(data, source='ORIGIN', target='DEST', edge_attr=True)


# In[4]:


print("We Are Plotting A Graph In Between All Origin And Destination To Show All The Possible Connections Avaibale")


# In[5]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.figure(figsize=(12,8))
nx.draw_networkx(df, with_labels=True)

