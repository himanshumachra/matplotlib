import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

dt = pd.read_csv('vk.csv')
plt.hist(dt["match_id"],bins=[20,50,60,80,90,100,130],log=True,label="virat",color="blue",rwidth=0.5)
plt.legend()
plt.show()
print(dt)