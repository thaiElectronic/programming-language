# Em: năng lượng ngắn hạn.

import numpy as np

data = np.array([-1.66000, -0.43700, -1.58700, -1.23100, -0.01900, -1.29500, 0.97900, -0.44200, -0.71700, 0.97200, 0.30000, -0.34400, -1.31100, -2.10000, 0.89500, 0.05000, 1.12800, 0.92700, 1.02400, -2.35100, 0.54100, 0.49900, 0.74400, 0.93100, 0.24900, -1.46300, -1.66400, -0.07700, 0.03300, -1.36900, 1.09100, -0.66100, -1.13700, 0.82600, 0.97800, 0.01700, -0.69000, 0.58100, -0.26800, -0.76500, -0.92900, 0.42300, -0.28300, -0.87500, -1.08000, -0.88700, -0.22200, 0.22300, 2.75900, 0.10000, -0.92900, 1.70000, -0.14300, -0.63300, -0.37300, 0.14800, -0.04000, 1.54400, 0.93200, -1.18400, 0.34200, 0.32300, 0.14600, 0.36100, 0.86000, 0.55800, -0.64700, 0.29100, 0.49700, -0.15900, 0.38500, 0.26200, 1.13200, 1.12200, 0.91500, -2.39200, 0.10100, -0.52900, 0.37600, 1.08600, 0.04800, 0.45100, 0.27300, 0.37500, 1.16800, 2.74600, 0.93000, -0.96200, -0.49700, -0.76400, -0.10500, 0.28100, -0.60000, 1.05300, 0.55000, -2.18700, -0.39200, -0.83900, 0.22700, 0.26300])

Wn = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
# N = 4
# Overlap = 50%
N = int(input("N = ")) # chiều dài khung phân tích
Overlap = int(input("overlap = "))

leng = len(data) # độ dài doạn tín hiệu ban đầu
check = (int)(N*Overlap/100) # tinh ra số phần tử cần lùi theo overlap
#print("Sô Si(n) = {0}".format(check))
temp = leng%(N-check) #
if temp != 0 : # nếu độ dài ban đầu của khung dữ liệu chia cho số độ dài khung phân tích trừ số phần từ cần lùi mà KQ ra lẻ
    frame = (leng//(N-check)) + 1 # check số khung dữ liệu được phân tích
else :
    frame = leng//(N-check)
print("count = {0}".format(temp))
add = N - temp #số phần tử 0 cần thêm vào cho chẵn doạn tín hiệu
#print("Số phần tử cần thêm: {0}".format(add))
for k in range(add):
    data = np.append(data,0) # thêm số 0 vào cuối đoạn tín hiệu
print(data) # in ra doạn tín hiệu mới
j = 0
k = N
checksum = 0
for i in range(frame):
    flash_data = data[j:k].copy()
    flash_Sn = flash_data*Wn
    print("S{0}(n): {1} => {2}".format(i,flash_Sn,np.sum(np.power(flash_Sn,2))))
    checksum += np.sum(np.power(flash_Sn,2))
    j = k-check
    k = k+(N-check)
print("S(n) = ",checksum)

