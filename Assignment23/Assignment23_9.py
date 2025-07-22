import pandas as pd
import numpy as np

data2 = {
'Name': ['Amit', 'Sagar', 'Pooja'],

'Math': [np.nan, 76, 88],

'Science': [91, np.nan, 85]
}
df=pd.DataFrame(data2)
line="_"*60


def Mean():
    df[['Name','Math','Science']]=df[['Name','Math','Science']].fillna(df.mean(numeric_only=True))
    print(df)

def main():
    Mean()
    

if __name__=="__main__":
    main()