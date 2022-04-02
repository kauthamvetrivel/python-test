#!/usr/bin/env python
# coding: utf-8

# In[1]:


#5th question

d = {'John':45, 'Shelly':65, 'Marry':35}

calc_grav = lambda x: round((x / 9.81) * 1.622, 2)

calc = lambda k: (k,  calc_grav(d[k]))

r  = dict(calc(k) for k in d)

print(r)


# In[ ]:




