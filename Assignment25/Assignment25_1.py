import pandas as pd 
import numpy as np


data ={'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
df=pd.DataFrame(data)

q1=df['Salary'].quantile(0.25)
q3=df['Salary'].quantile(0.75)

IQR=q3-q1

lowerval=q1-1.5*IQR
upperval=q3+1.5*IQR

filtered=df[(df['Salary']>=lowerval) & (df['Salary']<=upperval)]
outliers = df[~((df['Salary']>=lowerval) & (df['Salary']<=upperval))]

print("Orignal data")
print(df)
print("Filter data")
print(filtered)
print("Outlier data is ")
print(outliers)
