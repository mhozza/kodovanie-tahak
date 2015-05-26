
# coding: utf-8

# In[4]:

a = list()
with open('table.txt') as f:
    a = [l.split() for l in f]
        


# In[5]:

a


# In[8]:

for i, l in enumerate(a):
    a[i] = ['']*(15-len(l)) + l
    print(l)


# In[9]:

a


# In[14]:

print(list(zip(*a)))


# In[19]:

def merge(x, y):
    z = list()
    for x1, y1 in zip(x, y):        
        z1 = list()
        for x2, y2 in zip(x1, y1):
            z2 = x2 + y2
            z1.append(z2)
        z.append(z1)
    return z

            


# In[21]:

b = merge(a, list(zip(*a)))


# In[22]:

for line in b:
    print(*line)


# In[ ]:



