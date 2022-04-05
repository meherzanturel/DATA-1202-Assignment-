#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import pandas
import pandas as pd


# In[ ]:


# Set file path to a variable
input_file_path = r"C:\Users\Durham\Desktop\Duraham\Courses\data1202\vgsales.csv"


# In[ ]:


# Read Data into a DataFrame
input_raw_data = pd.read_csv(input_file_path)


# In[ ]:


# Filter DataFrame for proper years
between_00_05 = input_raw_data[(input_raw_data["Year"] >= 2000) & (input_raw_data["Year"] <= 2005)]

print(between_00_05)


# In[ ]:


pip install pymysql


# In[ ]:


# creating an engine and connecting it to a database

# import required libraries
import pandas as pd
from sqlalchemy import create_engine
    import pymysql


# In[ ]:


# create engine
engine = create_engine('')


# In[ ]:


# connection string
conn = engine.connect()


# In[ ]:


# read a simple query into DataFrame
df = pd.read_sql("SELECT * FROM data1202.vgsales_new", conn)


# In[ ]:


# print DataFrame
print(df.head())


# In[ ]:



# TWO condition WHERE claus
action_05 = df[(df['Genre']=='Action') & (df['Year'] >= 2005)]

print("The sum of action games in NA is: " + str(action_05.NA_Sales.sum()))

