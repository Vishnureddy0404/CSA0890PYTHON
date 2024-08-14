l = list(map(int,input("enter the numbers:").split()))
u = []
for i in l:
    if i not in u and l.count(i)==1:
        u.append(i)
print(list(u))
