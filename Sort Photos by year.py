#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil
import time

SEP=os.sep

ricoh = f'D:{SEP}Photo Archive{SEP}Ricoh BackUp'

my_pics = f'C:{SEP}Users{SEP}Nicholas{SEP}Pictures'


cwd = my_pics


os.chdir(cwd)


# In[2]:


year_list = []
year_month_list=[]
for r,d,files in os.walk(cwd):
    for file in files:# Get a list of years for each of the photos in the drive
#         print(r,file)
        year_month_list.append(time.strftime('%Y_%m%b',time.localtime(os.path.getmtime(os.path.join(r,file)))))
        
print(sorted(set(year_month_list)))


# In[3]:



for i in year_month_list:  # Create a folder for each year month
    try:
        os.mkdir(os.path.join(cwd,i))
    except FileExistsError: # Check if folder is present
        continue

# print(os.path.join(cwd,time.strftime('%Y_%b',time.localtime(os.path.getmtime(file)))))


# In[4]:


'''Only use this code when you are restructuring a folder 
or organising a directory with multiple folders because it recursively goes through every file in each folder'''


'''
for r,d,files in os.walk(cwd):
    print(len(files))
    for file in files:
        try:
#           print(os.path.join(r,file),os.path.join(cwd,time.strftime('%Y_%m_%b',time.localtime(os.path.getmtime(os.path.join(r,file)))),file))
            shutil.move(os.path.join(r,file),os.path.join(cwd,time.strftime('%Y_%m%b',time.localtime(os.path.getmtime(os.path.join(r,file)))),file))
            print(f'moved {file}')
        except:
            continue
    else:
        pass'''
        



# In[5]:


'''To move files in top level into respective folders, use this instead'''
for file in os.listdir(cwd):
    if os.path.isfile(file):
        try:
    #       print(os.path.join(r,file),os.path.join(cwd,time.strftime('%Y_%m_%b',time.localtime(os.path.getmtime(os.path.join(r,file)))),file))
            shutil.move(os.path.join(cwd,file),os.path.join(cwd,time.strftime('%Y_%m%b',time.localtime(os.path.getmtime(os.path.join(cwd,file)))),file))
        except:
            continue

    else:
        pass


# In[ ]:




