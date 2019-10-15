#!/usr/bin/env python
# coding: utf-8

# In[20]:


import math #standart sapma ve ortalama hesaplama fonksiyonu
def my_f_1(my_list=[2,4,3,40,5,6,3,3,2,1]):
    toplam=0
    total=0
    for i in my_list:
        toplam+=i

    #hist=?
    mean=toplam/len(my_list) #ortalama
    #print(mean)

    for i in my_list:

        total+=(i-mean)*(i-mean)
    
    var=total/(len(my_list)-1)
    var=math.sqrt(var)
    #print(var)
    #std=?
    return mean,var


# In[21]:


print(my_f_1())


# In[40]:


my_histogram={} #liste
my_list=[2,4,3,40,5,6,3,3,2,1] #degerlerın frekansını buluyor.
    
for i in my_list:
    if i in my_histogram.keys():
        my_histogram[i]+=1
    else:
        my_histogram[i]=1

#my_histogram[1]=10 # value:1 değerinde olanın key:10 yap gibi.
# my_histogram[2]=15
# my_histogram[40]=40
print(my_histogram)


# In[41]:


import matplotlib.pyplot as plt
import numpy as np


# In[53]:


def my_f_2(image_1=plt.imread('istanbul.jpg')):
    print(image_1.ndim,image_1.shape)
    m,n,p=image_1.shape
    my_histogram={}
    for i in range(m):
        for j in range(n):
            if (image_1[i,j,0] in my_histogram.keys()):
                my_histogram[image_1[i,j,0]]+=1
            else:
                my_histogram[image_1[i,j,0]]=0
#             image_1[i,j,1]
#             image_1[i,j,2]

    return my_histogram


# In[54]:


print(my_f_2())


# In[59]:


x=[]

y=[]
my_histogram=my_f_2()
for key in my_histogram.keys():
    x.append(key) #value
    y.append(my_histogram[key]) #key

plt.bar(x,y)
plt.show()

print(x)
print(y)


# In[ ]:




