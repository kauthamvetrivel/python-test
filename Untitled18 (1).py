#!/usr/bin/env python
# coding: utf-8

# In[3]:


#10th question

datelists=['17-12-1997','22-04-2011','01-05-1993','19-06-2020']
out=[]
for r in datelists:
    d=r.split("-")
    out.append(d[2])
    print("output",out)


# In[ ]:




