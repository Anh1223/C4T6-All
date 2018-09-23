from turtle import *
speed(0)
shape("turtle")
colormode(255)
hideturtle()
for i in range(5):
    begin_fill()
    for y in range(4):
        color(0,210-i*25,0)
        forward(140-i*20)
        left(90)
    end_fill()
mainloop()