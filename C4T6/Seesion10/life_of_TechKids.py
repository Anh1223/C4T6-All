from combat import *
from stats import *
from random import *

while True:
    cmd = input("Your command(Stats or Here)")
    cmd = cmd.lower()
    if cmd == "stats":
         show_index(player)
    elif cmd == "here":
        print("Bạn đang ở trước cửa TechKids")
        print("Bạn có 2 lựa chọn")
        print("1. Về TechKids")
        print("2. Đi vào khu rừng phía trước")
        option = input("Lựa chọn của bạn ?")
        if option == "1":
            print("Xin lỗi, đã hết giờ làm việc")
        elif option == "2":
            print("Bạn đã bước vào rừng")
            print("Bạn thấy một bình thủy dịch ở trên mặt đất")
            print("1. Bỏ qua")
            print("2. Nhặt lên sử dụng")
            option = input("Lựa chọn bạn")
            if option == "1":
                print("Tiếc quá")
                soluong_orc = randint(4, 8)
                print("Bạn gặp", soluong_orc, "con Orc")
                print("1. Chạy ra khỏi khu vực này")
                print("2. Nấp vào hang đá bên cạnh")
                print("3. ĐÁNH!!!")
                option = input("Lựa chọn của bạn?")
                if option == "1":
                    print("Do bạn chạy quá chậm nên đã bị Orc bắt đi")
                elif option == "2":
                    print("Con Orc không nhìn thấy")
                    print("Tuy nhiên bạn quay lại nhìn vào trong hanh, bạn thấy một đoàn sói")
                elif option == "3":
                    for danh_orc in range(soluong_orc):
                        print("OPPONENT")
                        show_index(Orc)
                        show_index(player)
                        combat_full(player, Orc)
                        Orc["HP"] = 60
                    break

            elif option == "2":
                player["HP"] = 100
                print("Bạn đã được hồi phục HP")
                print("HP", player["HP"])
                soluong_orc = randint(4, 8)
                print("Bạn gặp", soluong_orc, "con Orc")
                print("1. Chạy ra khỏi khu vực này")
                print("2. Nấp vào hang đá bên cạnh")
                print("3. ĐÁNH!!!")
                option = input("Lựa chọn của bạn?")
                if option == "1":
                    print("Do bạn chạy quá chậm nên đã bị Orc bắt đi")
                elif option == "2":
                    print("Con Orc không nhìn thấy bạn")
                    print("Tuy nhiên bạn quay lại nhìn vào trong hanh, bạn thấy một đàn sói")
                elif option == "3":
                    for danh_orc in range(soluong_orc):
                        print("OPPONENT")
                        show_index(Orc)
                        show_index(player)
                        combat_full(player, Orc)
                        Orc["HP"] = 60
                    break



    else :
        print("Hãy nhập lại")

print("Bạn đã tiến sâu vào rừng hơn")
print("........... chưa nghĩ ra phần sau")