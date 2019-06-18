#!/usr/bin/env python
# coding: utf-8

# In[208]:


myfile = open('Information regarding address.eml')


# In[209]:


string1 = 'Content-Type: text/plain; charset="UTF-8"'


# In[210]:


string2 = "--"


# In[211]:


body = ""
subject = ""
fromAdress = ""


# In[212]:


flag= False
count=0
for line in myfile.readlines():
    
    if line[0:7] == 'Subject':
        subject = line
    if line[0:4] == 'From':
        fromAdress = line
    if string1 in line:
        flag= True
        count= count+1
        continue
    if string2  in line:
        if(count>=1):
            flag = False 
    if flag and count==1:
        body = body + " "+ line
        
        

        
        
        


# In[213]:


body = body.replace('Content-Transfer-Encoding: quoted-printable','')
body = body.replace('=E2=80=99',"'")
body = body.replace("= ","")
body = body.replace("=","")


# In[214]:


print(subject)
print(fromAdress)
print(body)


# In[ ]:




