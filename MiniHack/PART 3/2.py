while True:
    print("Nhập 1 số")
    so = int(input(">>>"))
    for i in range((so + 1) % 2):
        print("Ngu vãi")
        print("Ai chả biết số này là số chẵn")
    for i in range(so % 2):
        print("Ngu vãi")
        print("Ai chả biết số này là số lẻ")