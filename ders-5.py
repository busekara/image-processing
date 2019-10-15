#!/usr/bin/env python
# coding: utf-8

# In[41]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[42]:


data_path ="C:\\Users\\Buse"
train_data = np.loadtxt(data_path + "\mnist_train.csv", 
                        delimiter=",")
test_data = np.loadtxt(data_path + "\mnist_test.csv", 
                       delimiter=",")


# In[43]:


image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size #784
data_path = "data/mnist/"
test_data[:10]


# In[44]:


train_data.ndim, train_data.shape


# In[45]:


train_data[10,0]


# In[46]:


im_3=train_data[10,:] #resimde 10.satır tamamen alındı 3 dahil 


# In[47]:


im_3.shape ## im_3te butun pixel bilgisi var


# In[48]:


im_4=im_3[1:] #label ı attık


# In[49]:


im_4.shape


# In[50]:


im_5=im_4.reshape(28,28)


# In[52]:


plt.imshow(im_5)
plt.show()


# In[53]:


plt.imshow(im_5,cmap="gray")
plt.show()


# In[54]:


60000 ,785 ; 1+ 28*28


# In[55]:


#train datada kac tane 3 oldugunu bulan fonksiyonu yaz.
#60000 data var 785 lik ve bir tanesi label 28*28lik resimler.


# In[56]:


m,n=train_data.shape
m,n


# In[57]:


def my_counter(k=0):
    s=0
    for i in range(m):
        if(train_data[i,0]==k): # burada 3 degeri label degeri oluyor ve label'da hangi sayı oldugunu gosteriyor datasetinde.
            s=s+1 #i satır j sutun degerleri
    return s


# In[58]:


for i in range(10):
    c=my_counter(i) 
    print(i," ",c)


# In[59]:


print(my_counter(2))


# In[60]:


#sıfır digitinin sol üstteki pixelin ortalaması ve standart sapma degeri nedir ?


# In[61]:


# digit_class=train_data[i,0]
    # top_left=train_data[i,1]
    # bottom_right=train_data[i,784]
    # print(digit_class,end=" ")
    # print(top_left,end=" ")
    # print(bottom_right,end=" ") #end son kareketere bosluk bırakıyor.


# In[62]:


import  math
def my_pdf_1(x, mu=0.0 , sigma=1.0):
    x= float(x -mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma


# In[63]:


my_pdf_1(10,1,3)


# In[64]:


#m,n=im_1.shape


# In[65]:


def get_my_mean_and_std(k=0,l=350):
    s=0 # kactane sıfır var onu saysın//kac digit oldugu
    #k=0 # sınfı bilgisi yani digitin
    t=0 #intersitiy degeri pixeldeki
    #l=350  #location ı belirtiyor.classın pixel degeri
    for i in range(m):  #ortalamayı buldurdu
        if(train_data[i,0]==k):
            s=s+1
            t=t+train_data[i,l+1]
           # digit_class=train_data[i,0]
            #top_left=train_data[i,1]
            #bottom_right=train_data[i,784]
           # print(digit_class,end=" ")
            #print(top_left,end=" ")
          #  print(bottom_right,end=" \n")      
    mean_1=t/s

    s=0
    t=0
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            diff_1=train_data[i,l+1]-mean_1
            t=t+diff_1*diff_1
    #var_1=t/(s-1)
    std_1=np.sqrt(t/(s-1))

    print(mean_1,std_1)
    return mean_1,std_1
        # train_data[i,0] #label
        # train_data[i,1] #sol üstteki deger
        # train_data[i,784]#en alt kosedeki deger 


# In[66]:


#yukarda ortalamayı bulduk, ortalama ve varyansı olan degerin pdf degeri nedir ?


# In[68]:


m_1,std_1=get_my_mean_and_std(2,100)
#my_pdf_1(test_value,m_1,std_1) #(40 intersitiy degerinin ) 2.labelın 100. pixelinde 40 degerinin bulunma olasılıgı
#test value yerine normalde 40 degerini yazmıstık.


# In[71]:


im_1=plt.imread("1.png")
plt.imshow(im_1,cmap='gray')
plt.show()
#test_value=im_1[0,0,0]


# In[ ]:


#resmin hangi sayı oldugunu buldurunuz.


# In[ ]:




