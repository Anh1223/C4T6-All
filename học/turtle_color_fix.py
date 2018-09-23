color1='red'
color2='blue'
color3='purple'
color4='orange'
color5='light blue'
color6='teal'
from turtle import*
shape("turtle")
hideturtle()
penup()
goto(-600, 0)
for c in [color1,color2,color3,color4,color5,color6]:
    fillcolor(c)
    stamp()
    forward(200)

mainloop()