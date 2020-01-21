
# coding: utf-8

# In[17]:


import pandas as pd


# In[18]:


print('\t\tWelcome To our Airport Management System ')


# In[19]:


data1=pd.read_csv(r'new.csv')


# In[20]:


data1.sort_values(['AIRLINE_NAME'], axis = 0, ascending = [True], inplace = True, na_position ='last')
q=input('Enter Airline name : ')


# In[21]:


data1.sort_values(["ORIGIN",'DEST'], axis = 0, ascending = [True,True], inplace = True, na_position ='last')


# In[22]:


a=input("Enter The City From Where U Want To Start The Journey : ")


# In[8]:


#data1.head()


# In[23]:


b=input("Enter The City  Where U Want To End The Journey : ")


# In[24]:


#for a in data1


# In[25]:


if (data1.loc[(data1['ORIGIN']==a)&(data1['DEST']==b)].sum)==0:
      print("NO FLIGHTS AVAILABLE \t")
else:
    print("\tThe Schedule Is\t")


# In[26]:


b=data1.loc[(data1['ORIGIN']==a)&(data1['DEST']==b)]


# In[28]:


print(b)


# In[29]:


print("\n\t\tIf We Sort On The Basis Of Time The Schedule Will be ")


# In[30]:


b.sort_values(["AIR_TIME"], axis = 0, ascending = [True], inplace = True, na_position ='last')


# In[32]:


#print("\t\tThe schedule is")
print(b)


# In[ ]:




