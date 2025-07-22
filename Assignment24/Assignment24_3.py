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


def ADD():
    global df
    print(line)
    df['Gender']=['Male','Male','Female']
    print(df)
    print(line)
    encoder=OneHotEncoder(sparse_output=False)
    encoded=encoder.fit_transform(df[['Gender']])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['Gender']))

    df = pd.concat([df, encoded_df], axis=1)

    print(df)
    print(line)

def group():
    print(line)
    marksbygender=df.groupby('Gender')[['Math', 'Science', 'English']].mean()
    print(marksbygender)
    print(line)

def main():
    
    ADD()
    group()
   


if __name__=="__main__":
    main()