a=[[1,2],
   [3,4]]
b=[[5,6],
   [7,8]]
c=[[9,10],
   [11,12]]
for i in range (len(a)):
    for j in range (len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
for r in c:
    print(r)
