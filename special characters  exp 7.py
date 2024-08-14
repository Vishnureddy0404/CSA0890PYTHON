char = input("enter char:")
count=0
for i in char:
    if i in "~!@#$%^&*":
        count+=1
print("no.of sp char:",count)
