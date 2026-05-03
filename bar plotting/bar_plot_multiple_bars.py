import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sas
import numpy as np

dt = pd.read_csv('batsman_season_record.csv')
w=0.2
# we use arrary on plae of batsman`s name to calculkate the distace from the batsman1 and batsman2 pointing graph position like where it placed and when we got to know
# the spcae or the position we subtact the width to move the first pole to left side because the position is in the certer just to fit 3 pole we shift pol_1 at 0.8and pole _2 
# at 1 and pole 3 at 1.2 means 1 -width =pole1 | 1 =pole 2 | 1 + width =pole3


m = np.arange(len(dt['batsman'])) 
plt.bar(m - w,dt['2015'],width=w,color='blue',label="2015")
plt.bar(m,dt['2016'],width=w,color='orange',label="2016")
plt.bar(m + w,dt['2017'],width=w,color='green',label="2017")
plt.xticks(m , dt['batsman'])# without it the batsmans name now sahown properly


# if we have a larger names on the x or y axes and they are mearjing in to each others data or names sop we use a parameter as 
#rotation in the xticks rotation = "vertical"
plt.xticks(rotation = "vertical")

plt.legend()
plt.show()