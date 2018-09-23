from turtle import *
speed(0)

print("Nạp các màu")
mau = input(">>>")
mau = mau.split(",")

for i in mau:
    color(i)
    forward(30)

mainloop()