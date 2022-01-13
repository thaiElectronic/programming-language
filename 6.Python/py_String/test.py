# a = 21
# print("-"*20)
# print("tuoi cua ban: {0}".format(a))
# print("tuoi cua ban: ",a)

# dtb = float(input("diem trung binh cua ban: "))
# if dtb >= 9:
#     print("hoc sinh gioi")
# elif dtb > 7:
#     print("hoc sinh kha")
# elif dtb > 5: 
#     print("hoc sinh trung binh")
# else:
#     print("hoc sinh kem")

# b = int(input("nhap b:"))
# print("chan" if b % 2 ==0 else "le")
# print("do van thai")

# from math import *
# b = 24
# print(round(sqrt(b),4))


# import time 
# print("nhap ten cua ban: ")
# start_time = time.time()
# text = input("ten cua ban: ")
# end_time = time.time()
# sum_time = end_time - start_time
# print("thoi gian chay chuong trinh: {0}".format(round(sum_time,3)))

##########################################################################

# # Em: năng lượng ngắn hạn.
# import numpy as np
# import math 

# N = int(input("chiều dài khung phân tích = "))
# Overlap = int(input("overlap = "));
# data = np.array([1,2,-1,2,-1,-2,-1,1])
# #data = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
# leng = len(data) # số phần từ trong mảng
# check = (int)(N*Overlap/100) # tinh ra số phần tử cần lùi theo overlap
# print("Sô Si(n) = {0}".format(check))

# count = leng%(N-check) # 
# if count != 0:
#     conter = (leng//(N-check)) + 1 # check số khung dữ liệu được phân tích
# else :
#     conter = leng//(N-check)
# print("count = {0}".format(count))
# add = N - count #số phần tử 0 cần thêm vào cho chẵn khung dữ liệu
# print("Số phần tử cần thêm: {0}".format(add))
# for k in range(add):
#     data = np.append(data,0)
# print(data)
# j = 0
# k = N
# for i in range(conter):
#     print("S{0}(n)): {1} => {2}".format(i,data[j:k],np.sum(np.power(data[j:k],2))))
#     j = k-check
#     k = k+(N-check)

##########################################################################
# ZCR: Tốc độ trổ kháng về 0 
#(hai mẫu tín hiệu cạnh nhau có dáu khác nhau)

# import numpy as np

# #data = np.array([1,2,-1,2,-1,-2,-1,1,2])
# data = np.array([1,0.5,-1,-0.5,1,0.5,-1,-0.5,1,0.5,-1,-0.5])
# N = int(input("N = ")) # chiều dài khung phân tích
# Overlap = int(input("overlap = "))

# leng = len(data) # độ dài doạn tín hiệu ban đầu
# check = (int)(N*Overlap/100) # tinh ra số phần tử cần lùi theo overlap
# temp = leng%(N-check) #
# if temp != 0 : # nếu độ dài ban đầu của khung dữ liệu chia cho số độ dài khung phân tích trừ số phần từ cần lùi mà KQ ra lẻ
#     frame = (leng//(N-check)) + 1 # check số khung dữ liệu được phân tích
# else :
#     frame = leng//(N-check)
# print("count = {0}".format(temp))
# add = N - temp #số phần tử 0 cần thêm vào cho chẵn doạn tín hiệu
# for k in range(add):
#     data = np.append(data,0) # thêm số 0 vào cuối đoạn tín hiệu
# print(data) # in ra doạn tín hiệu mới
# j = 0
# k = N
# counter = 0
# for i in range(frame):
#     x = data[j:k].copy()
#     for m in range(len(x)-1):
#         if x[m]>0 and x[m+1]<0:
#             counter += 1
#         elif x[m]<0 and x[m+1]>0:
#             counter += 1 
#     print("=>S{0}(n)): {1} => ZCR({2}) = {3}".format(i,x,i,counter))
#     counter = 0
#     j = k-check
#     k = k+(N-check)
    
import numpy as np
import math as mt
c = 0
data = np.array([-1,2,1,-2,1])
checksum = 0
for k in range(4):
    print("S({0}): {1}".format(k,data[k]))
    for n in range(4):
        #c = data[n]*(mt.cos(-(2*mt.pi*k*n)/4) + mt.sin(-(2*mt.pi*k*n)/4))
        c = complex(data[n]*mt.cos(-(2*mt.pi*k*n)/4), data[n]*mt.sin(-(2*mt.pi*k*n)/4))
        checksum += c
        print("K = {0}: S({1}): {2}".format(k,k,c))
    print("Result: {0}".format(round(checksum,2)))
    checksum = 0
    print("\n")

# import math as mt

# from numpy import power

# a = 3+4j
# print(mt.sqrt(power(a.real,2)+power(a.imag,2)))