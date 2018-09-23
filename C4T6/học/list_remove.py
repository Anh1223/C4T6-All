color_list = ['red', 'blue' , 'yellow', 'teal']

while True:
    command = input("What's your command(add, remove, draw)?")
    command = command.lower()
    if command == "remove":
        color_list.remove(input("Color to remove"))
    elif command == "add":
        color_list.append(input("Color to append"))
    elif command == "draw":
        from turtle import*
        shape("turtle")
        hideturtle()
        penup()
        goto(-600, 0)
        for c in color_list:
            fillcolor(c)
            stamp()
            forward(200)

        mainloop()
    else:
        print("What?")

    for c in color_list:
        print(c)