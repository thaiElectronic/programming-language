import numpy as np

data = np.array([
                [6,6,4,3,3,4],
                [8,3,1,6,4,8],
                [0,8,4,6,7,1],
                [9,3,7,0,6,2],
                [7,4,4,9,2,2],
                [2,7,3,2,7,6]
                ])
m = int(input("m = "))
n = int(input("n = "))
print("toa do giua: {0}_{1}".format(m//2+1,n//2+1))
# print("data: {0}". format(data[0,0]))

x = int(input("x = "))
y = int(input("y = "))
if data[x,y] == data[0,0]:
    print("output: ",data[x,y])


