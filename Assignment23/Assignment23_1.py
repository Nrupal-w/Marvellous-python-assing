import pandas as pd
import numpy as np
import matplotlib.pylab as plt
data={'Name': ['Amit', 'Sagar', 'Pooja'],

    'Math': [85, 90, 78],

    'Science': [92, 88, 80],

    'English': [75, 85, 82]}
    
df=pd.DataFrame(data)
line="_"*60

def dataframe():
    print(line)
    print("Basic Information")
    print(line)
    print(df.shape)
    print(df.dtypes)
    print(df.columns)
    print(line)




def main():
    dataframe()



if __name__=="__main__":
    main()