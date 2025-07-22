import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data= {'Age': [18, 22, 25, 30, 35]}
df=pd.DataFrame(data)
scaler=MinMaxScaler()
df["AgeNorm"]=scaler.fit_transform(df[['Age']])

print("Data after saclling")
print(df)
