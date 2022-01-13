#     -- Read File
# f = open("linetext.txt","r")
# print(f.read())
# f.close()

#     -- Write File
f = open("./fileText/WriteFile.txt","w")
f.write("Con tim em thay long, de niem dau thay bao man nong, buoc chan anh di ve chang con ai mong")
f.close()
f = open("./fileText/WriteFile.txt","r")
print(f.read())
f.close()