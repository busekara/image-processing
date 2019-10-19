
# coding: utf-8

# In[99]:

get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
data_path ="C:\\Users\\Buse"
#train_data = np.loadtxt(data_path + "\mnist_train.csv", 
#                        delimiter=",")
test_data = np.loadtxt(data_path + "\mnist_test.csv", 
                       delimiter=",")


# In[100]:

import  math    
eps=np.finfo(float).eps

def my_pdf_1(x, mu=0.0 , sigma=1.0):
    x= float(x -mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma


# In[115]:

def get_my_mean_and_std(k=0,l=350):
    s=0 # kactane sıfır var onu saysın//kac digit oldugu
    #k=0 # sınfı bilgisi yani digitin
    t=0 #intersitiy degeri pixeldeki
    #l=350  #location ı belirtiyor.classın pixel degeri
    for i in range(10000):  #ortalamayı buldurdu
        if(test_data[i,0]==k):
            s=s+1
            t=t+test_data[i,l+1]
           # digit_class=train_data[i,0]
            #top_left=train_data[i,1]
            #bottom_right=train_data[i,784]
           # print(digit_class,end=" ")
            #print(top_left,end=" ")
          #  print(bottom_right,end=" \n")      
    mean_1=t/s

    s=0
    t=0
    for i in range(10000):
        if(test_data[i,0]==k):
            s=s+1
            diff_1=test_data[i,l+1]-mean_1
            t=t+diff_1*diff_1
    #var_1=t/(s-1)
    std_1=np.sqrt(t/(s-1))

    #print(mean_1,std_1)
    return mean_1,std_1


# In[116]:

get_my_mean_and_std(1,100)


# In[117]:

test_data[100,:]


# In[118]:

my_test_image=plt.imread('im_1.png')
plt.imshow(my_test_image)
plt.show() 


# In[119]:

im_2=my_test_image[:,:,0]
im_2.shape


# In[120]:

im_2[14,:]


# In[121]:

im_5=im_2.reshape(1,784)


# In[122]:

im_5.shape


# In[125]:

import math
liste = list()
for i in range(10):
    pdf_t=0
    for j in range(784): #resmin boyutu
        
        x=im_5[0,j]
        m_1,std_1=get_my_mean_and_std(i,j) #butun pıksellerın ortalaması ve varyansını buluyor.
        pdf_deger=my_pdf_1(x,m_1,std_1+eps)
        pdf_t= pdf_t+pdf_deger
        liste.append(pdf_t)
m=len(liste)
maxNumber=0
for i in range(m):
    if maxNumber < liste[i]:
        maxNumber = liste[i]
print(maxNumber)
        
        
        
        


# In[ ]:



