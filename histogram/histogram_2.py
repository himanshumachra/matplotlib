import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

dt = np.load('big-array.npy')
plt.hist(dt,rwidth=0.5,log=True)
plt.show()