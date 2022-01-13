# for i in range(4):
#     print("a[%d] = %d",i,i)

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

import numpy as np

#x = np.array([1.301, 0.416, -0.715, -0.656, 1.301, 0.416])2
#x = np.array([1.301, 0.416, -0.715, -0.656,	1.301,	0.416,	-0.715,	-0.656,	1.301,	0.416,	-0.715,	-0.656,	1.301,	0.416,	-0.715,	-0.656])
#x = np.array([-0.656,	1.301,	0.416,	-0.715,	-0.656,	1.301])3
x = np.array([-0.715,	-0.656,	1.301,	0.416,	-0.715,	-0.656])
zcr1 = 0
for i in np.nditer(x):
    if(i > 0 and i+1 < 0):
        zcr1+=1
    elif(i < 0 and i+1 > 0):
        zcr1+=1
print(zcr1)


