from turtle import *
speed(0)
print("Nhập bán kính hình tròn bạn cần vẽ")
bankinh = float(input(">>>"))

forward(bankinh)
left(90)
for i in range(900):
    forward(bankinh/5.599999)
    left(10)

mainloop()