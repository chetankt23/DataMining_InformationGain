#!/usr/bin/env python
# coding: utf-8

# In[610]:


import numpy as np
import pandas as pd

dataframe = pd.read_csv('1.csv', names=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U"])
dataframe["U"] = dataframe["U"].apply(lambda x:0 if x<1 else 1)
for column in dataframe.iloc[:,0:len(dataframe.columns)-1]:
       dataframe[column] = dataframe[column].apply(lambda x:0 if x<dataframe[column].median() else 1)

Ycount = dataframe["U"].where (dataframe["U"]==1).count()
Ncount = dataframe["U"].where (dataframe["U"]==0).count()
        
for j in dataframe.columns:
    if(j not in 'U'):
            new_df = dataframe.groupby([dataframe[j],dataframe["U"]]).size().reset_index()
            #new_df
            NN=0
            NY=0
            YN=0            
            YY=0
            for i in new_df.index:
                if new_df.iloc[i,0]==0 and new_df.iloc[i,1]==0:
                    NN=new_df.iloc[i,len(new_df.columns)-1]
                elif new_df.iloc[i,0]==0 and new_df.iloc[i,1]==1:
                    NY=new_df.iloc[i,len(new_df.columns)-1]
                elif new_df.iloc[i,0]==1 and new_df.iloc[i,1]==0:
                    YN=new_df.iloc[i,len(new_df.columns)-1]
                elif new_df.iloc[i,0]==1 and new_df.iloc[i,1]==1:
                    YY=new_df.iloc[i,len(new_df.columns)-1]
            #print (j,NN,NY,YN,YY)
            #print(new_df)
            #gini of yes node:
            gini_Y=1
            gini_N=1
            if ((YY+YN) != 0):
                gini_Y =  1- ((YY/(YY+YN))**2 )- ((YN/(YY+YN))**2 )
                #print(gini_Y)
            #gini of yes node:
            if ((NN+NY) != 0):
                gini_N =  1- ((NN/(NN+NY))**2 )- ((NY/(NN+NY))**2 )
                #print(gini_N)
                    
    
            split = (((YY+YN)/Ycount)*gini_Y)  + (((NN+NY)/Ncount)*gini_N)
            print(j,round(split,4))
            del new_df


            


# In[ ]:





# In[ ]:





# In[ ]:



                


# In[ ]:



  


# In[ ]:




