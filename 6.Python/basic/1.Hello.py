# name = 'Donald Trump' # biến kiểu chuỗi
# age = 40 # biến kiểu số
# companies = ['Apple', 'Google', 'Microsoft'] # biến kiểu danh sách
# person_tuple = ('Trump', 'USA', 40, 'President') # biến kiểu tuple
# person_dict = {'Name': 'Trump', 'Age': 40, 'Job': 'US President'} # biến kiểu từ điển
# print(name)
# print(age)
# print(companies)
# print(person_tuple)
# print(person_dict)

################################################################
#giải phương trình bặc 2.
# from math import sqrt # sử dụng hàm tính căn sqrt trong module math

# print('--- EQUATION SOLVER ---')

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))

# d = b*b - 4*a*c

# if {d >= 0}:
#     print('THERE ARE REAL SOLUTIONS:')
#     x1 = (-b + sqrt(d))/(2*a)
#     x2 = (-b - sqrt(d))/(2*a)
#     print(f'x1 = {x1}')
#     print(f'x2 = {x2}')
# else:
#     print('THERE ARE COMPLEX SOLUTIONS BUT I CANNOT SHOW YOU.')

# input('\nThank you! Press enter to quit ...')
################################################################

# age = int(input("Your age: "))
# gender = input("Gender (male/female): ")
# name = input("Your name: ")

# if(age >= 18):
#     print('Your age a legal.')
#     if(name.isalpha()):
#         if(gender.lower() == "male"):
#             print(f'Welcome, Mr. {name}!')
#         elif(gender.lower() == "female"):
#             print(f'Welcome, lady {name}!')
#         else:
#             print(f'Welcome, {name}')
#     else:
#         print('Sorry, who are you?')
# else:
#     print('You are too young to come here!')

# print("Hello world!")

print("Nhap ten cua ban: ")
str = input();
print("Chu Hoa: ",str.upper())
print("chu thuong: ",str.lower())

# str="$code,123,234,464,ON,1034,OFF"
# print(str.split(','))

# a = input("nhap a: ");
# b = input("nhap b: ");
# if{a>b}: print("Max: ",a)
# else: print("Max: ",b)