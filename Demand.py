
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


print('\t\tWelcome To our Airport Management System ')


# In[3]:


data1=pd.read_csv(r'new.csv')


# In[4]:


data1.sort_values(["ORIGIN",'DEST'], axis = 0, ascending = [True,True], inplace = True, na_position ='last')


# In[5]:


a=input("Enter The City From Where U Want To Start The Journey :")


# In[6]:


b=input("Enter The City  Where U Want To End The Journey :")


# In[7]:


if data1.loc[(data1['ORIGIN']==a)&(data1['DEST']==b)].sum==0:
      print("NO FLIGHTS AVAILABLE \t")
else:
  print("\tTHE HIGHEST NOS OF DEMAND IS FOR THE AILRLINES AT THE TOP OF THE LIST \t")


# In[8]:


data1.sort_values(["PASSENGERS_ON_WAY"], axis = 0, ascending = [False], inplace = True, na_position ='last')


# In[9]:


b=data1.loc[(data1['ORIGIN']==a)&(data1['DEST']==b)]


# In[10]:


print(b.head())


# In[11]:


print("THE AIRLINES WHICH IS IN MOST DEMAND AND ITS DETAILS ARE ")


# In[12]:


print(b.head(1))

