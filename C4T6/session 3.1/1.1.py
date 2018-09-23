from turtle import *
speed(0)
shape("turtle")
hideturtle()

for i in range(3):
    for y in range(4):
        forward(20+i*20)
        left(90)

mainloop()