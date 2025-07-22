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
    print(line)
    df['Status']=df['Total'].apply(lambda x: "Pass" if x>250 else "Fail")
    print(df)
    print(line)
def Count():
    print(line)
    passcount=df[df['Status']=='Pass'].shape[0]
    print(passcount)
    print(line)

def main():
    
    AddCol()
    Count()
    


if __name__=="__main__":
    main()