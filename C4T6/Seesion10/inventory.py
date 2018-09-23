from stats import *
from random import *

def generate_item_name():
    f = choice(product_types)
    c = choice(material_types)
    l = choice(workmanship_levels)
    items_name = [f , c , l]
    return items_name

def item_after_combat():
    new_item = generate_item()
    while True:
        print("Một", new_item["NAME"], "vừa rơi ra")
        print("1. Xem")
        print("2. Nhặt")
        print("3. Bỏ qua")
        option = input(">>>")
        if option == "1":
            show_index(new_item)
        elif option == "2":
            add_item(new_item)
            print("Bạn đã nhặt", new_item["NAME"], "vào hòm")
            count_item()
            break
        elif option == "3":
            print("Bạn đã bỏ qua đồ")
            break

def add_item(item):
    items.append(item)

def count_item():
    count = len(items)
    print("Bạn có số", count, "đồ trong hòm")

def generate_item():
    name = generate_item_name()
    item = {
        "NAME": name,
        "HP": 0,
        "STR": 0,
        "DEF": 0,
        "LUCK": 0,
        "AGI": 0,
    }
    if f == product_types[1]:

    if f == product_types[2]:
    return items

def show_index(name_show_index):
    print("*"*15)
    for key, value in name_show_index.items():
        print("*", key, value)
    print("*"*15)
