color_list=["red","blue","purple",]
while True:
    new_color=input("New color?")
    color_list.append(new_color)
    print("*"*10)
    for color in color_list:
        print(color)
    print("*"*10)