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


def histogram():
    print(line)
    print("Hisytogram of Maths Marks")
    plt.hist(df['Math'],bins=8,color='blue')
    plt.xlabel('students')
    plt.ylabel('Marks')
    plt.show()
    print(line)

def main():
    
    histogram()
    


if __name__=="__main__":
    main()