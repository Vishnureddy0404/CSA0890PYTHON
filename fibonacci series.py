num = int(input("enter the terms:"))
a = 0
b = 1
count = 2
print("fibonacci series",num,end='')
print(a,end=',')
print(b,end=',')
while(count<num):
  c = (a+b)
  a = b
  b = c
print(c,end=',')
count +=1
