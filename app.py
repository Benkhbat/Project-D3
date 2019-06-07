#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Dependecies
import pandas as pd
from flask import Flask, flash, redirect, render_template, request, session, jsonify, Markup, abort


# In[2]:


# Read the file
superstore = "Superstore.xls"
superstore_df = pd.read_excel(superstore)


# In[3]:


superstore_df.head(2)


# In[4]:


Superstore = superstore_df[["City", "State", "Code", "Latitude", "Longitude", "Category", "Sales", "Profit"]]
Superstore


# In[5]:


# SQLAlchemy dependencies 

# To create engine & declarative base 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# For data types
from sqlalchemy import Column, Integer, String, Float, Date

# Create base
Base = declarative_base()


# In[6]:


Base.metadata.clear()
# Creates Classes which will serve as the anchor points for our Tables
class Orders(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'Orders'
    index = Column(String, primary_key=True)
    City = Column(String(255),nullable=True)
    State = Column(String(255),nullable=True)
    Code = Column(String(255),nullable=True)
    Latitude = Column(Float,nullable=True)
    Longitude = Column(Float,nullable=True)
    Category = Column(String(255),nullable=True)
    Sales = Column(Float,nullable=True)
    Profit = Column(Float,nullable=True)
    


# In[7]:


# Create a sqlite engine
engine = create_engine("sqlite:///superstore.sqlite")


# In[8]:


# Add metadata to tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# In[9]:


# Data from Excel to respective tables
Superstore.to_sql('Orders',engine, if_exists='append',index=True)


# In[11]:


Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
session = Session(engine)
results = session.query(Orders.index, Orders.City, Orders.State, Orders.Code, Orders.Latitude, Orders.Longitude, 
                        Orders.Category, Orders.Sales, Orders.Profit).all()


# In[16]:


mydata=jsonify(results)
app = Flask(__name__)

@app.route('/')
def home():
  #dat=jsonText
  #return "Hello"
  return render_template("index.html",dat=mydata)

if __name__ == "__main__":
  app.run(debug=True)


# In[ ]:





# In[ ]:




