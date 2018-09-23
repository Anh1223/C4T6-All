from turtle import *
speed(0)
shape("turtle")
hideturtle()
left(90)
lv = 11
l  = 100
s  = 17
back(l)
forward(l)
def draw_tree(l, level):
    l = 3.0/4.0*l
    left(s)
    forward(l)
    level +=1
    if level<lv:
        draw_tree(l, level)
    back(l)
    right(2*s)
    forward(l)
    if level<=lv:
        draw_tree(l, level)
    back(l)
    left(s)
draw_tree(l, 2)
mainloop()