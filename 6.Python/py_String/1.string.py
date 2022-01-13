#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# upper,lower       : xử lý in hoa, in thường
# rjust             : căn lề phải 
# ljust             : căn lề trái
# center            : căn giữa
# strip             : xóa khoảng trắng dư thừa
# startswith        : kiểm tra chuỗi có phải bắt đầu là kí tự 
# endswith          : kiểm tra chuỗi có phải kết thúc là kí tự
# count             : điểm số lần xuất hiện trong chuỗi
# find              : tìm kiếm chuỗi con 
# format            : định dạng chuỗi 
# len               : trả về số lượng kí tự trong chuỗi
# split,splitlines  : tách chuỗi
# join              : nối chuỗi


# print("Input: ")
# fullname = input("Full Name: ")
# age = int(input("Age: "))
# studentcode = input("Student Code: ")
# print("Information: ")
# print("Full Name   : " + fullname.lower())
# print("Age         : " + format(age))
# print("Student Code: " + studentcode.lower())

# acc = input("User: ")
# pas = input("PassWord: ")
# print("Thong tin tai khoan: \n" + acc + "\n" + pas)

# if acc == "B18DCDT230" and pas == "22052000":
#     print("Dang nhap thanh cong")
# else: print("Dang nhap that bai")

############ substring ##############
# data = "192.168.255.255"
# print(data[:5]) # từ kí tụ đầu tiền đến kí tự thứ 5
# print(data[5:]) # từ kí tự thứ 5 đến kí tự cuối cùng.

############ split,splitlines - tách chuỗi ##############
# data = "$code,1024,1022,1000,978,1023,0,1,0*0x23"
# arr = data.split('$code,')
# for x in arr:
#     print(x)

# information = """do van thai
# hoc vien cong nghe buu chinh vien thong
# thuy son, thai thuy, thai binh"""
# check = information.splitlines()
# for line in check:
#     print(line,"a->",line.count("a"))

# student = """Do Van Thai;22/05/2000;B18DCDT230;D18CQDT02
# Vu Thi Thu Ha;06/07/2000;B18DCAT067;D18CQAT03
# Tran Ngoc Khiem;17/11/2000;B18DCDT115;D18CQDT03"""

# std = student.splitlines()
# print(len(std))
# for x in std:
#     arr = x.split(';')
#     if len(arr)==4:
#         print(x)
###################################################################
import math as mt

from numpy.lib.type_check import imag

a = 4
b = 3+4j
c = a*b
tf = 25*mt.e-4
print(abs(b))