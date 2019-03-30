#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


import warnings
warnings.filterwarnings("ignore")


# In[18]:


df = pd.read_csv("Cluster_finallist.csv", index_col=0)


# In[19]:


df.head()


# In[20]:


list = []
fh = open('Cluster_finallist.csv', 'r')
 
for line in fh:
     list.append(line.strip().split(','))
list


# In[21]:


data = " ".join(str(x) for x in list)


# In[26]:


wordcloud = WordCloud(max_font_size=100,max_words=150, background_color="white").generate(data)


# In[28]:


plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()

