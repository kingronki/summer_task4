#!/usr/bin/env python
# coding: utf-8

# 🔅 Task 4.1
# 📌 Create image by yourself Using Python Code 
# 

# In[1]:


import cv2
import numpy as np


# In[2]:


arr = np.empty(shape = (240,1020,3))
arr.shape


# In[3]:


B=0
G=0
R=0
for j in range(0,255):
    arr[:,j] = [B,G,R]
    R+=1
    
for j in range(255,510):
    arr[:,j] = [B,G,R]
    G+=1
    R-=1

for j in range(510,765):
    arr[:,j] = [B,G,R]
    B+=1
    G-=1

for j in range(765,1020):
    arr[:,j] = [B,G,R]
    B-=1

    
cv2.imwrite("pic1.jpg",arr)
pic = cv2.imread("pic1.jpg")
cv2.imshow("untitled",pic)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 🔅 Task 4.2
# 📌 Take 2 image crop some part of both image and swap it.

# In[1]:


import cv2


# In[2]:


photo1 = cv2.imread("WhatsApp Image 2021-06-02 at 11.51.48 PM.jpeg")
photo2 = cv2.imread("WIN_20191118_19_44_56_Pro.jpg")


# In[3]:


dup_photo1 = cv2.imread("WhatsApp Image 2021-06-02 at 11.51.48 PM.jpeg")
dup_photo2 = cv2.imread("WIN_20191118_19_44_56_Pro.jpg")


# In[4]:


cp_ph1 = photo1
cp_ph2 = photo2
cp_dph1 = dup_photo1
cp_dph2 = dup_photo2


# In[5]:


cv2.imshow("Photo1",photo1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[6]:


photo1.shape


# In[7]:


cv2.imshow("Photo2",photo2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[8]:


photo2.shape


# In[9]:


crop_ph1 = photo1[200:600,330:600]


# In[10]:


cv2.imshow("crop_ph1",crop_ph1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[11]:


crop_ph1.shape


# In[12]:


cp_ph2[30:430,535:805] = crop_ph1


# In[13]:


cv2.imshow("swap2",cp_ph2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[14]:


crop_ph2 = dup_photo2[30:430,535:805]


# In[15]:


cv2.imshow("crop_ph2",crop_ph2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[16]:


crop_ph2.shape


# In[17]:


cp_dph1[200:600,330:600] = crop_ph2


# In[18]:


cv2.imshow("swap1",cp_dph1)
cv2.waitKey()
cv2.destroyAllWindows()


# 🔅 Task 4.3
# 📌 Take 2 image and combine it to form single image. For example collage 

# In[19]:


import numpy as np


# In[20]:


final = np.hstack((crop_ph1,crop_ph2))


# In[ ]:





# In[22]:


cv2.imshow("final",final)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




