import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('911-a.csv')
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
fig,ax = plt.subplots(figsize = (15,7))
grouped = df.groupby(['month','problem'])['timeStamp'].count().unstack().plot(kind='bar')
print(grouped)
plt.show()
