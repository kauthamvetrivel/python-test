#!/usr/bin/env python
# coding: utf-8

# In[1]:


#3rd question

fruits = (('Lemon','sour'),('DragonFruit', 'Sweet'),('Grapes','soUr'),('Kiwi','Sour'),('Apples', 'sweet'),('Orange', 'sour'),('Blueberries','sweet'),('Limes','Sour'))

sourFruits=[]

for j in fruits:
    if(j[1].lower()=='sour'):
        sourFruits.append(j[0])
 
print("Sour Fruits:", sourFruits)


# In[ ]:




