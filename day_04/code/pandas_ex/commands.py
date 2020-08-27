import pandas as pd
df = pd.read_csv("student.csv")

df.head()
df.tail()
df.columns

df['name']
df[['name', 'regid', 'avg']]
df['newcol'] = df['phy'] + df['chem'] + df['bio'] + df['math']


df.loc(0)
df.iloc(0)
df.iloc[[7,1,2,3]]

df.drop('newcol', axis=1, inplace=True)
df.drop([2,3,4])

df['newcol'] = df[['phy', 'chem', 'math', 'bio']].mean(axis=1)
df['avg'] = df[['phy', 'chem', 'math', 'bio']].mean(axis=1)

df['rank'] = df['avg'].rank()
df['rank'] = df['avg'].rank(method='dense', ascending=False)

import matplotlib.pyplot as plt
plt.bar(df['regid'], df['avg'], color='m')
plt.show()

with pd.ExcelWriter('report.xlsx') as writer:
    df.to_excel(writer)
