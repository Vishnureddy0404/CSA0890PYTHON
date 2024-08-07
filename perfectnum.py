num = int(input("Enter any Number: "))
Sum = 0
for i in range(1, num):
    if(num % i == 0):
        Sum = Sum + i
if (Sum == num):
    print(" %d is a Perfect Number" %num)
else:
    print(" %d is not a Perfect Number" %num)
