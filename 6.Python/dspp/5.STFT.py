import math as mt
import numpy as np

data = np.array([1,0.5,-1,2,1,-2,1,-2,-0.5,1])
l = int(input("N = ")) # chiều dài khung phân tích
Overlap = int(input("overlap = "))

leng = len(data) # độ dài doạn tín hiệu ban đầu
check = (int)(l*Overlap/100) # tinh ra số phần tử cần lùi theo overlap
temp = leng%(l-check) #
if temp != 0 : # nếu độ dài ban đầu của khung dữ liệu chia cho số độ dài khung phân tích trừ số phần từ cần lùi mà KQ ra lẻ
    frame = (leng//(l-check)) + 1 # check số khung dữ liệu được phân tích
else :
    frame = leng//(l-check)
print("count = {0}".format(temp))
add = l - temp #số phần tử 0 cần thêm vào cho chẵn doạn tín hiệu
for k in range(add):
    data = np.append(data,0) # thêm số 0 vào cuối đoạn tín hiệu
print("S(n): ",data) # in ra doạn tín hiệu mới
j = 0
m = l
checksum = 0
c = 0
for i in range(frame):
    data_temp = data[j:m].copy()
    print("S({0}): {1}".format(i,data_temp))
    for k in range(l):
        for n in range(l):
            c = complex(round(data[n]*mt.cos(-(2*mt.pi*k*n)/l),2), round(data[n]*mt.sin(-(2*mt.pi*k*n)/l),2))   
            checksum += c  
        print("k = {0}: S({1}) = {2} => |S({3})| = {4}".format(k,i,checksum,i,abs(checksum)))
        checksum = 0
        c = 0
    j = m-check
    m = m+(l-check)
