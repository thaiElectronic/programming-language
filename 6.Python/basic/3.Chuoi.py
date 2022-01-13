
# thao tác thường sử dụng để tránh lỗi trùng với các kí tự đặc biệt \n, \a, \t..
# thêm 'r' ở trước chuỗi
# VD
# print(r"C:User\thaimcu\Desktop\Lab AI-photonics\STM32");
#**********************************************************************************

# cắt chuỗi: 
# C1: <Name>[vt1:vt2:bước nhảy]
# C2: <Namw>[vt1:vt2]
# bước nhảy > 0 -> trái qua phải
# bước nhảy < 0 -> phải qua trai
# vt1 = None -> vị trí sẽ ở đầu chuỗi
# vt2 = None -> vị trí sẽ ở cuối chuỗi
# str="Vu Thi Thu Ha"
# ptr=str[None:len(str)-3:-1]
# print(ptr)
#**********************************************************************************

# str = "Ho va ten: %s\nTuoi: %d\nQue Quan: %s" %("Do Van Thai",21,"Thuy Son - Thai Thuy - Thai Binh") 
# print(str)
#**********************************************************************************

# data = "$code,1024,1003,1022,1018,978"
# detext1 = data.split(',');
# detext2 = data.split(',',1);
# detext3 = data.split(',',2);
# print(detext1)
# print(detext2)
# print(detext3)
#**********************************************************************************

# data = "$code,1024,1003,1022,1018,978"
# check = data.count(",")
# check1 = data.count(",",0,15)
# print(check)
# print(check1)

data = "$code,1024,1003,1022,1018,978"
check = data.startswith("$code")
check1 = data.startswith("$code",5,15)
print(check)
print(check1)