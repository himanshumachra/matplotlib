import matplotlib.pyplot as plt
import seaborn as sas 
import random
import pandas as pd
x= random.sample(range(34,100),14)
y = random.sample(range(1,24), 14)
plt.scatter(x,y,color='red',marker='*')
plt.title(" time studied and marks got")
plt.xlabel("marks")
plt.ylabel("hours study") 
print(x);print(y)
plt.show()

# this one is the basic idea about the scatter ploting like howe it basically works and all 