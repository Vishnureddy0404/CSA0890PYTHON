n = int(input("enter the number:"))
if(n % 400 == 0 and n % 100 == 0):
    print("leap year")
elif (n % 4 == 0 ) and (n % 100!= 0):
    print("Leap year")
else:
    print("Not a leap year")
