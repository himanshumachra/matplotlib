import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sas
bt = pd.read_csv("sharma-kohli.csv")
plt.plot(bt['index'],bt['V Kohli'],color='grey',linewidth=2,marker='o',markersize=5,label='viratcbvxxcbxcv')
plt.plot(bt['index'],bt['RG Sharma'],color='red',linewidth=2,marker='*',markersize=5,label='sharma')
plt.xlabel('season')
plt.ylabel('RUNS')
plt.title('virat vs sharma')
plt.xlim(2008,2018)
plt.ylim(150,976)
print(bt)
plt.grid()
plt.legend()
plt.show()