print("nhập danh sách")
danhsach = input(">>>")
danhsach_list = danhsach.split(",")
for i in danhsach_list:
    print(i.title())
