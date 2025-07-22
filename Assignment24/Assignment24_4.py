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


def Pie():
    global df

    sagerdata=df[df['Name'] == 'Sagar'].iloc[0]
    subjdata=['Math',"Science","English"]
    sagerscore = sagerdata[subjdata].values
    lables=subjdata
    plt.figure(figsize=(8,10))
    plt.pie(sagerscore,labels=lables,colors=["#A91037","#0F3DD5","#0ABC1C"],autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Distribution of Sagar's Marks Across Subjects")
    plt.show()
    print(line)
    print("Pie Plot for Sagar's Marks Generated.")

def main():
    
    Pie()
   


if __name__=="__main__":
    main()