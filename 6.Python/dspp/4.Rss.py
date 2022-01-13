# Rxy(n) = Rxx(n){tự tương quan} <=> Rss(n): Tương quan ngắn hạn
#
import numpy as np

data = np.array([1,0.5,0.25,1,0.5,0.25,1,0.5,0.25]) # Đoạn tín hiệu
leng = len(data)
deta  = 0 # giá trị Deta
checksum = 0 # Tông của các Rss(x) vs x = [0,N-1]
for i in range(leng-deta):
    data1 = data[0:leng-i].copy() # mảng tín hiệu mới Sm(k) sau mỗi lần tăng giá trị của Deta(số lượng phần tử giảm đi i)
    temp = data[i:leng].copy()  # mảng tín của Sm(k+Deta)
    result = data1*temp
    # print(data1)
    # print(temp)
    # print("KQ: ",np.add.reduce(result),"\n" )
    print("Deta: {0} =>Rss({1}): {2} => Sum = {3}".format(deta,deta,result,np.add.reduce(result)))
    checksum = checksum + np.add.reduce(result) 
    deta+=1
print("Rss(n): ",checksum)