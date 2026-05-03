import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

bt = pd.read_csv('sharma-kohli.csv') 
plt.plot(bt['index'],bt['RG Sharma'],marker="o",markersize=4,linewidth=1.5,color='#FF00FF',label='virat')
plt.plot(bt['index'],bt['V Kohli'],label='sharma',marker='*',markersize=9,linewidth=1.5)
plt.title('ipl satta')
plt.xlabel('season')
plt.xlim(2008,2017.08)
plt.ylim(0,1500)
plt.legend()
plt.ylabel('runs')
plt.grid()
#print(bt)
plt.show()