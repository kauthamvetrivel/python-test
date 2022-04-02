#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2nd question


def solve(n):
    dict = { 'Square': lambda a : a**2, 
         'Cube': lambda a : a**3, 
         'Squareroot': lambda a : a**(1/2)}
    result = 0
    for k in dict.keys():
        result += dict[k](n)
    return result
    
print(round(solve(6),2))


# In[ ]:




