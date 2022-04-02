#!/usr/bin/env python
# coding: utf-8

# In[1]:


#6th question


ls = ["santa Maria" , "Hello World" , " Merry christmas", "tHank You"]


o = []
for i in ls:
    a ,b = i.split()
    if a[0].isupper(): 
        o.append(a)
    if b[0].isupper():o.append(b)
print(o)


# In[ ]:




