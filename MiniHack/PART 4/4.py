print("Nhập các dãy số")
dayso = input(">>>")
dayso = dayso.split(",")
dodaidayso = len(dayso)
for i in range(dodaidayso):
    dayso[i] = int(dayso[i])
tongdayso = 0
for i in range(dodaidayso):
    tongdayso += dayso[i]
print(tongdayso)