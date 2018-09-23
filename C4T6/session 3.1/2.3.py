from turtle import *
speed(0)
shape("turtle")
hideturtle()
colormode(255)
for i in range(10):
    color(255-20*i,123-10*i,56-4*i)
    begin_fill()
    for y in range(4):
        forward(200-i*15)
        left(90)
    end_fill()
    left(30)
mainloop()