import pandas as pd
import numpy as np
import matplotlib.pylab as plt
data={'Name': ['Amit', 'Sagar', 'Pooja'],

    'Math': [85, 90, 78],

    'Science': [92, 88, 80],

    'English': [75, 85, 82]}
    
df=pd.DataFrame(data)
line="_"*60


def Drop():
    global df
    df=df.drop('English',axis=1)
    print(df)



def main():

    Drop()


if __name__=="__main__":
    main()