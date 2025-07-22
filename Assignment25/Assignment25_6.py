import pandas as pd


data={'Grade': ['A+', 'B', 'A', 'C', 'B+']}
df=pd.DataFrame(data)
print("Orignal DataFrame")
print(df)
rep = {
    'A+': 'Excellent',
    'A': 'Very Good',
    'B+': 'Good',
    'B': 'Average',
    'C': 'Poor'}

df['Grade']=df['Grade'].replace(rep)
print("After Replacemnet")
print(df)