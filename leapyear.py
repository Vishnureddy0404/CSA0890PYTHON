date = input("enter the date to check:")
c = date.split("/")
b = list(map(int,c))
input_year = (b[2])

if(input_year%4==0):
   if (input_year%100==0):
       if(input_year%400==0):
          print("%d is leap year:"%input_year)
       else:
           print("%d is not a leap year:"%input_year)
   else:
       print("%d is leap year:"%input_year)
else:
    print("% d is not a leap year:"%input_year)

x = input_year%4
if x!=0:
    print("Previous leap year:",input_year-x)
else:
    print("Next leap year :",input_year+4)
         
         
