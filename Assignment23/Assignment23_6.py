import pandas as pd
import numpy as np
import matplotlib.pylab as plt
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

def Sort():
    print(line)
    print("Sorted The Data Into Descending Oder")
    print(line)
    dfsorted=df.sort_values(by='Total',ascending=False)
    print(dfsorted)
    print(line)




def main():

    Newcolom()

    Sort()
    


if __name__=="__main__":
    main()