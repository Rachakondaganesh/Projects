from pydoc import describe

import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import barplot

#THE BANKING PROJECT
connect=pymysql.connect(host="localhost",
                        user="root",
                        password="ganesh",
                        db="bank_data")

query="select * from bank_data.customer"
df=pd.read_sql(query,connect)
connect.close()
df.info()

# DATA IS CLEANED SO WE DONT GOING THROUGH WITH HANDLING MISSING VALUES

print(df)
print("shape of the data",df.shape)
print("descriptive statatics\n",df.describe()) #it show the all numerical values related data from the bank_data
b1=df["Estimated Income"].min()
b2=df["Estimated Income"].value_counts()
print(b1,b2)## O/P=15k
bins=[0,100000,300000,float('inf')]
label=["low","med","high"]
df["Income Band"]=pd.cut(df["Estimated Income"],bins=bins,labels=label,right=False)
INCOMEBAND=df["Income Band"].value_counts().plot(kind="bar")
print(INCOMEBAND)
plt.show()#based on this graph we can find what type of customers are more

#EXMANINE THE DISTRIBUTIONS OF UNIQUE CATEGORIES IN CATEGORICAL COLUMNS

categorical_cols=df[["Nationality","Occupation",
                     "Fee Structure","Amount of Credit Cards",
                     "Risk Weighting","BRId","GenderId",
                     "IAId","Loyalty Classification",
                     "Properties Owned","Income Band"]]

for cols in categorical_cols:
    print(f"value_counts for {cols}:")
    print(df[cols].value_counts())

### PERFORMING EDA (EXPLORATORY DATA ANALYSIS)


# bivariate analysis

for i , predictor in enumerate(df[["Nationality","Occupation",
                                   "Fee Structure","Amount of Credit Cards",
                                   "Risk Weighting","BRId","GenderId","IAId",
                                   "Loyalty Classification","Properties Owned",
                                   "Income Band"]]):
    plt.figure(i)
    sns.countplot(data=df,x=predictor,hue="GenderId")
    plt.show()

# NUMERICAL ANALYSIS
#univariate analysis

numeric_cols=["Estimated Income","Superannuation Savings",
              "Bank Loans","Saving Accounts","Bank Deposits"]

plt.figure(figsize=(15,4))
for i, cols in enumerate(numeric_cols):
    plt.subplot(2,3,i+1)
    sns.histplot(df[cols],kde=True)
    plt.title(cols)
plt.show()

##PERFORMING HEATMAPS
numeric_cols=["Estimated Income","Superannuation Savings",
              "Bank Loans","Saving Accounts","Bank Deposits",
              "Amount of Credit Cards","Foreign Currency Account",
              "Checking Accounts","Business Lending"]


correlation_matrix=df[numeric_cols].corr()
plt.figure(figsize=(12,12))
sns.heatmap(correlation_matrix,annot=True,cmap="crest",fmt=".2f")
plt.title("correlation matrix")
plt.show()

'''
Based on the data, strong positive correlations
include Saving Accounts and Bank Deposits, and
Checking Accounts and Foreign Currency Accounts,
indicating that these financial behaviors often go hand-in-hand. 
Moderate positive correlations are seen between Estimated Income
and Superannuation Savings, and Estimated Income and Business Lending,
suggesting income influences both retirement planning and borrowing.
Weak correlations appear among most other variables, showing minimal
direct relationships and more independent financial patterns'''

## COMPLETION OF PYTHON LETS GO TO POWER BI DASHBOARD











