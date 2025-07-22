import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}

df=pd.DataFrame(data)
lable=LabelEncoder()
print("Befor Lable encoding")
print(df)
print("After Lable encoding ")
df['Encoded codes']=lable.fit_transform(df)
print(df)
