lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))
result = []
for num in range(lower_range, upper_range + 1):
    sqrt = int(num ** 0.5)
    if sqrt * sqrt == num:
        digit_sum = sum(map(int, str(num)))
        if digit_sum < 10:
            result.append(num)
print(result)
         
