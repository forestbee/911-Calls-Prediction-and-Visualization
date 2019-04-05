import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('911-a.csv')
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
fig,ax = plt.subplots(figsize = (14,8))
grouped = df.groupby(['month','problem'])['timeStamp'].count().unstack()
grouped.plot.area()
plt.show()
