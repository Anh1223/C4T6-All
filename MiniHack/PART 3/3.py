print("Nhập 1 tháng")
so = int(input(">>>"))
for i in (1, 3, 5, 7, 8, 10, 12):
    if so == i:
        print("Ngu vãi")
        print("Ai chả biết tháng", i, "có 31 ngày")
for i in (4, 6, 9, 11):
    if so == i:
        print("Ngu vãi")
        print("Ai chả biết tháng", i, "có 30 ngày")
if so == 2:
    print("Tháng 2 có 28 hoặc 29 ngày")