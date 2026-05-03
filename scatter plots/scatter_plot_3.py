import matplotlib.pyplot as plt
import seaborn as sas 
import random as rd 
import pandas as pd 

dt = pd.read_csv('batter.csv')
plt.plot(dt['runs'],dt['avg'],'o',s=dt[strike_rate])
plt.xlabel('runs')
plt.ylabel('avg')
plt.title('runs and avg of the players')
plt.show()

#this one is more faster we have less options to manuplate it with liek some function as colors and size as the 3 info teller like runs stick on x,y and the size of the dot depends on the 3rd column
# this one have the high speed in comparizen of the scatter