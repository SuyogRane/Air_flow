
# coding: utf-8

# In[4]:


import csv
data = [('data1', 'data2','data3','data4','data5','data6','data7','data8','data9','data10')]

csvfile = open(r'new.csv', 'wb')
for row in data:
    line = ','.join(row)
    csvfile.write(line + '\n')

