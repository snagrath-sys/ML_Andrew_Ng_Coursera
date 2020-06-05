import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

db=pd.read_csv("ex1data1.txt")
df=np.array(db)
#print(db.head())
x=df[:,0];
y=df[:,1]
#db.head()
plt.scatter(x,y)
plt.show()
