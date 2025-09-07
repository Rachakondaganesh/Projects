## MINI PROJECT REPORT ON EV VECHILE

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


link="C:/Users/user/Downloads/archive.zip"
df=pd.read_csv(link)
print(df)
print(df.shape)
print(df.columns)
print(df.info)
data=df.describe()
e1=df["Monthly_Charging_Cost_USD"].max()
e2=df["Monthly_Charging_Cost_USD"].min()
print("The minimum monthly cost for charging =",e2)
print("The maximum monthly cost for charging =",e1)

# o/p = min 7.99 dollars
# o/p = max 1643 dolLars

# resale value which is best
e3=df["Resale_Value_USD"].min()
e4=df["Resale_Value_USD"].max()
print("minimum resale value=",e3) # 8506 dollars
print("maximum resale value=",e4) # 35521 dollars
# NOW I MAKE THIS AS LOW MED HIGH

bins=[0,15000,30000,float("inf")]
label=["LOW","MEDIUM","HIGH"]
df["RESALE_VALUE"]=pd.cut(df["Resale_Value_USD"],bins=bins,labels=label,right=False)
resale_value=df["RESALE_VALUE"].value_counts().plot(kind="bar")
print(resale_value)
plt.show()

##PERFORMING EDA EXPLORATORY DATA ANALYSIS

for i,predictor in enumerate(df[['Vehicle_ID', 'Make', 'Model', 'Year', 'Region', 'Vehicle_Type',]]):
    plt.figure(i)
    sns.countplot(data=df,x=predictor,color="red")
    plt.show()

sns.barplot(data=df,x="Vehicle_Type",y="Range_km",color="yellow")
plt.show()

sns.barplot(data=df,x="Make",y="Resale_Value_USD",color="yellow")
plt.show()




