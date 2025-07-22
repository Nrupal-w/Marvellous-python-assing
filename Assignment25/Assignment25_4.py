import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
df = pd.DataFrame(data)
encoder = OneHotEncoder(sparse_output=False)

encode = encoder.fit_transform(df[['Department']])
encodecol = encoder.get_feature_names_out(['Department'])
endf = pd.DataFrame(encode, columns=encodecol)
df = pd.concat([df, endf], axis=1)

print(df)
