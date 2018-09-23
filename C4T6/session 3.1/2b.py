n=int(input("Enter a number: "))
m=n//2
j=n+1
b=(" 1 0")
for y in range(j%2):
    print(b*m)
for i in range(n%2):
    print(b*m,1)