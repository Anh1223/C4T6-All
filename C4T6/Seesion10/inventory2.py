from random import choice

items = []

product_types = [
    "Kiếm",
    "Cung",
    "Giáo",
    "Khiên",
    "Rìu",
    "Súng",
    "Katana",
]

material_types = [
    " sắt",
    " gố",
    " vàng",
    " bạc",
    " titan",
    " kim cương",
    " bạch kim",
    " in 3D"
]

workmanship_levels = [
    " (áp dụng công nghệ nano)",
    " cao cấp",
    " dởm",
    " mini",
    " big",
    " heavy",
    " slight"
]



def generate_item_name():
    f = choice(product_types)
    c = choice(material_types)
    l = choice(workmanship_levels)
    items_name = f + c + l
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
            show_item(new_item)
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
        "AGT": 3,
        "HP": -1,
        "DEF": 2,
        "STR": 2,
    }
    return item
#
#
def show_item(game_item):
    print("* " * 15)

    for key, value in game_item.items():
        print("*", key, ":", value)

    print("* " * 15)

#
#
# steel_gauntlet = {
#     "NAME": "STEEL GAUNLET",
#     "HP": 10,
#     "AGI": 5,
#     "LUCK": 1,
# }
#
# bronze_shield = {
#     "NAME": "BRONZE SHIElD",
#     "HP": 5,
#     "AGI": 1,
# }
#
# golden_stick = {
#     "NAME": "GOLDEN STICK",
#     "AGI": 15,
#     "HP": 20,
#     "STR": 100,
# }
#
# inventory = [steel_gaunlet, bronze_shield, golden_stick]
# for item in inventory:
#     show_item(item)