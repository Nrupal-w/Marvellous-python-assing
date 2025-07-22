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


def rename():
    global df
    print(line)
    df.rename(columns={'Math':'Mathematics'},inplace=True)
    print(df)
    print(line)

def main():
    
    rename()


if __name__=="__main__":
    main()