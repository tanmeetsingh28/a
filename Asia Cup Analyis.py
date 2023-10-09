#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go 


# # Asia Cup Analysis 

# In[9]:


data = pd.read_csv("C:\\Users\\Admin\\Downloads\\Db\\asiacup.csv")


# In[10]:


data 


# # Number of Matches won by Each Team By in Asia Cup 2022

# In[13]:


figure = px.bar(data,x=data["Opponent"], title= "Number of matches won in Asia 2022")
figure.show()


# In[14]:


figure = px.bar(data,x=data['Player Of The Match'],title="Player Of The match")
figure.show()


# In[19]:


figure = px.bar(data, y=data["Team"],x=data["Highest Score"],color=data["Highest Score"],title="Highest Score By Team")
figure.show()    


# In[ ]:




