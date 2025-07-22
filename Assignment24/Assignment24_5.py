import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
import seaborn as sns

data={'Name': ['Amit', 'Sagar', 'Pooja'],

    'Math': [85, 90, 78],

    'Science': [92, 88, 80],

    'English': [75, 85, 82]}
    
df=pd.DataFrame(data)
line="_"*60


def Newcolom():
    print(line)
    print("Add New Colum Total")
    print(line)
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    print(df)
    print(line)

def AddCol():
    global df

    df['Status']=df['Total'].apply(lambda x: "Pass" if x>250 else "Fail")
    print(df)

def main():

    AddCol()



if __name__=="__main__":
    main()