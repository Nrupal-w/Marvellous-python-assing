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


def tocsv():
    print(line)
    print("Conveted Into Csv")
    df.to_csv('Child.csv',index=False)
    print(line)

def main():
    
    tocsv()
    


if __name__=="__main__":
    main()