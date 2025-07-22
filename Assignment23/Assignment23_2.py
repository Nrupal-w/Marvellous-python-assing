import pandas as pd
import numpy as np
import matplotlib.pylab as plt
data={'Name': ['Amit', 'Sagar', 'Pooja'],

    'Math': [85, 90, 78],

    'Science': [92, 88, 80],

    'English': [75, 85, 82]}
    
df=pd.DataFrame(data)
line="_"*60



def Descriptive():
    print(line)
    print("Descriptive Statistics")
    print(line)
    print(df.describe())
    print(line)




def main():

    Descriptive()
    


if __name__=="__main__":
    main()