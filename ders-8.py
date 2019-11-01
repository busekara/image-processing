#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt


# In[8]:


x=[180,170,170,175,181,175,177,185,179,160]
y=[95,70,60,79,60,63,83,80,75,50]


# In[9]:


x,y,len(x),len(y)


# In[10]:


X=np.stack((x,y),axis=0)
X


# In[15]:


sigma_1=np.cov(X)
sigma_1


# In[16]:


# X_test=np.stack((x,x),axis=0)
# X_test


# In[17]:


# sigma_2=np.cov(X_test)
# sigma_2


# In[19]:


def generate_data():
    x=[180,170,170,175,181,175,177,185,179,160]
    y=[95,70,60,79,60,63,83,80,75,50]
    X=np.stack((x,y),axis=0)
    return X
def get_cov_matrix(X):
    sigma_1=np.cov(X)
    return sigma_1


# In[20]:


data_1=generate_data()
get_cov_matrix(data_1)


# In[21]:


def multivariate_normal(x, d, mean, covariance):
    """pdf of the multivariate normal distribution."""
    x_m = x - mean
    return (1. / (np.sqrt((2 * np.pi)**d * np.linalg.det(covariance))) * 
            np.exp(-(np.linalg.solve(covariance, x_m).T.dot(x_m)) / 2))


# In[44]:


x=generate_data()
print(np.mean(x[0,:]),np.mean(x[1,:]))
x_1=[175,72]
d_1=2
data=generate_data()
mean_1=np.array([np.mean(x[0,:]),np.mean(x[1,:])]) #boyların ve kıloların ortalaması
covariance_1=get_cov_matrix(data)
multivariate_normal(x_1,d_1,mean_1,covariance_1)


# In[43]:


for i in range(20):
    v=167+i
    x_1=[v,72]
    s=multivariate_normal(x_1,d_1,mean_1,covariance_1)
    print(v,"    ",s)
    


# In[ ]:




