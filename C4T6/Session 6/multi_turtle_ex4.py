from turtle import *
speed(0)
turtle_list = []
for _ in range(9):
    turtle_list.append(Turtle())

# def cautraloi_cmdfalse():
#     print("What?")
#     print("I don't can read")
#     print("Please re-enter cmd")
#     cmd = input("What command (fd + độ dài cần đi, bd + độ dài cần đi, lt + số đo góc, rt + số đo góc)")
#     cmd = cmd.lower()
#     cmd_list = cmd.split(" ")
#     for c in cmd_list:
#         if c == "fd":
#             turtlelist.forward(int(cmd_list[cmd_list.index(c) + 1]))
#         elif c == "bd":
#             turtlelist.backward(int(cmd_list[cmd_list.index(c) + 1]))
#         elif c == "lt":
#             turtlelist.left(int(cmd_list[cmd_list.index(c) + 1]))
#         elif c == "rt":
#             turtlelist.right(int(cmd_list[cmd_list.index(c) + 1]))
#         else:
#             cautraloi_cmdfalse()

def kiemcautraloi_turtlecandieukhienfalseortrue():
    if tp > 9:
        print("You can only choose one of the 9 turtles, ranked in order of 1 to 9")
        print("Please enter the serial number of the turtle to control")
        cautraloi_turtlecandieukhienfalse2()
    if tp < 1:
        print("You can only choose one of the 9 turtles, ranked in order of 1 to 9")
        print("Please enter the serial number of the turtle to control")
        cautraloi_turtlecandieukhienfalse2()

def cautraloi_turtlecandieukhienfalse2():
    tp = int(input("Which one do you want to control?"))
    if tp > 9:
        print("You can only choose one of the 9 turtles, ranked in order of 1 to 9")
        print("Please enter the serial number of the turtle to control")
        cautraloi_turtlecandieukhienfalse2()
    if tp < 1:
        print("You can only choose one of the 9 turtles, ranked in order of 1 to 9")
        print("Please enter the serial number of the turtle to control")
        cautraloi_turtlecandieukhienfalse2()
    else:
        turtlelist = turtle_list[tp - 1]
        turtlelist.color(input("What color?"))
        cmd = input("What command (fd + độ dài cần đi, bd + độ dài cần đi, lt + số đo góc, rt + số đo góc)")
        cmd = cmd.lower()
        cmd_list = cmd.split(" ")
        for c in cmd_list:
            if c == "fd":
                turtlelist.forward(int(cmd_list[cmd_list.index(c) + 1]))
            elif c == "bd":
                turtlelist.backward(int(cmd_list[cmd_list.index(c) + 1]))
            elif c == "lt":
                turtlelist.left(int(cmd_list[cmd_list.index(c) + 1]))
            elif c == "rt":
                turtlelist.right(int(cmd_list[cmd_list.index(c) + 1]))
            # else:
            #     cautraloi_cmdfalse()

def color_commad(tp) :
    turtlelist = turtle_list[tp - 1]
    colororcmd = input("Color or Command or Color Command")
    colororcmd = colororcmd.lower()
    colororcmd_list = colororcmd.split(" ")
    for _ in colororcmd_list :
        if _ == "color" :
            turtlelist.color(input("What color?"))
        elif _ == "command" :
            cmd = input("What command (fd + độ dài cần đi, bd + độ dài cần đi, lt + số đo góc, rt + số đo góc)")
            cmd = cmd.lower()
            cmd_list = cmd.split(" ")
            for c in cmd_list:
                if c == "fd":
                    turtlelist.forward(int(cmd_list[cmd_list.index(c) + 1]))
                elif c == "bd":
                    turtlelist.backward(int(cmd_list[cmd_list.index(c) + 1]))
                elif c == "lt":
                    turtlelist.left(int(cmd_list[cmd_list.index(c) + 1]))
                elif c == "rt":
                    turtlelist.right(int(cmd_list[cmd_list.index(c) + 1]))
                # else:
                #     cautraloi_cmdfalse()
        else :
            print("Your can choose( Color or Command or Color Command)")
            print("Please choose again")
            color_commad(tp)

while True:

    tp = int(input("Which one do you want to control?"))
    kiemcautraloi_turtlecandieukhienfalseortrue()
    if 9 > tp > 0 :
        turtlelist = turtle_list[tp - 1]
        colororcmd = input("Color or Command or Color Command")
        colororcmd = colororcmd.lower()
        colororcmd_list = colororcmd.split(" ")
        for _ in colororcmd_list :
            if _ == "color" :
                turtlelist.color(input("What color?"))
            elif _ == "command" :
                cmd = input("What command (fd + độ dài cần đi, bd + độ dài cần đi, lt + số đo góc, rt + số đo góc)")
                cmd = cmd.lower()
                cmd_list = cmd.split(" ")
                for c in cmd_list:
                    if c == "fd":
                        turtlelist.forward(int(cmd_list[cmd_list.index(c) + 1]))
                    elif c == "bd":
                        turtlelist.backward(int(cmd_list[cmd_list.index(c) + 1]))
                    elif c == "lt":
                        turtlelist.left(int(cmd_list[cmd_list.index(c) + 1]))
                    elif c == "rt":
                        turtlelist.right(int(cmd_list[cmd_list.index(c) + 1]))
                    # if cmd_list.index(c)%2 :
                        # if c != "fd" or c != "bd" or c != "lt" or c != "rt":
                            # cautraloi_cmdfalse()
            else :
                print("Your can choose( Color or Command or Color Command)")
                print("Please choose again")
                color_commad(tp)

mainloop()