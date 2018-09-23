from turtle import *
color("blue")
shape("turtle")
penup()
for i in range(5, 60, 2):
    stamp()
    forward(i)
    right(24)

mainloop()