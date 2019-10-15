#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import numpy as np
import matplotlib.pyplot as plt
os.getcwd()


# In[4]:


jpg_files=[f for f in os.listdir() if f.endswith('.jpg')]
print(jpg_files)


# In[5]:


im_1=plt.imread(jpg_files[1])
type(im_1)


# In[10]:


print(im_1.ndim) #kaç boyutlu olduğu
print(im_1.shape) #boyutun piksel değerleri


# In[11]:


print(im_1[100,100,:])


# In[12]:


m,n,p=im_1.shape


# In[14]:


plt.imshow(im_1)
plt.show()


# In[31]:


im_2=im_1[:,:,0] #im_1 resmini iki boyuta indirdik.
plt.imshow(im_2)
plt.show()
plt.imsave('Merhabasonsinif.jpg',im_2) #yazılan isimle kaydedildi.


# In[18]:


new_image=np.zeros((m,n),dtype=float)


# In[35]:


for i in range(m): #resmi siyah-beyaz yapma.
    for j in range(n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3 #r,g,b degerlerının ortalamasını alıyor.
        new_image[i,j]=s
plt.imshow(new_image,cmap="gray")
plt.show()
plt.imsave('test_1.png',new_image,cmap='gray')


# In[37]:


for i in range(m): #2 boyutlu resmi siyah-beyaz yapma.
    for j in range(n):
        s=im_2[i,j] 
        new_image[i,j]=s
plt.imshow(new_image,cmap="gray")
plt.show()
plt.imsave('test_2.png',new_image,cmap='gray')


# In[40]:


#90 derece döndürme
new_image=np.zeros((n,m),dtype=float)
for i in range(m):
    for j in range(n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3
        new_image[j,i]=s
plt.imshow(new_image,cmap="gray")
plt.show()
plt.imsave('test_3.png',new_image,cmap='gray')


# In[49]:


#renk ters çevirme fonksiyonu
def my_inverse(im_1):
    return(255-im_1)


# In[56]:


im_3=im_1+25 #parlaklık arttırır.
im_4=255-im_1 #renkleri ters çevirir.
plt.imshow(im_3)
plt.show()
plt.imshow(im_4)
plt.show()


# In[ ]:




