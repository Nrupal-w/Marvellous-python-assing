import pandas as pd
import numpy as np

data = {'Marks': [85, np.nan, 90, np.nan, 95]}
df=pd.DataFrame(data)
print("Befor Interpolation")
print(df)
df['Filled missing data']=df['Marks'].interpolate(method='linear')

print("After Interpolation")
print(df)

