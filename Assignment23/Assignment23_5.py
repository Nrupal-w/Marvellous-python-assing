import pandas as pd
import numpy as np
import matplotlib.pylab as plt
data={'Name': ['Amit', 'Sagar', 'Pooja'],

    'Math': [85, 90, 78],

    'Science': [92, 88, 80],

    'English': [75, 85, 82]}
    
df=pd.DataFrame(data)
line="_"*60


def replacename():
    global df
    print(line)
    print("Replaced Pooja with Puja")
    print(line)
    df['Name']=df['Name'].replace("Pooja","Puja")
    print(df)
    print(line)


def main():

    replacename()



if __name__=="__main__":
    main()