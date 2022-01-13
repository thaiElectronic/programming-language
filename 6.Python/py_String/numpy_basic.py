import numpy as np
from numpy import power, ptp

y = np.array([1,2,3])
# x = mt.sqrt((y-1)/2)
print("Tổng các phần tử: {0}".format(np.sum(y)))
print("Tổng các phần tử: {0}".format(np.add.reduce(y)))
print("Tổng các phần tử bình phương: {0}".format(np.sum(np.power(y,2))))

# for x in np.nditer(y)
