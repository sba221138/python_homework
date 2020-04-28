import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,9,1)

Data1 = [1,4,9,16,25,36,49,64]
Data2 = [1,2,3,6,9,15,24,39]

plt.figure(figsize = (6,4) ,facecolor = "lightgreen")

plt.xlim(0,8)
plt.ylim(0,70)

plt.plot(x,Data1,'b.',x,Data2,'r.')
plt.plot(x,Data1,'b--',x,Data2,'r--')

plt.title("Figure",size = '26')
plt.xlabel("x-Value", size = '16')
plt.ylabel("y-Value", size = '16')

plt.show()
