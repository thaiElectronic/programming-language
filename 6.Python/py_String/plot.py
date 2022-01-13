from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
ypoints = np.array([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1])

plt.plot(xpoints, ypoints)
plt.xlabel("Time(s)")
plt.ylabel("Don Vi($)")
plt.title("Bieu do gia tri gia tang")
plt.grid() #hiển thị đường lưới theo trục  y
#plt.grid(axis='x') #hiển thị đường lưới theo trục  x
#plt.grid()         #hiển thị đường lưới theo cả 2 trục 
#plt.scatter(xpoints ,ypoints, color = 'red')
plt.show()
