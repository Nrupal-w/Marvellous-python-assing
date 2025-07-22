import pandas as pd
import numpy as np
import matplotlib.pylab as plt
data={'Name': ['Amit', 'Sagar', 'Pooja'],

    'Math': [85, 90, 78],

    'Science': [92, 88, 80],

    'English': [75, 85, 82]}
    
df=pd.DataFrame(data)
line="_"*60


def Linechart():
    print(line)
    print("Line Chart Of Makrs For amit Across All Subjects")
    print(line)
    amitdf=df[df['Name']=='Amit'].iloc[0]
    sub=['Math', 'Science', 'English']
    score=[amitdf['Math'],amitdf['Science'],amitdf['English']]
    plt.figure(figsize=(8,10))
    plt.plot(sub,score,color='Blue',marker="*")
    plt.xlabel("Amit")
    plt.ylabel("All Subjects")

    plt.title("Amit All Subject Graph")
    plt.show()
    print(line)




def main():

    Linechart()



if __name__=="__main__":
    main()