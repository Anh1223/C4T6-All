r=int(input("How many color red?"))
b=int(input("How many color blue?"))
from turtle import *
speed(0)
width(6)
colormode(255)
penup()
left(180)
forward(750)
left(180)
pendown()
for i in range(20):
    for y in range(b):
        pendown()
        color("blue")
        forward(40)
        penup()
        forward(25)
    for I in range(r):
        pendown()
        color("red")
        forward(40)
        penup()
        forward(25)

mainloop()