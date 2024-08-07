num1 = int(input("enter the first integer:"))
num2 = int(input("enter the second integer:"))
result_and = num1&num2
result_or = num1|num2
result_xor = num1 ^ num2
result_left_shift = num1 << num2
result_right_shift = num1 >> num2
print("Bitwise AND:",bin(result_and))
print("Bitwise or:",bin(result_or))
print("Bitwise xor:",bin(result_xor))
print("Bitwise_left_shift:",bin(result_left_shift))
print("BItwise_right_shift:",bin(result_right_shift))
