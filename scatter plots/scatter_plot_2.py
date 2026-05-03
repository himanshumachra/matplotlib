import matplotlib.pyplot as plt
import seaborn as sas 
import random as rd 
import pandas as pd 

dt = pd.read_csv('batter.csv')
plt.scatter(dt['strike_rate'],dt['avg'],color='black',marker='o',s = dt['runs']/10,label='players')
plt.xlabel('strike rate')
plt.ylabel('average runs')
plt.title('avg player buying info')
plt.legend(loc='upper left')
plt.grid()
plt.show()

# we can use the function like marker and s and color and label all in it but be clear 
# some of them are not proiperly working in the same formte like they are working but there syntax might be different 
# here like the markersize in plot and here we having s parameter