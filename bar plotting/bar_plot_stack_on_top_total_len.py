import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sas

dt = pd.read_csv('batsman_season_record.csv')
print(dt)

plt.bar(dt['batsman'],dt['2017'],width=0.4,color='green',label="2017")
plt.bar(dt['batsman'],dt['2016'],width=0.4,color='red',label="2016",bottom=dt['2017'])
plt.bar(dt['batsman'],dt['2015'],width=0.4,color='black',label="2015",bottom=(dt['2017']+dt['2016']))
plt.legend()
plt.show()