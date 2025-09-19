
# SUPERSTORE SALES DATA ANALYSIS PROJECT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

link="C:/Users/user/Downloads/Superstore_Excel.xlsx"
df=pd.read_excel(link)
print(df)
print("shape of the data ",df.shape)
print(df.columns) # printing all columns in data set
print(df.describe()) # descriptive statistics
print("mising values in the cols")
print(df.isnull().sum()) # here you can see any null values are present in cols
# in our case there is no null values
row_null=df[df.isnull().any(axis=1)] # here you can see any null values are present in rows
print(row_null)
dropmis=df.dropna(inplace=True)
print(dropmis)
#we can also perform removing duplicates
remove_dupl=df.drop_duplicates()

#for_al=df.fillna().mean()# for all null vals replace
#df["profit"].fillna(df["profit"].mean(),inplace=True) # to remove null values with mean for cols
# we commented the above null values remove syntax. because we don't have null values

# now we will perform EDA (EXPLORATORY DATA ANALYSIS)

sns.barplot(df,x="Segment",y="Profit",hue="Category",color="blue")
plt.title("PROFIT BASED ON CATEGORY AND SEGMENT")
plt.show()

# we perform some more
sns.barplot(df,x="Region",y="Profit",color="blue")
plt.title("region wise profit")
plt.show()
sns.barplot(df,x="Region",y="Sales",color="blue")
plt.title("region wise sales")
plt.show()
sns.barplot(df,x="Segment",y="Sales",color="blue")
plt.title("segment wise sales")
plt.show()
sns.scatterplot(df,x="State",y="Profit",color="blue")
plt.title("state wise profit")
plt.show()


# convert dates and extract time features
'''
df["Order Date"]=pd.to_datetime(["Order Date"])
df["Month"]= df["Order Date"].dt.month
df["Year"]=df["Order Date"].dt.year
'''
## TOP 10 BEST SELLING PRODUCTS
top_products=df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
print("TOP SELLING PRODUCTS \n",top_products.head(10))
## TOP 10 BEST SELLING SUB CATEGORY PRODUCTS
top_sub_category=df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
print("TOP SELLING SUB_CATEGORY PRODUCTS \n",top_sub_category.head(10))

# NOW WE PERFORM EDA ON TOP SELLING PRODUCTS

plt.figure(figsize=(10,10))
sns.barplot(x=top_products.head(10).values,y=top_products.head(10).index)
plt.title("TOP SELLING PRODUCTS")
plt.xlabel("total sales")
plt.ylabel("product")
plt.show()

# Same like category products also

plt.figure(figsize=(10,10))
sns.barplot(x=top_sub_category.head(10).values,y=top_sub_category.head(10).index)
plt.title("TOP BEST SELLING SUB CATEGORY PRODUCTS")
plt.xlabel("total sales")
plt.ylabel("sub category products")
plt.show()

## we are done with python CLEANING AND EDA lets move on to;
# POWER BI DASHBOARD


