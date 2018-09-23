from turtle import *
shape("turtle")

colormode(255)
width(10)
speed(0)
for i in range(100):
    forward(10+5*i)
    left(90)
    color((2*i)%255,(3*i)%255,(4*i) % 255)
mainloop()