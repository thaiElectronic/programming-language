import numpy as np

data = np.array([
    [6,6,4,3,3,4],
    [8,3,1,6,4,8],
    [0,8,4,6,7,1],
    [9,3,7,0,6,2],
    [7,4,4,9,2,2],
    [2,7,3,2,7,6]
])

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)