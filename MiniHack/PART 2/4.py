from turtle import *
speed(0)

print("Số cạnh của đa giác đều")
socanh = int(input(">>>"))
sogoc = 360 / socanh
for i in range(socanh):
    forward(150)
    left(sogoc)
mainloop()