#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import nltk
import numpy as np
import re


# In[16]:


#functions
def returnMatches(description, blockchain):
    return [x for x in blockchain if x in description]


# In[39]:


dummydata = pd.read_csv("C:\Program Files\Docker Toolbox\product\DockerAssignment2\Job_Description_Team_7 - BB&T Corp.csv")
print(dummydata.shape)
dummydata.head()
dummy=dummydata.apply(pd.Series)


# In[40]:


#print(dummy.head())23422
link=dummy['Job_Link']
#print(link.head(1))
title=dummy['Job_Title']
#print(title.head(1))
descrip=dummy['Job_Description']
#print(descrip.head(1))
bankname=dummy['Bank_Name']
#print(bankname.head(5))
bankname.shape


# In[42]:


dummy1 = pd.read_csv("C:\Program Files\Docker Toolbox\product\DockerAssignment2\Cluster_finallist.csv")
#print(dummy1.shape)
#dummy1.head()
#dum=dummy1.apply(pd.Series)
#print(dummy1)


# In[43]:


blockchain=dummy1['blockchain']
infotech=dummy1['information technology']
analysis=dummy1['data analytics']
cog=dummy1['cognitive']
cyber=dummy1['cyber security']
database=dummy1['Database']
cloudcomputing=dummy1['cloud computing']
finance=dummy1['financial management']
technology=dummy1['technology']
allkeywords=dummy1['all']


# In[44]:


blockchain_list = []  
infotech_list=[]
analysis_list=[]
cog_list=[]
finance_list=[]
cyber_list=[]
cloudcomputing_list=[]
finance_list=[]
database_list=[]
technology_list=[]
jobtype=[]
categorytype=[]
categorynumber=[]
jobtypenumber=[]
dict={}

list1=' '
indexvalue=len(dummy.index)

for i in range(0,indexvalue):
    if isinstance(descrip.iloc[i], str):
        tokenized_desc=nltk.word_tokenize(descrip.iloc[i].lower())

        blockchainvar=','.join(returnMatches(tokenized_desc,blockchain))
        dict['blockchain']=len(returnMatches(tokenized_desc,blockchain))
        blockchain_list.append(blockchainvar)

        itvar=','.join(returnMatches(tokenized_desc,infotech))
        dict['infotech']=len(returnMatches(tokenized_desc,infotech))
        infotech_list.append(itvar)

        analysisvar=','.join(returnMatches(tokenized_desc,analysis))
        dict['data analysis']=len(returnMatches(tokenized_desc,analysis))
        analysis_list.append(analysisvar)

        cogvar=','.join(returnMatches(tokenized_desc,cog))
        dict['cognitive science']=len(returnMatches(tokenized_desc,cog))
        cog_list.append(analysisvar)

        cybervar=','.join(returnMatches(tokenized_desc,cyber))
        dict['cyber']=len(returnMatches(tokenized_desc,cyber))
        cyber_list.append(cybervar)

        databasevar=','.join(returnMatches(tokenized_desc,database))
        dict['database']=len(returnMatches(tokenized_desc,database))
        database_list.append(databasevar)

        cloudcomputingvar=','.join(returnMatches(tokenized_desc,cloudcomputing))
        dict['cloudcomputing']=len(returnMatches(tokenized_desc,cloudcomputing))
        cloudcomputing_list.append(cloudcomputingvar)

        financevar=','.join(returnMatches(tokenized_desc,finance))
        dict['finance']=len(returnMatches(tokenized_desc,finance))
        finance_list.append(financevar)
        
        techlist=','.join(returnMatches(tokenized_desc,technology))
        dict['technology']=len(returnMatches(tokenized_desc,technology))
        technology_list.append(techlist)
        
        

        sorted_by_value = sorted(dict.items(), key=lambda kv: kv[1],reverse=True)

        for value in sorted_by_value[:1]:
            key,data=value
            if data!=0:
                jobtype.append(key)
                if (key=='blockchain'):
                    jobtypenumber.append(1)
                elif(key=='infotech'):
                    jobtypenumber.append(3)
                elif(key=='data analysis'):
                    jobtypenumber.append(2)
                elif(key=='cognitive science'):
                    jobtypenumber.append(7)
                elif(key=='cyber'):
                    jobtypenumber.append(4)
                elif(key=='database'):
                    jobtypenumber.append(6)
                elif(key=='cloudcomputing'):
                    jobtypenumber.append(5)
                else:
                    jobtypenumber.append(8)                
            else:
                jobtype.append('finance')
                jobtypenumber.append(8)
            if isinstance(title.iloc[i], str):
                tokenized_word=re.split(r'; |, |\*|\n|-|\s',(title.iloc[i].lower()))
                if (blockchainvar) or (itvar) or ( analysisvar) or  (cogvar) or (cybervar) or (databasevar) or (cloudcomputingvar):
                    tokenized_title=nltk.word_tokenize(title.iloc[i].lower())
                    list1=','.join(returnMatches(tokenized_word,allkeywords)) 
                    if (len(list1)!=0):
                        categorytype.append('fintech')
                        categorynumber.append(1) 
                    else:
                        categorytype.append('nonfintech')
                        categorynumber.append(0)
                else:
                    categorytype.append('nonfintech')
                    categorynumber.append(0)
            else:
                blockchain_list.append('')
                infotech_list.append('')
                analysis_list.append('')
                finance_list.append('')
                cog_list.append('')
                cyber_list.append('')
                database_list.append('')
                cloudcomputing_list.append('')
                jobtype.append('')
                categorytype.append('')
                categorynumber.append('')
                jobtypenumber.append('')
                technology_list.append('')
    else:
        print(descrip.iloc[i])
        blockchain_list.append('')
        infotech_list.append('')
        analysis_list.append('')
        finance_list.append('')
        cog_list.append('')
        cyber_list.append('')
        database_list.append('')
        cloudcomputing_list.append('')
        jobtype.append('')
        categorytype.append('')
        categorynumber.append('')
        jobtypenumber.append('')
        technology_list.append('')
#print(len(blockchain_list))
#print(len(infotech_list))
#print(len(analysis_list))
#print(len(cog_list))
#print(len(datascience_list))
#print(len(cyber_list))
#print(len(cloudcomputing_list))
#print(len(database_list))
#print(len(jobtype))
print(len(technology_list))


# In[36]:


print(len(blockchain_list))
print(len(infotech_list))
print(len(analysis_list))
print(len(cog_list))
#print(len(datascience_list))
print(len(cyber_list))
print(len(cloudcomputing_list))
print(len(database_list))
print(len(jobtype))
print(len(technology_list))


# In[37]:


dummy['blockchain']=blockchain_list
dummy['IT']=infotech_list
dummy['analysis']=analysis_list
dummy['cognitive science']=cog_list
#dummy['data science']=datascience_list
dummy['cyber security']=cyber_list
dummy['database']=database_list
dummy['cloud computing']=cloudcomputing_list
dummy['financial Management']=finance_list
dummy['Job Category']=jobtype
dummy['fintech-NonFintech']=categorytype
dummy['Fin-Nonfin number']= categorynumber
dummy['Job Category Number ']=jobtypenumber
dummy['Technology']=technology_list


# In[38]:


dummy.to_csv('C:\Program Files\Docker Toolbox\product\DockerAssignment2\analysis8.csv')


# In[32]:


def fun(val):
    list1=','.join(dummy[val])
    list2=list1.split(',')
    dict={}
    filename=val+'.csv'
    for value in list2:
    #print(value)
        if value not in dict and  isinstance(value, str) and value != '':
            a=len(re.findall(value,list1))
            dict[value]=a
    value = sorted(dict.items(), key=lambda kv: kv[1],reverse=True)
    
    wordcount= pd.DataFrame(columns=[val])
    wordcount[val]=pd.Series(value)
    wordcount.to_csv(filename)
    return value


# In[16]:


blockchain_wordlist=fun('blockchain')
IT_wordlist=fun('IT')
analysis_wordlist=fun('analysis')
cog_wordlist=fun('cognitive science')
cyber_wordlist=fun('cyber security')
database_list=fun('database')
fs_wordlist=fun('financial Management')
cloud_wordlist=fun('cloud computing')

