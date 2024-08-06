#!/usr/bin/env python
# coding: utf-8

# ![Paytm](data:image/png;base64,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)

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report


# In[2]:


df = pd.read_csv('Paytm.csv')
df


# In[3]:


df.head(10)


# In[ ]:





# In[4]:


df.isnull().sum()


# In[5]:


df.tail()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df


# In[10]:


df['Total Payments Revenue'].fillna(df['Total Payments Revenue'].mean(), inplace=True)
df['Payment processing charges'].fillna(df['Payment processing charges'].mean(), inplace=True)
df['Net Payments Margin'].fillna(df['Net Payments Margin'].mean(), inplace=True)
df['Payments Services to Merchants'].fillna(df['Payments Services to Merchants'].mean(), inplace=True)
df['Payments Services to Consumers'].fillna(df['Payments Services to Consumers'].mean(), inplace=True)


# In[11]:


df.isnull().sum()


# In[12]:


df.columns


# In[13]:


plt.plot(df['Date '],df['Payments Services to Consumers'],label='Revenue From Consumers')
plt.plot(df['Date '],df['Payments Services to Merchants'],label= 'Revenue From Merchants')
plt.plot(df['Date '],df['Total Payments Revenue'],label= 'Total Payments Revenue')
plt.title(' Rupee Revenue in INR Crores')
plt.xlabel('Year-Month')
plt.ylabel('Rupee Value in INR Cr')
plt.grid(True)
plt.xticks(rotation = 90)
plt.legend()
plt.show()


# In[14]:


plt.figure(figsize=(15,6))
sns.barplot(data=df,x=df['Registered Merchants (end of period)'],y=df['Total Transactions'])
plt.title("Transaction By Registered Merchants")
plt.show()


# In[15]:


plt.figure(figsize=(15,6))
sns.barplot(data=df,x=df['Date '],y=df['Average Monthly Transacting Users (MTU)'])
plt.title("Monthly Transaction By Users")
plt.show()


# In[16]:


plt.figure(figsize=(15,6))
sns.barplot(data=df,x=df['Date '],y=df['Total Payments Revenue'])
plt.title("Payment Revenue Perodicaly")
plt.show()


# In[17]:


plt.figure(figsize=(15,6))
sns.barplot(data=df,x=df['Average Monthly Transacting Users (MTU)'],y=df['Registered Merchants (end of period)'])
plt.title("# Average Monthly Transacting By Registered Merchants")
plt.show()


# In[18]:


plt.figure(figsize=(15,6))
sns.barplot(data=df,x=df['Date '],y=df['Payment Devices (cumulative, end of period)'])
plt.title("Payment Devices (cumulative, end of period) Perodically")
plt.show()


# In[19]:


plt.figure(figsize=(15,6))
sns.barplot(data=df,x=df['Volume of loans distributed'],y=df['Date '])
plt.title("Volume of Loan distributed Perodically")
plt.show()


# In[20]:


plt.plot(df['Date '],df['  Personal Loans'],label= 'Personal Loans')
plt.plot(df['Date '],df['  Merchant Loans'],label= 'Merchant Loans')
plt.title('Paytm : Number of differnt types of loans distributed in thousands')
plt.xlabel('Year-Month')
plt.ylabel('Number of loans distributed in thousands')
plt.grid(True)
plt.xticks(rotation = 90)
plt.legend()
plt.show()


# In[21]:


data1 = pd.read_csv('Paytm.csv')  
X = data1.drop(['Merchant Transactions','Date ','Total Transactions','Average Monthly Transacting Users (MTU)','Total Payments Revenue','Payment processing charges','Net Payments Margin'], axis=1)  
y = data1['Net Payments Margin']


# In[22]:


X


# In[23]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[24]:


model = RandomForestRegressor()
model.fit(X_train, y_train)


# In[27]:


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




