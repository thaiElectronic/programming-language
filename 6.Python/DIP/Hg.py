import numpy as np

data = np.array([
    [8,9,0,3,1,3],
    [2,5,0,7,9,1],
    [1,1,8,9,1,9],
    [0,5,7,5,8,5],
    [2,9,3,7,1,9],
    [2,4,0,9,8,3]
])
# Liệt kê các phần từ duy nhất trong mảng và số lần xuất hiện
counts = np.unique(data, return_counts=True)
print(counts)



# print("kich thuoc ma tran: {0}".format(data.shape))
# print("Gia tri: {0}".format(np.unique (data))) #in ra cac phan tu duy nhan trong mang

#    Liệt kê các phần từ duy nhất trong mảng và số lần xuất hiện
# counts = np.unique(data, return_counts=True)
# print(counts)




# x = int(input("x = "))
# y = np.searchsorted(data,x)
# print("Phan tu x: {0} => {1}".format(x,y))

