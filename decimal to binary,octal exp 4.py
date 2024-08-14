def decimal_to_binary(decimal_number):
    return bin(decimal_number).replace("0b","")
def decimal_to_octal(decimal_number):
    return bin(decimal_number).replace("0o","")
decimal_number=int(input("enter the decimal_number:"))
binary_number=decimal_to_binary(decimal_number)
octal_number = decimal_to_octal(decimal_number)
print(f"decimal_number:{decimal_number}")
print(f"binary equivlent:{binary_number}")
print(f"octal equivalent:{octal_number}")
